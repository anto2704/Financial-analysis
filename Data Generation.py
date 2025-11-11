"""
generate_cashflow.py
Generates 3 years of sparse, event-based cash flow records for construction projects.
Outputs: synthetic_construction_cashflows.csv
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from tqdm import tqdm

np.random.seed(42)

# Parameters
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)   # 3 full calendar years inclusive
projects = {
    # project_id: dict(size_scale, front_loadedness, avg_event_rate_per_month)
    "PJT_A": {"size": 4.0, "front_load": 0.8, "event_rate": 10},
    "PJT_B": {"size": 4.5, "front_load": 0.9, "event_rate": 10},
    "PJT_C": {"size": 2.0, "front_load": 0.65, "event_rate": 7},
    "PJT_D": {"size": 2.0, "front_load": 0.65, "event_rate": 7},
    "PJT_E": {"size": 1.0, "front_load": 0.4, "event_rate": 5},
    "PJT_F": {"size": 1.0, "front_load": 0.4, "event_rate": 5}
}

# Helper functions
def daterange(sd, ed):
    d = sd
    while d <= ed:
        yield d
        d += timedelta(days=1)

def poisson_events_per_year(event_rate_per_month):
    return int(event_rate_per_month * 12)

def clamp_nonneg(x):
    return max(0.0, x)

# Create milestone/invoice schedule and outflow events per project
records = []

for pid, cfg in projects.items():
    size = cfg["size"]
    front_load = cfg["front_load"]
    event_rate = cfg["event_rate"]
    total_events = poisson_events_per_year(event_rate)

    # Project lifecycle: phases change every ~12 months (concept drift)
    phase_change_dates = [
        start_date,
        start_date + timedelta(days=365),
        start_date + timedelta(days=730),
        start_date + timedelta(days=1064)
    ]

    # Starting cash (opening float) scaled by project size
    opening_cash_balance = 500000 * size + np.random.normal(0, 30000)
    opening_cash_balance = clamp_nonneg(opening_cash_balance)

    # Keep a ledger of receivable invoices (expected inflows) and their actual payment date
    invoices = []

    # Generate milestone invoice dates (irregular): more in earlier months if front-loaded
    days = []
    # Place expected events (invoices + outflows) randomly across the 3-year span, but biased to early year if front-loaded
    for _ in range(total_events):
        # sample a day index 0..(Ndays-1), biased by front_load
        total_days = (end_date - start_date).days + 1
        # Use Beta distribution to bias earlier if front_load high
        a = 1 + front_load * 5
        b = 1 + (1 - front_load) * 5
        frac = np.random.beta(a, b)
        day_index = int(frac * (total_days - 1))
        d = start_date + timedelta(days=day_index)
        days.append(d)

    # Add occasional large lump-sum outflow events (materials, mobilization)
    lump_count = max(3, int(3 * size))
    for _ in range(lump_count):
        # lumps more likely early for front-loaded projects
        total_days = (end_date - start_date).days + 1
        a = 1 + front_load * 6
        b = 2
        frac = np.random.beta(a, b)
        d = start_date + timedelta(days=int(frac * (total_days - 1)))
        days.append(d)

    # Add some random monthly smaller events
    # We will consolidate later by date
    # For each event day, decide whether it's invoice (expected inflow) or outflow or both
    day_events = {}
    for d in days:
        key = d.date()
        if key not in day_events:
            day_events[key] = []
        day_events[key].append("candidate")

    # Also add occasional events caused by subcontractor demands (unplanned)
    unplanned_count = int(2 * size)
    for _ in range(unplanned_count):
        d = start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days + 1))
        key = d.date()
        day_events.setdefault(key, []).append("unplanned")

    # Build chronological events and simulate cash flows
    # Use AR(1) process for net cash flow to get autocorrelation
    phi = 0.4  # autocorrelation coefficient
    prev_net = np.random.normal(0, 10000)

    # Keep track of receivables map: invoice_id -> dict(amount, expected_date, actual_date)
    receivables = []
    invoice_counter = 0

    # We'll iterate through all calendar days but only create records on event days.
    # To mimic real-world sparse reporting, we only create rows for days that had inflow/outflow.
    all_event_dates = sorted(day_events.keys())
    for d in sorted(all_event_dates):
        # Introduce small chance of multiple entries on same calendar day; we'll aggregate into one record per day
        # Decide which phase the project is in (affects payment terms and outflow intensity)
        days_since_start = (pd.to_datetime(d) - pd.to_datetime(start_date)).days
        if days_since_start < 365:
            phase = "setup"
        elif days_since_start < 730:
            phase = "execution1"
        elif days_since_start < 1064:
            phase = "execution2"
        else:
            phase = "finishing"

        # Payment terms and delays depend on phase
        if phase == "setup":
            term_mean = 45  # days to pay
            outflow_scale = 1.5
            invoice_rate = 0.7
        elif phase == "execution1":
            term_mean = 40
            outflow_scale = 1.0
            invoice_rate = 0.6
        elif phase == "execution2":
            term_mean = 30
            outflow_scale = 0.7
            invoice_rate = 0.5
        else:
            term_mean = 25
            outflow_scale = 0.5
            invoice_rate = 0.4

        # Determine expected inflow: some days issue invoices; some days receive payments
        # Probability of issuing an invoice vs receiving payment
        issue_invoice_prob = invoice_rate
        receive_payment_prob = 0.5

        expected_inflow = 0.0
        actual_inflow = 0.0
        expected_outflow = 0.0
        actual_outflow = 0.0

        # Opening cash is last closing cash; if first day use project opening cash
        if len(records) == 0 or all(r['project_id'] != pid for r in records):
            opening_cash = opening_cash_balance
        else:
            # find last record for this project
            prev = None
            for r in reversed(records):
                if r['project_id'] == pid:
                    prev = r
                    break
            opening_cash = prev['closing_cash']

        # Reserve contingency buffer: a percentage of size; ensure ring-fence
        reserve_pct = 0.05 + 0.05 * np.random.rand()  # between 5-10%
        reserve_buffer = opening_cash * reserve_pct

        # 1) Possibly issue invoice (expected inflow)
        if np.random.rand() < issue_invoice_prob:
            # invoice size varies by project size and phase
            base_invoice = 200000 * size * (0.2 + 0.8 * np.random.rand())
            # front-loading increases early invoices
            if phase == "setup":
                base_invoice *= (1.0 + front_load * 0.6)
            expected_inflow = round(base_invoice, 2)
            # Payment expected after some days (terms) with variability
            delay = int(np.clip(np.random.normal(term_mean, 8), 14, 90))
            expected_payment_date = pd.to_datetime(d) + pd.Timedelta(days=delay)
            # schedule receivable
            receivables.append({
                "invoice_id": f"{pid}_INV_{invoice_counter}",
                "issue_date": pd.to_datetime(d),
                "expected_payment_date": expected_payment_date,
                "amount": expected_inflow,
                "paid": False
            })
            invoice_counter += 1

        # 2) Possibly receive payments for past invoices (actual inflow)
        # Iterate receivables and decide if payment happens today (some may be late)
        for inv in receivables:
            if inv["paid"]:
                continue
            # Payment probability increases after expected date
            days_past_due = (pd.to_datetime(d) - inv["expected_payment_date"]).days
            if days_past_due >= 0:
                # probability grows with days_past_due; also some partial payments possible
                pay_prob = min(0.9, 0.25 + 0.03 * days_past_due + 0.1 * np.random.rand())
                if np.random.rand() < pay_prob:
                    # actual paid amount is around invoice amount with some partial/late reductions
                    late_penalty_factor = np.random.normal(1.0, 0.05)
                    # occasional partial payments (20% chance)
                    if np.random.rand() < 0.2:
                        paid_fraction = np.random.uniform(0.3, 0.9)
                    else:
                        paid_fraction = 1.0
                    paid_amount = round(inv["amount"] * paid_fraction * late_penalty_factor, 2)
                    actual_inflow += paid_amount
                    inv["paid"] = True
                    inv["actual_payment_date"] = pd.to_datetime(d)

        # 3) Expected outflow: planned supplier/subcontractor invoices (milestones)
        # On many event days we plan outflows; their expected amounts are set
        if np.random.rand() < 0.8:
            # expected outflow relates to project size, may be large in setup and finishing phases
            base_out = 150000 * size * (0.2 + np.random.rand())
            if phase == "setup":
                base_out *= (1.0 + front_load * 1.0)  # front-loaded cost multiplier
            if phase == "finishing":
                base_out *= 1.1
            expected_outflow = round(base_out, 2)

        # 4) Actual outflow: pay suppliers or subcontractors. We ensure actual outflow doesn't exceed available cash minus reserve.
        # Outflow volatility: multiply by random shock
        if expected_outflow > 0:
            vol = np.random.normal(1.0, 0.25)
            candidate_outflow = max(0.0, expected_outflow * vol)
            # occasional lump-sum spikes
            if np.random.rand() < 0.08:
                candidate_outflow *= (1.5 + np.random.rand() * 2.0)

            # Also allow some unplanned demands
            if "unplanned" in day_events[d]:
                candidate_outflow *= (1.0 + 0.5 * np.random.rand())

            # Ensure funds available: opening_cash + today's actual_inflow - reserve_buffer
            available_for_payments = opening_cash + actual_inflow - reserve_buffer
            available_for_payments = max(0.0, available_for_payments)
            # If cannot fully pay, pay part of it (simulate supplier put-on-hold rather than negative closing)
            actual_outflow = round(min(candidate_outflow, available_for_payments), 2)

        # 5) Net cash flow with AR(1) autocorrelation component
        # base_net = actual_inflow - actual_outflow
        # inject autocorrelation by blending with prev_net
        base_net = actual_inflow - actual_outflow
        noise = np.random.normal(0, 500 * size)  # noise scales with project size
        net_cash = phi * prev_net + (1 - phi) * base_net + noise
        # Round and make sure net_cash consistent with actuals (we will set actuals consistent)
        # To keep bookkeeping consistent: adjust actual_inflow or actual_outflow slightly so that actual_inflow - actual_outflow == net_cash (rounded)
        net_cash = round(net_cash, 2)
        # If discrepancy, adjust actual_inflow preserving non-negativity and available cash constraint
        discrepancy = net_cash - (actual_inflow - actual_outflow)
        if abs(discrepancy) > 1.0:
            # If discrepancy positive, increase actual_inflow by min(discrepancy, some small fraction of outstanding receivables)
            if discrepancy > 0:
                # try to realize payments from unpaid receivables
                unpaid_total = sum(inv["amount"] for inv in receivables if not inv["paid"])
                add_cash = min(discrepancy, unpaid_total, max(0.0, opening_cash * 0.2))
                if add_cash > 1.0:
                    actual_inflow += add_cash
                    # mark some receivables paid proportionally (soft simulation)
                    to_allocate = add_cash
                    for inv in receivables:
                        if not inv["paid"] and to_allocate > 0:
                            take = min(inv["amount"], to_allocate)
                            inv["paid"] = True
                            inv["actual_payment_date"] = pd.to_datetime(d)
                            to_allocate -= take
            else:
                # discrepancy negative: need to increase actual_outflow or reduce actual_inflow
                extra_needed = -discrepancy
                # can increase outflow up to available_for_payments
                available_for_payments = opening_cash + actual_inflow - reserve_buffer
                add_out = min(extra_needed, available_for_payments - actual_outflow)
                add_out = max(0.0, add_out)
                actual_outflow += add_out

        actual_inflow = round(actual_inflow, 2)
        actual_outflow = round(actual_outflow, 2)

        # Final consistency: prevent outflow > opening_cash + actual_inflow - reserve (again)
        available_for_payments = opening_cash + actual_inflow - reserve_buffer
        available_for_payments = max(0.0, available_for_payments)
        if actual_outflow > available_for_payments:
            actual_outflow = round(available_for_payments, 2)

        # Compute closing cash; never negative due to above guard
        closing_cash = opening_cash + actual_inflow - actual_outflow
        closing_cash = round(max(0.0, closing_cash), 2)

        # Save record only if there was activity (actual inflow or actual outflow) -- mimic sparse event-based entries
        if (actual_inflow > 0) or (actual_outflow > 0) or (expected_inflow > 0) or (expected_outflow > 0):
            rec = {
                "date": pd.to_datetime(d).date(),
                "project_id": pid,
                "expected_inflow": float(round(expected_inflow, 2)),
                "actual_inflow": float(actual_inflow),
                "expected_outflow": float(round(expected_outflow, 2)),
                "actual_outflow": float(actual_outflow),
                "opening_cash": float(round(opening_cash, 2)),
                "closing_cash": float(closing_cash),
                "net_cash_flow": float(round(actual_inflow - actual_outflow, 2))
            }
            records.append(rec)
            prev_net = net_cash

# Build DataFrame
df = pd.DataFrame(records)
# Sort by project and date
df = df.sort_values(["project_id", "date"]).reset_index(drop=True)

# Add forecasting-friendly columns: lagged net_cash_flow (t-1), and rolling stats (optional)
df["net_cash_flow_lag1"] = df.groupby("project_id")["net_cash_flow"].shift(1)
df["rolling_net_7"] = df.groupby("project_id")["net_cash_flow"].rolling(7, min_periods=1).mean().reset_index(level=0, drop=True)
df["rolling_outflow_30"] = df.groupby("project_id")["actual_outflow"].rolling(30, min_periods=1).mean().reset_index(level=0, drop=True)

# Final sanity checks: closing_cash non-negative (already enforced), outflow <= opening + inflow
violations = df[df["actual_outflow"] > (df["opening_cash"] + df["actual_inflow"]) + 1e-6]
if not violations.empty:
    print("Warning: outflow > opening+inflow in some rows (should be none). Rows:", len(violations))

# Save to CSV
out_fname = "competitor2.csv"
df.to_csv(out_fname, index=False)
print(f"Saved {len(df)} event rows to {out_fname}")

# Print a small sample per project
for pid in projects.keys():
    print(f"\nSample for {pid}:")
    print(df[df["project_id"] == pid].head(5).to_string(index=False))
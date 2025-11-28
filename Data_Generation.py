"""
generate_cashflow_v3_FIXED.py
Fixes for: (1) Revenue tracking, (2) Current Liabilities calculation, (3) COGS clarity
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

# Parameters
start_date = datetime(2022, 1, 1)
end_date = datetime(2025, 11, 30)
projects = {
    "PJT_A": {"size": 5.0, "front_load": 0.9, "event_rate": 15},
    "PJT_B": {"size": 1.0, "front_load": 0.45, "event_rate": 5},
    "PJT_C": {"size": 2.0, "front_load": 0.7, "event_rate": 10},
}


def poisson_events_per_year(event_rate_per_month):
    return int(event_rate_per_month * 12)


def clamp_nonneg(x):
    return max(0.0, x)


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)


records = []

for pid, cfg in projects.items():
    size = cfg["size"]
    front_load = cfg["front_load"]
    event_rate = cfg["event_rate"]
    total_events = poisson_events_per_year(event_rate)

    phase_change_dates = [
        start_date,
        start_date + timedelta(days=365),
        start_date + timedelta(days=730),
        start_date + timedelta(days=1064)
    ]

    opening_cash_balance = 500000 * size + np.random.normal(0, 30000)
    opening_cash_balance = clamp_nonneg(opening_cash_balance)

    # ==================== FIX #1: PROPER ACCOUNTING STATE ====================
    # Separate Revenue (accrual) from Cash Inflow (cash basis)
    project_accounts_receivable = 0.0
    project_accounts_payable = 0.0
    project_accrued_expenses = 0.0  # NEW: Track accrued (not yet paid) expenses

    # Track invoices issued (revenue recognition) and their payment status
    issued_invoices = []
    invoice_counter = 0

    # Track supplier/COGS invoices received (expense recognition)
    supplier_invoices = []
    supplier_counter = 0

    days = []
    total_days_span = (end_date - start_date).days + 1

    for _ in range(total_events):
        a = 1 + front_load * 5
        b = 1 + (1 - front_load) * 5
        frac = np.random.beta(a, b)
        day_index = int(frac * (total_days_span - 1))
        d = start_date + timedelta(days=day_index)
        days.append(d)

    lump_count = max(3, int(3 * size))
    for _ in range(lump_count):
        a = 1 + front_load * 6
        b = 2
        frac = np.random.beta(a, b)
        d = start_date + timedelta(days=int(frac * (total_days_span - 1)))
        days.append(d)

    unplanned_count = int(2 * size)
    for _ in range(unplanned_count):
        d = start_date + timedelta(days=np.random.randint(0, total_days_span))
        days.append(d)

    day_events = {}
    for d in days:
        key = d.date()
        if key not in day_events:
            day_events[key] = []
        day_events[key].append("candidate")

    unplanned_count = int(2 * size)
    for _ in range(unplanned_count):
        d = start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days + 1))
        key = d.date()
        day_events.setdefault(key, []).append("unplanned")

    phi = 0.4
    prev_net = np.random.normal(0, 10000)

    all_calendar_dates = list(daterange(start_date.date(), end_date.date()))

    for d_date in all_calendar_dates:
        d = pd.to_datetime(d_date)

        days_since_start = (d - start_date).days
        if days_since_start < 365:
            phase = "setup"
        elif days_since_start < 730:
            phase = "execution1"
        elif days_since_start < 1064:
            phase = "execution2"
        else:
            phase = "finishing"

        if phase == "setup":
            invoice_rate = 0.5
            payment_term_mean = 60
            outflow_scale = 1.75
        elif phase == "execution1":
            invoice_rate = 0.7
            payment_term_mean = 45
            outflow_scale = 1.0
        elif phase == "execution2":
            invoice_rate = 0.6
            payment_term_mean = 30
            outflow_scale = 0.7
        else:
            invoice_rate = 0.8
            payment_term_mean = 15
            outflow_scale = 0.5

        # Initialize daily values
        revenue_recognized = 0.0  # NEW: Revenue (accrual basis)
        actual_cash_inflow = 0.0  # Cash received
        cogs_expense_recognized = 0.0  # COGS expense (accrual)
        actual_cash_outflow = 0.0  # Cash paid
        accrued_expenses_delta = 0.0  # Change in accrued expenses

        if len(records) == 0 or all(r['project_id'] != pid for r in records):
            opening_cash = opening_cash_balance
        else:
            prev = next((r for r in reversed(records) if r['project_id'] == pid), None)
            opening_cash = prev['closing_cash'] if prev else opening_cash_balance

        reserve_pct = 0.05 + 0.05 * np.random.rand()
        reserve_buffer = opening_cash * reserve_pct

        # ==================== FIX #1a: REVENUE RECOGNITION ====================
        if d_date in day_events:

            # 1) ISSUE INVOICE (Revenue Recognition - Accrual)
            if np.random.rand() < invoice_rate:
                base_invoice = 200000 * size * (0.2 + 0.8 * np.random.rand())
                if phase == "setup":
                    base_invoice *= (1.0 + front_load * 0.6)

                revenue_recognized = round(base_invoice, 2)
                project_accounts_receivable += revenue_recognized

                # Payment expected after term_mean days
                delay = int(np.clip(np.random.normal(payment_term_mean, 8), 14, 90))
                expected_payment_date = d + pd.Timedelta(days=delay)

                issued_invoices.append({
                    "invoice_id": f"{pid}_INV_{invoice_counter}",
                    "issue_date": d,
                    "expected_payment_date": expected_payment_date,
                    "amount": revenue_recognized,
                    "paid": False,
                    "actual_payment_date": None
                })
                invoice_counter += 1

            # 2) RECEIVE PAYMENTS (Cash Inflow)
            unpaid_invoices = [inv for inv in issued_invoices if not inv["paid"]]
            for inv in unpaid_invoices:
                days_past_due = (d - inv["expected_payment_date"]).days
                if days_past_due >= 0:
                    # Probability increases over time past due
                    pay_prob = min(0.95, 0.25 + 0.03 * days_past_due + 0.1 * np.random.rand())
                    if np.random.rand() < pay_prob:
                        # Late payment penalty (increases with days late)
                        penalty_rate = max(1.0, 1.0 + 0.005 * max(0, days_past_due))
                        paid_fraction = np.random.uniform(0.95, 1.05)
                        paid_amount = round(inv["amount"] * paid_fraction * penalty_rate, 2)

                        actual_cash_inflow += paid_amount
                        inv["paid"] = True
                        inv["actual_payment_date"] = d

                        # Reduce AR (payment received)
                        project_accounts_receivable = max(0.0,
                                                          project_accounts_receivable - paid_amount)

            # ==================== FIX #3: PROPER COGS RECOGNITION ====================
            # 3) RECOGNIZE COGS EXPENSE (Accrual - when purchase order placed)
            if np.random.rand() < 0.8:
                base_cogs = 150000 * size * (0.2 + np.random.rand())
                if phase == "setup":
                    base_cogs *= (1.0 + front_load * 1.0)
                if phase == "finishing":
                    base_cogs *= 1.1

                cogs_expense_recognized = round(base_cogs, 2)

                # COGS is matched to AP (liability when expense incurred)
                project_accounts_payable += cogs_expense_recognized

                # Also track in accrued expenses (portion not paid yet)
                accrued_expenses_delta = cogs_expense_recognized
                project_accrued_expenses += accrued_expenses_delta

                # Track supplier invoice for payment
                supplier_invoices.append({
                    "supplier_id": f"{pid}_SUP_{supplier_counter}",
                    "issue_date": d,
                    "amount": cogs_expense_recognized,
                    "payment_terms_days": np.random.randint(15, 60),
                    "paid": False,
                    "actual_payment_date": None
                })
                supplier_counter += 1

            # 4) PAY SUPPLIERS (Cash Outflow)
            unpaid_suppliers = [sup for sup in supplier_invoices if not sup["paid"]]
            for sup in unpaid_suppliers:
                expected_pay_date = sup["issue_date"] + pd.Timedelta(days=sup["payment_terms_days"])
                if d >= expected_pay_date:
                    # Probability increases over time
                    days_past_term = (d - expected_pay_date).days
                    pay_prob = min(0.9, 0.3 + 0.02 * days_past_term + 0.1 * np.random.rand())

                    if np.random.rand() < pay_prob:
                        available_cash = opening_cash + actual_cash_inflow - reserve_buffer
                        available_cash = max(0.0, available_cash)

                        # Pay full amount or what's available
                        payment = min(sup["amount"], available_cash)
                        actual_cash_outflow += payment

                        sup["paid"] = True
                        sup["actual_payment_date"] = d

                        # Reduce AP and accrued expenses
                        project_accounts_payable = max(0.0,
                                                       project_accounts_payable - payment)
                        project_accrued_expenses = max(0.0,
                                                       project_accrued_expenses - payment)

        # ==================== FIX #2: PROPER CURRENT LIABILITIES ====================
        # Current Liabilities = AP + Accrued Expenses (not random multiplier!)
        # This is more stable and contable-aligned
        current_liabilities = round(project_accounts_payable + project_accrued_expenses, 2)

        # Net cash flow
        base_net = actual_cash_inflow - actual_cash_outflow
        noise = np.random.normal(0, 500 * size)
        net_cash = 0.4 * prev_net + (1 - 0.4) * base_net + noise
        net_cash = round(actual_cash_inflow - actual_cash_outflow, 2)
        closing_cash = round(max(0.0, opening_cash + net_cash), 2)

        is_activity = (actual_cash_inflow > 0) or (actual_cash_outflow > 0) or \
                      (revenue_recognized > 0) or (cogs_expense_recognized > 0)
        is_state_change = d_date in day_events

        if is_activity or is_state_change:
            rec = {
                "date": d_date,
                "project_id": pid,

                # ===== ACCRUAL BASIS (Revenue & Expenses) =====
                "revenue_recognized": float(round(revenue_recognized, 2)),
                "cogs_expense": float(round(cogs_expense_recognized, 2)),

                # ===== CASH BASIS (Inflows & Outflows) =====
                "cash_inflow": float(actual_cash_inflow),
                "cash_outflow": float(actual_cash_outflow),

                # ===== BALANCE SHEET ITEMS =====
                "accounts_receivable": float(round(project_accounts_receivable, 2)),
                "accounts_payable": float(round(project_accounts_payable, 2)),
                "accrued_expenses": float(round(project_accrued_expenses, 2)),
                "current_liabilities": float(current_liabilities),

                # ===== CASH ITEMS =====
                "opening_cash": float(round(opening_cash, 2)),
                "closing_cash": float(closing_cash),
                "net_cash_flow": float(net_cash),
                "reserve_buffer": float(round(reserve_buffer, 2)),
            }
            records.append(rec)
            prev_net = net_cash

# Build DataFrame
df = pd.DataFrame(records)
df = df.sort_values(["project_id", "date"]).reset_index(drop=True)

# ==================== RATIO CALCULATIONS - NOW CORRECT ====================

# 1. Rolling Averages (30-day windows)
df["rolling_revenue_30"] = df.groupby("project_id")["revenue_recognized"].rolling(30, min_periods=1).sum().reset_index(
    level=0, drop=True)
df["rolling_cogs_30"] = df.groupby("project_id")["cogs_expense"].rolling(30, min_periods=1).sum().reset_index(level=0,
                                                                                                              drop=True)
df["rolling_cash_inflow_30"] = df.groupby("project_id")["cash_inflow"].rolling(30, min_periods=1).sum().reset_index(
    level=0, drop=True)
df["rolling_ar_30"] = df.groupby("project_id")["accounts_receivable"].rolling(30, min_periods=1).mean().reset_index(
    level=0, drop=True)
df["rolling_ap_30"] = df.groupby("project_id")["accounts_payable"].rolling(30, min_periods=1).mean().reset_index(
    level=0, drop=True)
df["rolling_cl_30"] = df.groupby("project_id")["current_liabilities"].rolling(30, min_periods=1).mean().reset_index(
    level=0, drop=True)

# Avoid division by zero
df["avg_daily_revenue_30"] = (df["rolling_revenue_30"] / 30).replace(0, 1e-6)
df["avg_daily_cogs_30"] = (df["rolling_cogs_30"] / 30).replace(0, 1e-6)

# ==================== FIX #1: DSU NOW USES REVENUE (NOT CASH INFLOW) ====================
# DSU = (Accounts Receivable / Average Daily Revenue)
# This is the CORRECT formula: measures how long it takes to collect payments
df["dsu_days_sales_uncollected"] = df["rolling_ar_30"] / df["avg_daily_revenue_30"]
df["dsu_days_sales_uncollected"] = df["dsu_days_sales_uncollected"].clip(0, 120)

# ==================== DPO (Already correct, but clarified) ====================
# DPO = (Accounts Payable / Average Daily COGS)
# Measures how long the project takes to pay suppliers
df["dpo_days_payables_outstanding"] = df["rolling_ap_30"] / df["avg_daily_cogs_30"]
df["dpo_days_payables_outstanding"] = df["dpo_days_payables_outstanding"].clip(0, 120)

# ==================== OCF Ratio ====================
# OCF Ratio = Net Cash Flow / Current Liabilities
# Measures liquidity: ability to cover short-term obligations with daily cash
df["ocf_ratio"] = df["net_cash_flow"] / df["rolling_cl_30"]
df.loc[df["rolling_cl_30"] == 0, "ocf_ratio"] = 1.0

# Working Capital Cycle (Cash Conversion Cycle proxy)
# CCC = DSU + DPO (how many days cash is tied up)
df["working_capital_cycle_days"] = (
        df["dsu_days_sales_uncollected"] + df["dpo_days_payables_outstanding"]
).clip(0, 200)

# Additional ML features
df["net_cash_flow_lag1"] = df.groupby("project_id")["net_cash_flow"].shift(1)
df["rolling_net_7"] = df.groupby("project_id")["net_cash_flow"].rolling(7, min_periods=1).mean().reset_index(level=0,
                                                                                                             drop=True)
df["rolling_cash_outflow_30"] = df.groupby("project_id")["cash_outflow"].rolling(30, min_periods=1).mean().reset_index(
    level=0, drop=True)

# Drop intermediate rolling columns
columns_to_drop = [
    "rolling_revenue_30", "rolling_cogs_30", "rolling_cash_inflow_30",
    "rolling_ar_30", "rolling_ap_30", "rolling_cl_30",
    "avg_daily_revenue_30", "avg_daily_cogs_30"
]
df = df.drop(columns=columns_to_drop)

# Final output
out_fname = "saipem_dataset.csv"
df.to_csv(out_fname, index=False)
print(f"✓ Saved {len(df)} event rows to {out_fname}")

print("\n=== FIXED DATASET STRUCTURE ===")
print("\nColumns:")
print(df.columns.tolist())

print("\n=== Sample Data ===")
for pid in projects.keys():
    print(f"\n{pid}:")
    sample = df[df["project_id"] == pid].iloc[10:15]
    print(sample[["date", "revenue_recognized", "cash_inflow", "accounts_receivable",
                  "cogs_expense", "accounts_payable", "dsu_days_sales_uncollected",
                  "dpo_days_payables_outstanding", "ocf_ratio"]].to_string(index=False))

print("\n=== KEY METRICS RANGES ===")
print(
    f"DSU (Days Sales Uncollected): {df['dsu_days_sales_uncollected'].min():.1f} - {df['dsu_days_sales_uncollected'].max():.1f} days")
print(
    f"DPO (Days Payables Outstanding): {df['dpo_days_payables_outstanding'].min():.1f} - {df['dpo_days_payables_outstanding'].max():.1f} days")
print(f"OCF Ratio: {df['ocf_ratio'].min():.2f} - {df['ocf_ratio'].max():.2f}")
print(
    f"Working Capital Cycle: {df['working_capital_cycle_days'].min():.1f} - {df['working_capital_cycle_days'].max():.1f} days")
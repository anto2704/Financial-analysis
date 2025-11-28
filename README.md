# Cash Flow Crystal Ball - Predictive Liquidity in Construction

## Amir Gaddour, Antonio Bellomo, Arianna Veledi, Marco Briglia, Selina Hajarat, Udit Gagnani 

## 1 Introduction

The construction industry, valued at nearly two trillion U.S. dollars in 2023 and projected to reach
2.24 trillion by 2027[1], faces persistent cash flow management challenges that directly affect project
success and business sustainability. The purpose of a cash flow statement is to provide a detailed
picture of cash inflows and outflows during a given period, reflecting a company’s short- and long-term
operational capability[2]. According to the Construction Industry Institute, nearly 60% of construc-
tion firms experience cash flow difficulties, leading to payment delays, project disruptions, and even
business closures[3]. Ineffective liquidity management and poor payment term alignment often signal
potential financial distress[4].

We selected Saipem as the focal company after comparing its cash-flow dynamics with its competi-
tors. Saipem shows:

1. Volatility in operating cash flow (–477k in 2022 to 1,061k in 2024).
2. Weak operating cash-flow ratio (0.12 in 2024), far below Fluor’s (∼0.27)
3. Steep fall of cash balance from 2,136k (2023) to 1,410k (2024) while current liabilities rose to
    8,564k.
4. Financing flows swung from +871k (2022) to –544k (2024).

These patterns, like large liabilities, declining cash reserves, volatile OCF and financing dependency,
signal liquidity stress and make Saipem a high-impact candidate for a daily cash-flow forecasting
prototype (benchmarked against Fluor, the 3rd Company).

## 2 Industry Dynamics and Liquidity Assessment

## 2.1 Construction Industry Problem Scope

The construction industry operates within a uniquely volatile financial environment characterized
by irregular cash inflows, improper inventory management, extended payment cycles, and unexpected
changes in projects. Unlike manufacturing or retail, construction projects depend on milestone-based
billing, progress certifications, and client approvals. These are factors that often delay receivables and
cause liquidity strain even in otherwise profitable firms[5].

The sector’s capital-intensive structure further complicates liquidity management. Contractors
must commit substantial funds upfront for materials, labor, and equipment before receiving client
payments. This imbalance, combined with retention clauses and pay-when-paid contracts, makes cash
flow forecasting a critical determinant of survival rather than merely profitability. Real-world cases,
such as Carillion plc’s 2018 collapse in the UK, highlight how aggressive revenue recognition and in-
adequate forecasting can lead to insolvency despite strong order books[6].

This is precisely why we chose the construction sector for our study: the cash-flow fragility inherent
to this industry presents both an urgent challenge and a vast opportunity. These misforecasts of daily


inflows and outflows ultimately slow national economic growth and disrupt public services. By apply-
ing a predictive cash-flow model at a smaller scale, construction companies can strengthen liquidity,
optimise working-capital cycles, and enhance operational resilience. In turn, this supports faster in-
frastructure delivery, improved industry stability, and broader contributions to national development
and competitiveness.

### 2.2 Company and Competitor Evaluation

This section summarises the three companies analysed in our projects (Saipem, Fluor and AECOM)
and explains why Saipem was selected as the core case for our data-driven liquidity analysis. All three
belong to the broader engineering and construction universe, but they occupy different positions along
the spectrum from asset-heavy EPC contractors to more asset-light, consulting-driven models. This
diversity allows us to benchmark Saipem’s recent turnaround against both a structurally more fragile
EPC peer (Fluor) and a structurally more resilient, service-oriented peer (AECOM).

2.2.1 Company Profiles

Saipem S.p.A. is an Italy-based engineering, procurement, construction and installation (EPCI) com-
pany focused on large and complex energy and infrastructure projects. Its core activities include off-
shore and onshore engineering and construction, subsea pipelines and marine operations. The business
model is typical of heavy EPC contractors: multi-year projects, a mix of lump-sum and reimbursable
contracts, high capital intensity and significant exposure to project execution risk and working-capital
swings. Over the last decade Saipem has moved from a period of severe financial stress and high
leverage to a much stronger, de-leveraged position with record backlog and renewed profitability.

Fluor Corporation is a US-based global EPC player that designs, builds and maintains large in-
dustrial plants and infrastructure across energy, chemicals, mining and metals, infrastructure and
government services. Like Saipem, Fluor operates with a project-based revenue model and takes on
significant execution and contract risk. However, our common-size analysis shows that its profitability
and cash generation remain structurally fragile, with thin operating margins and strong dependence
on the timing of client payments and supplier settlements.

AECOM is a global leader in infrastructure consulting and professional services. Unlike Saipem and
Fluor, it operates with a more asset-light, service-oriented model: a large share of revenue comes from
design, advisory and project management, often under time-and-materials or cost-plus contracts. This
translates into more stable margins, lower capital intensity and generally smoother working-capital
dynamics. AECOM is thus a useful comparator to show how liquidity risk can be structurally lower
when the business mix is less exposed to lump-sum EPC execution risk.

2.2.2 Key Financial Metrics: Saipem, Fluor and AECOM

Table 1 summarises Saipem’s main financial indicators over the 2022–2025 period. The data highlight
a clear turnaround story: strong revenue growth, a swing from losses to solid profits, rapidly expanding
adjusted EBITDA, and a record order backlog. Most importantly for our project, operational working
capital has shifted from a large cash outflow in 2022 to sustained inflows from 2023 onward, while
the net financial position has moved from net debt to a sizeable net cash position. Saipem therefore
exemplifies how improved working-capital discipline and forecasting can transform the liquidity profile
of a heavy EPC contractor.

Table 2 shows that Fluor operates with sizeable revenue and a comfortable net cash position, but
with structurally thin margins and highly variable operating cash flow. Net income oscillates from
a loss in 2021 to modest profits in 2022–2023 and then to unusually high figures in 2024 and on a
TTM basis, driven largely by non-operating gains. Operating cash flow, however, remains in the low
single-digit percentage of revenue, and the balance sheet is dominated by current assets financed by
current liabilities. This configuration makes liquidity strongly dependent on the timing of collections
and payments, which is exactly the friction our project aims to address.


```
Table 1: Saipem: Key financial and liquidity indicators
Financial Metric Year Value Key Trend / Change
Revenue (Turnover) 2022 €9,980m
2023 €11,874m +19% YoY
2024 €14,549m +22.5% YoY
Net Result (Profitability) 2022 €209m loss Turnaround phase
2023 €179m profit Back to profit
2024 €306m profit Continued improvement
Adjusted EBITDA Growth 2023 – +55.6% vs 2022
2024 – +43.5% vs 2023
Order Backlog YE 2024 €34.1bn Multi-year visibility (2025–2028)
Operational Working Capital 2022 €450m outflow Cash drag from legacy projects
2023 €294m inflow Strong reversal
2024 €111m inflow Positive trend confirmed
9M 2025 €112m inflow Still positive
Net Financial Position (pre-
IFRS 16)
```
```
2021 Net Debt Highly leveraged
```
```
2022 Net Cash €56m Debt → cash
YE 2024 Net Cash €683m Strong balance sheet
9M 2025 Net Cash €844m Further improvement
```
```
Table 2: Fluor: Profitability, cash-flow and working-capital profile
Metric Year Value Trend
Revenue 2021 $14.2bn Base year
2022 $13.7bn –2.9%
2023 $15.5bn +12.6%
2024 $16.3bn +5.4%
Net Margin 2021 –3.1% Loss
2022 1.1% Small profit
2023 0.9% Low margin
2024 13.1% Non-operating effects
TTM 25.4% Not structural
Operating Cash Flow Margin 2021 0.2% Thin cash generation
2022 0.2% Flat
2023 1.4% Slightly better
2024 5.1% Best year
TTM 2.1% Normalises lower
Current Assets / Assets 2021–23 72–74% High working capital
2024/TTM 56.6% Still high
Net Receivables / Assets 2021–23 30% High dependence
2024/TTM 22.5% Still large
Cash + Investments / Assets 2021–TTM 32–38% Strong liquidity buffer
Current Liabilities / Assets 2021–23 45–51% Reliance on short-term funding
2024/TTM 33.6% Deleveraging
```
Table 3 summarises AECOM’s key indicators and underlines how its consulting-driven model trans-
lates into steady profitability, strong operating cash flow and high free cash-flow generation. A large,
diversified backlog supports visibility, while efficient working capital and moderate leverage keep liq-
uidity risk structurally low. Compared with Saipem and Fluor, AECOM serves as a benchmark at the
”low-risk” end of the engineering and construction spectrum.


```
Table 3: AECOM: Key Financial Metrics (2023–2025)
Financial Metric Year Value / Description Key Change / Trend
Revenue (Total revenue) 2023 (FY
ended Sept
30)
```
```
US$ 14,378.5 M Base for 2024 comparison
```
```
2024 US$ 16,105.5 M +12.0% vs 2023 — strong growth
driven by demand across end
markets
2025 (FY
ended Sept
30)
```
```
≈ US$ 16,140 M Flat vs 2024 — stable perfor-
mance
```
```
Gross profit margin / Gross
profit % of revenue
```
```
2023 ∼6.6% —
```
```
2024 ∼6.7% Slight improvement; cost control
maintained
Net income (net margin % of rev-
enue)
```
```
2023 Net income margin≈
0.7%
```
```
Low profitability — restructur-
ing, project mix, pass-through
effects
2024 Net income margin≈
2.5% (US$ 402.3 M)
```
```
Significant rebound vs 2023
```
```
2025 (contin-
uing opera-
tions)
```
```
Net income≈ US$ 638 M
(3.96% margin)
```
```
Further improvement — stronger
earnings
```
```
Operating cash flow (absolute) 2023 US$ 696 M —
2024 US$ 827.5 M +18.9% vs 2023 — stronger cash
generation
2025 US$ 822 M Slight dip vs 2024 — still strong
Working capital (CA – CL) 2023 (as of
Sept 30)
```
```
≈ US$ 319.2 M Modest working capital base
```
```
2024 (as of
Sept 30)
```
```
≈ US$ 802.0 M Large increase (+151%) — im-
proved liquidity
Net receivables & contract assets
(net)
```
```
2023 (as of
Sept 30)
```
```
≈ US$ 2,880.8 M —
```
```
2024 (as of
Sept 30)
```
```
≈ US$ 3,301.4 M Increase — reflects higher
project volume
Cash & short-term investments 2023 (as of
Sept 30)
```
```
≈ US$ 1,262.2 M —
```
```
2024 (as of
Sept 30)
```
```
≈ US$ 1,584.9 M +25.6% vs 2023 — stronger liq-
uidity position
```
2.2.3 Comparative assessment and rationale for selecting Saipem as core case

The objective of the project is to analyze liquidity risk in construction and EPC (Engineering,
Procurement, Construction) companies, with a focus on how working capital and contract structures
translate into cash tensions or cash generation. After reviewing their financial and qualitative profiles,
Saipem was selected as the main case company because it illustrates, better than the others, full
liquidity and balance-sheet turnaround within a classic EPC business model Saipem combines strong
recent growth with an improvement in margins and earnings:

- Revenue increased from €9,980m in 2022 to €11,874m in 2023 and €14,549m in 2024, with
    double-digit growth of +19.0% and +22.5% respectively.
- Adjusted EBITDA rose from €595m in 2022 to €926m in 2023 and €1,329m in 2024, implying
    cumulative growth of more than 120% over two years.
- Net result shifted from a €209m loss in 2022 to a €179m profit in 2023 and €306m profit in
    2024, confirming that the recovery is not only operational but also at the bottom line.
- Backlog increased from €24,017m in 2022 to €29,802m in 2023 and €34,065m in 2024, providing
    strong visibility for the 2025–2028 plan.


```
The analysis of changes in operational working capital shows:
```
- 2022: –€450m
- 2023: +€294m
- 2024: +€111m
- 9M 2025: +€112m

For our project this pattern is extremely valuable: it allows us to quantify the impact of contract
structure and working-capital discipline on the ability to transform revenues into cash.

Saipem also provides a clear example of de-leveraging supported by operational cash generation,
rather than by asset disposals alone:

- The company moves from net debt in 2021 to net cash of €56m in 2022,
- then to €216m net cash in 2023,
- €683m net cash in 2024,
- and €844m net cash in 9M 2025

Saipem is the most suitable main case for a project on liquidity in construction companies. It
offers:

- A clear numerical story of distress, recovery and strengthening.
- Direct evidence of how working capital management can transform liquidity risk into a liquidity
    source.
- A strong comparative angle against both a highly stable peer (AECOM) and a structurally con-
    strained one (Fluor).

```
This makes Saipem the ideal focal point for developing analytical tools, dashboards and predictive
models aimed at understanding and managing liquidity in the EPC and construction sector.
```
## 3 A Robust Synthetic Dataset for Predictive Liquidity

This project addresses the critical liquidity problem faced by Construction firms: the high risk of cash
shortages when future inflows and outflows are poorly forecast. To develop a robust predictive model
for daily cash flow, a comprehensive and realistic dataset is essential. Since real-world proprietary
data is unavailable, this project uses a Python script to generate a synthetic dataset that meticulously
models complex financial and operational realities.

### 3.1 The Necessity of Synthetic Dataset

Creating synthetic data, rather than relying on random numbers, is crucial for developing an effective
predictive model. A successful cash flow model must learn the complex relationships and dependencies
governing financial transactions. Our dataset ensures, while artificial, it strictly follows the funda-
mental accounting principles and financial logic, producing a high-fidelity simulation of a construction
project’s finances.


### 3.2 Financial Logic and Accounting Fidelity

The Python script is engineered to reflect the difference between Accrual Basis (when revenue or
expense is recognized) and Cash Basis (when cash is actually transferred), which is the core of cash
flow analysis. Dual Tracking of Revenue and Expense

- Revenue Recognition (Accrual) occurs when an invoice is issued, increasing the Accounts Re-
    ceivable (AR) balance.
- Cash Inflow (Cash Basis) occurs later when the invoice is paid, decreasing AR.
- Similarly, COGS Expense (Accrual) is recognized when a supplier order is placed, increasing
    Accounts Payable (AP) and Accrued Expenses.
- Cash Outflow (Cash Basis) occurs when the supplier is paid, decreasing AP and Accrued Ex-
    penses.

### 3.3 Current Liabilities Fix

The script correctly calculates Current Liabilities as the sum of Accounts Payable and Accrued
Expenses, providing an accurate measure of short-term obligations.

### 3.4 Liquidity Management Simulation

```
To enhance realism, the script simulates practical financial constraints:
```
- An openingcash balance is established for each project based on its size.
- A reservebuffer is calculated and effectively reserved, meaning supplier payments are constrained
    by available cash after accounting for this buffer, simulating prudent financial management.

### 3.5 Key Financial Ratios for Model Training

The dataset incorporates critical financial ratios, which serve as essential features for a machine
learning model focused on liquidity and efficiency:

- Days Sales Uncollected (DSU): Measures the average number of days it takes to bill and
    receive customer payments.[7]

#### DSU =

```
Accounts Receivable
Average Daily Revenue
```
- Days Payables Outstanding (DPO): Measures the average number of days a company takes
    to process invoices and pay suppliers.[7]

#### DPO =

```
Accounts Payable
Average Daily COGS
```
- Working Capital Cycle (WCC) / Cash Conversion Cycle (CCC) Proxy: measurement
    of a company’s cash flow efficiency—how long cash is tied up in operations before becoming
    available for reinvestment.[8]
       WCC = DSU + DPO
- Operating Cash Flow (OCF) Ratio: A liquidity ratio, it measures how well a company can
    pay off its current liabilities with the cash flow generated from its core business operations. This
    financial metric shows how much a company earns from its operating activities, per dollar of
    current liabilities.[9]
       OCF Ratio =
          Net Cash Flow
Current Liabilities


### 3.6 Operational Realism and Feature Engineering

The simulation is made highly realistic by modeling core project dynamics:
Project Differentiation: Different projects (A, B, C) have varying size, eventrate, and frontload
parameters, which dictate overall cash volume and the distribution of financial activities over time.

Phase-Dependent Activity: Financial behavior changes based on the project’s phase (setup,
execution, finishing), adjusting invoice rates, payment terms, and outflow scale to match typical con-
struction lifecycles.

Stochastic and Structured Events. Transactions are generated with both structured (based
on project size and front-load) and unplanned randomness, providing the necessary noise and unpre-
dictability of real-world construction.

The resulting dataset, rich in both raw transaction data and derived financial metrics (like the
30-day rolling averages and lag features), provides a robust foundation for building a highly accurate
Predictive Liquidity model.

## 4 Data Preprocessing and Dataset Understanding

### 4.1 Overview and Meaning of the Datasets

This section of the project is dedicated to the preprocessing and exploratory analysis of the dataset
generated in the previous phase, with the aim of gaining a thorough understanding of the variables
involved in the subsequent stages of analysis and properly preparing the data for the application of
the linear regression model.

The dataset analyzed represent synthetic construction company cash flow data over time. It contain
time-series financial information, focused primarily on cash movements related to construction project
operations. The core variables revolve around cash inflows, cash outflows, and derived financial indi-
cators that describe the liquidity and financial performance of the business across different dates.

The datasets is composed of a set of financial variables that collectively describe the cash flow
dynamics of a construction company over time. These variables include both planned and actual
financial movements, as well as derived indicators useful for temporal and predictive analysis. Specifi-
cally, expectedinflow and expectedoutflow represent the forecasted cash inflows and outflows for
each period, while actualinflow and actualoutflow reflect the real amounts received and spent.
The variables openingcash and closingcash indicate the liquidity available at the beginning and
end of each period, providing insight into short-term financial stability.

Furthermore, netcashflow represents the difference between actual inflows and outflows, serving
as a core indicator of operational performance. The inclusion of netcashflowlag1 introduces a tem-
poral dependency by capturing the previous period’s net cash flow, which is essential for time-series
modeling and regression analysis. The rolling indicators, rollingnet 7 and rollingoutflow 30 ,
represent moving averages over 7 days and 30 days, allowing the identification of short-term and
medium-term financial trends. Together, these variables offer a comprehensive and structured view of
liquidity management, operational efficiency, and the financial behavior of the company over time.

In addition to the core cash flow variables, the dataset also includes several accounting and financial
performance indicators that expand the analytical scope of the study. These include accountsreceivable
and accountspayable, representing the company’s outstanding credits from clients and short-term
obligations toward suppliers respectively. The variable cogs (Cost of Goods Sold) reflects the direct
operational costs associated with construction activities, while currentliabilities indicate the
company’s short-term financial commitments.

Furthermore, three financial efficiency ratios were introduced: dayssalesuncollected, which
measures the average time required to collect receivables; dayspayablesoutstanding, indicating


the average payment period to suppliers; and ocfratio, which reflects the company’s ability to gen-
erate operating cash flow relative to its obligations. These indicators allow for a more comprehensive
assessment of liquidity efficiency, operational performance, and short-term financial sustainability.

From an analytical standpoint, this dataset convey how much money moves in and out of a con-
struction business over time, the stability or volatility of cash flow patterns, the trends in cumulative
financial performance and the seasonal or quarterly financial behaviors. Through date-based financial
tracking, it allows users to monitor financial performance longitudinally, identify periods of financial
growth or decline and understand liquidity health and risk exposure periods.

### 4.2 Data Preprocessing

The preprocessing phase played a crucial role in converting the data into structured and analyz-
able information. The key steps included, first, data exploration, where we examined the dataset’s
dimensions and its first few rows to understand its structure. We also used .describe() and .info()
(Figure 1) to analyze statistical distributions and data types. Additionally, we identified the roles of
each column and distinguished between numerical and categorical data.

```
Figure 1: Dataset’s Information
```
After visualizing the data types, we proceeded with the data optimization, converting the float
columns into more memory-efficient formats, that is float32. This allowed us to reduce overall mem-
ory footprint without losing precision, to make more efficient the linear regression in the successive
phase.

The same optimization approach was applied to the date column, which was converted into a date-
time format using pd.to datetime(). This transformation allows the variable to be correctly interpreted
as a time-series feature while also contributing to more efficient memory usage and enabling robust
temporal analysis.


Additionally, the project ID column was converted into a categorical data type. This conversion en-
hances memory efficiency and provides a structured representation that is particularly suitable for
grouping, filtering, and statistical operations, improving both performance and analytical consistency.

In Figure 2, it is possible to observe how these modifications enabled the optimization of the dataset,
resulting in a 68.69% reduction in memory usage.

```
Figure 2: Dataset’s Memory After Optimization
```
As part of the preprocessing phase, particular attention was given to ensuring the integrity and
reliability of the datasets. A comprehensive check for missing values was performed across all columns
to identify any potential gaps that could negatively affect the accuracy of the analysis. In addition,
the dataset was examined for duplicate entries, with a specific focus on the date column to preserve
the correctness of the time-series structure. There were 39 duplicated values for the column date:
any duplicated records were removed to maintain consistency and avoid distortions in the financial
reporting and subsequent analytical results.

For the final stage of data preprocessing, a feature engineering step was performed to enhance the
analytical value of the dataset. A new meaningful variable, cumulativenetcashflow, was derived
by computing the cumulative sum of the netcashflow over time. This variable provides a clear and
progressive view of the company’s financial evolution, highlighting whether the overall cash position
is improving or deteriorating across the observed period.

By tracking the cumulative financial balance, it becomes easier to identify long-term trends, assess
the sustainability of operations, and evaluate the company’s ability to generate consistent positive cash
flow. This transformation therefore enriches the dataset by shifting the analysis from isolated daily
fluctuations to a broader, more strategic perspective of financial performance over time.

### 4.3 What We Learned From the Dataset

The analysis and preprocessing of the dataset provided a deeper understanding of the financial dy-
namics underlying the construction company’s operations. Several key insights emerged regarding
financial behavior, stability, and temporal trends.

As seen in Figure 3, a significant finding concerns the evolution of financial performance over
time. cumulativenetcashflow proved to be a valuable indicator of the company’s overall finan-
cial sustainability, as it clearly illustrates whether the business is strengthening its financial posi-
tion or facing deterioration. To gain more granular insights, we calculated the quarterly average of
cumulativenetcashflow for each year (2022, 2023, 2024, and 2025) and visualized these averages
using line plots for each year with a common y-axis.


This approach allows for direct comparison of financial performance across years while smoothing
short-term fluctuations, making it easier to identify recurring patterns, seasonal effects, or periods of
financial stress within each year. For comparative clarity, all annual line plots were displayed using a
common y-axis range, allowing for immediate visual assessment of relative cash flow trends across years.

```
Figure 3: Lineplot of the Dataset
```
```
The quarterly analysis revealed distinct temporal patterns:
```
- In 2022, cumulativenetcashflow started strongly negative in Q1 and fluctuated across the
    subsequent quarters, indicating initial financial strain followed by partial recovery.
- In 2023, the trajectory showed a progressive decline in the first three quarters, with slight recovery
    in Q4, highlighting periods of operational inefficiency or delayed inflows.
- In 2024, larger fluctuations occurred, with some quarters showing significant negative cash flow,
    suggesting irregular project expenditures or increased operational costs.
- In 2025, a notable positive spike in Q2 contrasted with negative values in Q1, Q3, and Q4,
    indicating a highly variable financial year with both opportunities and risks.

Tracking the trajectory of this cumulative metric allowed us to identify long-term growth patterns
and periods of financial strain, revealing moments when operational efficiency improved or weakened.
These trends provide a strategic perspective on the company’s ability to maintain positive cash flow
and ensure financial continuity.

The temporal structure of the data confirmed the presence of seasonal and quarterly variations
in cash flow. Certain periods consistently showed increased inflows or higher outflows, reflecting the
impact of seasonal demand, project schedules, or broader market conditions. This underscores the
importance of time-aware financial planning and forecasting.

Finally, the dataset offered insights into business stability. Periods of consistently positive netcashflow
suggest sound financial management and strong operational performance, while volatile trends high-
light potential operational inefficiencies or financial risk exposure. Such patterns can serve as early
warning signals, guiding closer monitoring and strategic intervention.

Overall, the dataset offers valuable insights into the company’s liquidity position, project profitabil-
ity trends, and the timing of financial risks. It provides a comprehensive financial portrait of business
operations, enabling the identification of strengths, vulnerabilities, and opportunities for improved
financial control and strategic planning.

### 4.4 How This Information Can Be Used

The processed dataset provides valuable insights that can be applied across multiple aspects of
business management and financial planning. By leveraging the information it contains, the companies
can make more informed, strategic decisions.


- Financial Forecasting: The historical financial data can be used to anticipate future cash
    flow behavior, helping management predict potential trends and fluctuations. This predictive
    capacity supports more accurate budgeting and financial planning, ensuring that resources are
    allocated efficiently and that the company is prepared for upcoming financial demands.
- Strategic Business Decisions: Understanding the temporal patterns of cash flow enables the
    identification of optimal periods for project investments and expansion. By recognizing periods
    of high financial stress or volatility, management can make strategic choices that minimize risk
    and maximize returns, aligning operational decisions with the company’s financial capacity.
- Risk Management: The dataset serves as a critical tool for risk management by highlighting
    potential cash shortages or periods of negative cash flow trends. Armed with this information,
    the company can proactively plan contingency funds or adjust operational strategies to mitigate
    financial risk, reducing the likelihood of unexpected liquidity issues.
- Performance Monitoring: Regular monitoring of the financial data allows management to
    track operational efficiency over time. By comparing actual performance against historical trends,
    the company can identify areas for improvement, evaluate the effectiveness of strategic initiatives,
    and ensure that financial goals are being met.
- Data-Driven Reporting: Finally, the dataset is an invaluable resource for creating dashboards
    and reporting to stakeholders. It supports automated financial analytics systems, allowing for
    real-time insights and clear communication of the company’s financial status. This ensures trans-
    parency, facilitates data-driven decision-making, and strengthens confidence among investors and
    other stakeholders.

## 5 Predictive Liquidity Modeling

This section outlines the validation phase of the cash flow forecasting system. Addressing the ”Cash
Flow Crystal Ball” challenge, the primary objective was to transition from reactive manual estimation
to a proactive, AI-driven liquidity model.

Given the high volatility of daily transactions in the construction sector, predicting raw ”Net Cash
Flow” often leads to statistical noise. Therefore, to effectively address the liquidity issues highlighted
in the problem statement, the model is designed to forecast the Daily Closing Cash Balance. This
metric integrates daily flows with the accumulated stock, providing a direct and actionable measure
of the firm’s Liquidity Position.

```
Specifically, this study aims to:
```
1. Link Prediction to Liquidity: Forecast the daily evolution of the bank balance to detect
    potential shortfalls before they occur.
2. Integrate Accounting Focus: Utilize efficiency ratios (DSU, DPO, OCF) as leading indicators,
    as mandated by the project scope.
3. Ensure Scientific Integrity: Eliminate ”look-ahead bias” (data leakage) by strictly strictly
    using historical data (t− 1) to predict future states (t).

## 6 Data Methodology and Preprocessing

Reliable forecasting requires a rigorous data pipeline capable of distinguishing between abstract
accrual-based metrics and concrete cash movements. To achieve this, the analysis adopts a specific
modeling strategy designed to stabilize predictions and ensure operational realism.

A critical methodological shift was the redefinition of the target variable. Unlike traditional models
that attempt to predict the exact magnitude of specific daily invoices (Net Flow)—which are inherently
volatile and noisy—our model is trained to predict the Closing Cash Balance. Defined as:


```
Closing Balancet= Opening Balancet+ Net Cash Flowt
```
This approach aligns directly with the business need to monitor overall solvency rather than just
transactional volume, providing a more stable and actionable signal for treasury management.

To validate this approach in a simulated real-world environment, a strict Time-Lag Strategy was
enforced to prevent data leakage. All efficiency ratios, stress indices, and operational metrics used
as input features are strictly calculated based on data available at t− 1 (the previous day). This
constraint ensures that the model does not ”cheat” by accessing current-day information that would
be unavailable at the moment of the forecast, thereby guaranteeing the scientific integrity of the
predictions.

## 7 Predictive Application of Accounting Indicators

Building on the definitions provided in Section 3.5, the modeling strategy transforms these static ac-
counting ratios into dynamic Leading Indicators. In strict compliance with the project’s ”Accounting
Focus,” these metrics are ingested as lagged features (t− 1), allowing the model to anticipate liquidity
shifts based on operational efficiency trends rather than relying solely on historical transaction volume.

DSU as a Latency Signal. The model utilizes the Days Sales Uncollected (DSU) to gauge
the velocity of inbound cash. From a predictive standpoint, the algorithm interprets an increasing
trend in lagged DSU not merely as a statistic, but as a specific risk of collection deceleration. This
prompts a downward correction in the forecasted liquidity curve, effectively ”pricing in” the probability
of delayed inflows before they impact the balance.

DPO as a Liquidity Lever. Conversely, Days Payables Outstanding (DPO) is analyzed as
a strategic variable for cash retention. The model learns the correlation between payment deferral
strategies and short-term solvency: a rising DPO is interpreted as a preservation of working capital,
temporarily bolstering the closing balance, while a sharp drop serves as an early warning signal for a
cash-intensive settlement phase.

OCF as a Solvency Barometer. Finally, the Operating Cash Flow Ratio serves as the primary
benchmark for self-funding capability. By monitoring the previous day’s OCF, the model weights
the probability of a liquidity crunch. A ratio consistently below the equilibrium threshold warns the
system that current liabilities are outpacing organic cash generation, triggering a conservative forecast
to reflect heightened financial stress.

## 8 Experimental Results and Visual Diagnostics

The model was validated using a chronological hold-out strategy (70% Train / 30% Test). The results
demonstrate that the system effectively learned the ”physics” of construction liquidity.

### 8.1 Feature Importance and Model Logic

```
The Feature Importance analysis (Figure 4) confirms the validity of the approach.
```

```
Figure 4: Feature Importance: model identifies Opening Cash and WCC as primary drivers
```
The analysis reveals that the top predictors are Opening Cash (the stock) followed by Working
Capital Cycle and DPO (the efficiency). This proves the model is not relying on spurious correlations
but is driven by the fundamental accounting mechanics required by the project scope.

### 8.2 Forecast Accuracy and Risk Profile

```
The forecasting performance varies by project type, offering distinct insights for risk management.
```
```
Figure 5: Liquidity Forecasting: Project C shows a strong predictive fit (R^2 > 0 .50)
```
- Structural Alignment (Project C): For projects with structural volatility, the model achieves
    an R^2 > 0 .50. As seen in Figure 5 (Project C), the predicted trend (orange) follows the actual
    liquidity curve (blue) closely, capturing both the Q1 dip and the Q2 recovery. This serves as a
    successful Proof of Concept.
- Conservative Bias (Project A/B): In highly volatile scenarios (Project A), the model adopts
    a conservative approach, often under-forecasting extreme liquidity peaks. From a risk manage-
    ment perspective, this is a desirable trait, as it prevents the overestimation of available funds.

### 8.3 Residual Analysis

The residual analysis (Figure 6) shows errors are centered, confirming the absence of systematic bias.
The model provides a reliable ”baseline” for liquidity planning.


```
Figure 6: Residual Analysis: Errors are centered around zero, validating the statistical robustness
```
### 8.4 Conclusion

The validation phase confirms that the Closing Balance Predictive Model is a viable tool for con-
struction cash management. By shifting the target from volatile daily flows to Liquidity Stock, and by
strictly integrating the required Accounting Focus metrics (DSU, DPO) as lagged predictors, we have
built a system that is:

1. Scientifically Defensible: Free from data leakage.
2. Business Aligned: Directly answers the ”Liquidity Issue” problem statement.
3. Risk Averse: Provides conservative estimates suitable for treasury planning.

## 9 Full Predictive Liquidity Pipeline

This section presents the end-to-end liquidity pipeline developed to predict the Daily Closing Cash
Balance, the primary indicator of short-term solvency in construction projects. Unlike raw Net Cash
Flow, which is highly volatile and operationally noisy, Closing Cash Balance captures the firm’s true
liquidity position by integrating daily inflows, outflows, and opening cash balances.

### 9.1 Overview and Rationale

The pipeline was redesigned to align the analytics with actual liquidity decision-making. Earlier
models focused on predicting Net Cash Flow, a metric that fluctuates heavily day-to-day and provides
limited value. From a financial management perspective, firms do not make liquidity decisions based
on isolated daily movements. Instead, they manage based on the Closing Cash Balance:

```
Closing Balancet= Opening Balancet+ Net Cash Flowt
```
The redesign also introduces accounting-driven leading indicators, such as DSU, DPO, OCF ra-
tio, integrated as lagged inputs. These indicators capture payment behavior, collection delays, and
operational cash-generation capacity.

### 9.2 Global Feature Engineering Architecture

To ensure financially credible predictions, the pipeline applies a structured feature-engineering frame-
work that mirrors real liquidity behavior. Each project is processed chronologically to maintain the
natural order of cash events, and all variables are transformed into t-1 lagged indicators to avoid any
forward-looking bias.

The accounting-driven predictors include DSUt− 1 , DP Ot− 1 , OCFt− 1 , and the W CCt− 1 , giving
the model visibility into delays, behavior, and solvency. Short-term patterns are captured through
rolling metrics such as 7-day net cash momentum and 30-day outflow smoothing, while net cash flow


lag-1 provides a direct momentum signal.

Calendar factors (day of month, day of week, month-end markers, and cumulative project time)
show predictable operational rhythms such as billing cycles and supplier settlement patterns.

### 9.3 Project-Level Data Preparation

To ensure reliable forecasting, each project (A, B, C) is processed independently. This mirrors real
construction operations, where liquidity dynamics differ by project size, payment terms, and execu-
tion pace. Data is chronologically ordered and cleaned to remove early rows where lagged ratios are
unavailable, preventing distortion of efficiency-driven signals. A minimum sequence length is enforced
to guarantee model stability (projects with insufficient usable history are excluded from modeling win-
dows). As seen in Table 4, the usable data points per project varied.

```
Table 4: Usable Data After Project-Level Cleaning
Project Usable Data Per Project
Project A 177
Project B 66
Project C 122
```
### 9.4 Model Benchmarking via Time-Series Cross-Validation

To evaluate forecasting robustness under real operational conditions, all models were benchmarked
using a 5-fold TimeSeriesSplit, which preserves chronological order and prevents forward-looking bias.
Three baseline algorithms were tested: Linear Regression, Random Forest, and Gradient Boosting.
Performance was assessed on R², RMSE, and MAE.

Across individual projects, Random Forest delivers the strongest performance on Project A, reflect-
ing its ability to capture nonlinear liquidity patterns. However, when averaging results across all project
environments, the Stacking Ensemble (Top-3) achieves the most stable and consistent performance,
making it the preferred model for enterprise-level deployment. A summary of the cross-validation
results is reported in Figure 7.

```
Figure 7: R^2 per project for each model
```
### 9.5 Ensemble Modeling: Voting and Stacking

To enhance predictive stability, the top-performing hyperparameter configurations from the Grid
Search were extracted and used to build two ensemble architectures.


Results show that the Voting Ensemble performs similarly to Random Forest, offering a balanced
but not significantly improved forecast. The Stacking Ensemble, despite weaker performance on some
individual projects, delivers the best overall cross-project average (–0.416 R^2 ). This indicates stronger
generalization and makes it the preferred model for multi-project liquidity environments.

### 9.6 Cross-Project Evaluation

Each project was evaluated independently by rebuilding the tuned models and applying a dedicated
TimeSeriesSplit. Their results were then consolidated into a single comparison table to assess model
robustness across heterogeneous liquidity profiles.

```
Figure 8: Heat map demonstrating R^2 across models
```
The analysis reveals clear differences in predictability and the heatmap for the R^2 values can be
seen in Figure 8:

- Project A shows mild but usable forecastability, reflecting moderately structured liquidity pat-
    terns.
- Project B exhibits high volatility and noise, resulting in consistently negative R^2 scores across
    all models.
- Project C behaves most predictably, with smoother cash dynamics and the strongest model
    performance overall.

When averaged across projects, the Stacking Ensemble emerges as the enterprise-level best model,
delivering the most consistent performance despite intra-project variability.

### 9.7 Multi-Horizon Forecasting (1, 7, 30 Days)

To extend liquidity visibility beyond the immediate day, a custom forecasting module was developed
to predict future net cash flow over three horizons: 1-day, 7-day, and 30-day, as seen in Figure 9.

These horizon-specific forecasts translate directly into short-term liquidity risk signals, enabling
treasury teams to anticipate cash shortages or surpluses and adjust funding, payment scheduling, or
supplier negotiations accordingly.


```
Figure 9: Predictions Across Horizons
```
### 9.8 Scenario Analysis Using Accounting Ratios (DSU, DPO, OCF)

The system trains on each project’s full historical data (closing cash target) and applies shocks to
the last observable state:

1. DSU increase (customer payment delays)
2. DPO increase(supplier payment extensions)
3. OCF ratio (revenue or COGS shocks)

```
Figure 10: Scenario Analysis
```
For each scenario, the model recomputes the predicted closing cash balance and reports the ∆ vs.
the base case, allowing management to assess liquidity sensitivity, illustrated in Figure 10.

```
Key insights:
```
- Project A behaves like a Saipem-type EPC project—highly exposed to DSU +10 days (client
    delay risk).
- Project B shows stronger sensitivity to OCF (revenue/COGS) shocks, consistent with thinner
    margins.


- Project C is comparatively stable, mirroring a service-type profile with smoother cash dynamics.

### 9.9 Backtesting: Actual vs Predicted Liquidity

The model’s reliability was validated through a strict chronological backtest using TimeSeriesSplit,
ensuring that each forecast is made only with historically available information.

For every fold, the system compares the predicted closing cash balance against the true observed
values, producing both line plots and residual diagnostics, as seen in Figure 11.

```
Figure 11: Backtesting: Actual Versus Predicted
```
```
These show that:
```
1. The model accurately follows the liquidity trend, capturing major rises and declines in cash
    position.
2. In highly volatile phases, the system exhibits a conservative bias, which is desirable for treasury
    risk management.
3. Residuals remain centered around zero, confirming no systematic over- or under-estimation and
    validating model stability.


### 9.10 Permutation Feature Importance (PFI)

To validate whether the model relies on meaningful financial drivers, a Permutation Feature Impor-
tance (PFI) analysis was performed. PFI measures how much forecasting accuracy deteriorates when
each feature is randomly shuffled, making it a robust indicator of true explanatory power. Figure 4
shown in the earlier section illustrates this.

```
The results clearly align with financial intuition:
```
- Opening Cash emerges as the primary determinant of future liquidity—confirming the model
    anchors to the existing cash stock.
- Working Capital Cycle components rank next, reflecting how client collection delays and supplier
    payment timing shape solvency.
- Momentum indicators such as netCashF lowLag1 and rolling 7-/30-day aggregates also show
    strong importance, capturing short-term liquidity inertia.

```
This confirms that the model is not exploiting random patterns but follows core accounting logic.
```
### 9.11 Working Capital Visual Analytics

To complement the modeling results, a set of working-capital visuals was developed to help interpret
liquidity risk at a managerial level. The dashboards focus on the operational levers that drive cash
stability:

- DSU / DPO / OCF time-series trends track how collection speed, payment timing, and operating
    cash efficiency evolve over the project lifecycle.
- Net Cash Flow with forecast markers highlights how short-term liquidity swings align with model
    predictions.
- Working Capital Cycle (CCC = DSU + DPO) shows the duration for which cash is tied up in
    operations.
- CCC vs. Net Cash Flow Volatility visualizes the link between operational inefficiency and liq-
    uidity instability.

```
From the provided visuals, we interpret the following:
```
1. DSU / DPO / OCF Time-Series Trends: as seen in Figure 12, DSU (collection speed)
    falls steadily across all projects, signaling improving receivable management. DPO (supplier
    payment timing) converges to stable levels. Projects with rising DPO (such as Project A) show
    improved short-term liquidity. As for OCF ratio, it stays near zero for most projects, indicating
    thin liquidity buffers, meaning minor deteriorations often precede cash-flow dips.
2. Net Cash Flow with Forecast Markers: From Figure 13, all projects exhibit high day-to-day
    cash-flow noise, confirming that raw net CF is not a stable forecasting target. Forecast markers
    generally align with local trends but intentionally avoid predicting extreme spikes—reflecting
    the model’s risk-averse stance. Longer (30-days) smooth out noise and better capture structural
    liquidity direction.
3. Cash Conversion Cycle (CCC = DSU + DPO): Lastly, as in Figure 14, Project B starts
    with extremely high CCC, explaining its persistent negative R^2 and unstable liquidity behavior.
    All projects converge toward lower CCC over time, showing efficiency gains in the synthetic
    scenario. Temporary CCC increases, such as in Project A, align with higher volatility episodes.
    So, CCC is a reliable structural indicator of liquidity stress. Higher CCC corresponds to weaker
    predictability and tighter cash conditions.


```
Figure 12: Time-Series Trends
```
### 9.12 Summary: Operational Value of Pipeline

The redesigned pipeline delivers a robust and actionable framework for construction cash-flow man-
agement. By enforcing strict time-lag rules, the system ensures leakage-free forecasting, preserving
real-world decision integrity.

Through the integration of daily accounting ratios (DSU, DPO, OCF, WCC), the model captures
the operational mechanics that drive short-term liquidity, aligning the analytics with treasury and
working-capital realities.

The pipeline produces multi-horizon forecasts, scenario-based stress tests, and risk-adjusted liquid-
ity predictions, enabling mitigation of emerging cash shortfalls. Finally, the visual dashboard translates
technical outputs into CFO-ready insights, clarifying the impact of operational efficiency on solvency
and empowering faster financial decisions.


Figure 13: Net Cash Flow & Forecast Markers


Figure 14: Cash Conversion Cycle


## 10 Conclusion and Managerial Implications

This project set out to address one of the most persistent challenges in the construction and EPC sec-
tor: the difficulty of forecasting liquidity in an environment defined by milestone-based billing, volatile
working capital and long project cycles. Our analysis of Saipem, Fluor and AECOM highlighted how
different business models shape liquidity risk, and why Saipem (having undergone a clear turnaround
driven by stronger working-capital discipline) was an ideal reference case for the development of a
predictive framework.

To support this, we constructed a synthetic dataset grounded in real accounting mechanics rather
than random numbers. The data-generation approach captured the essential drivers of liquidity: ac-
crual vs. cash timing, receivables, payables, current liabilities, and key ratios such as DSU, DPO,
OCF and the Working Capital Cycle, together with time-lagged and rolling indicators. After rigor-
ous preprocessing, the dataset provided a reliable foundation for modelling realistic cash-flow dynamics.

Building on this, we redesigned the forecasting pipeline around the closing cash balance, a more
stable and decision-relevant target than daily net flows. Using strict lagging to avoid data leakage and
time-series cross-validation, we evaluated multiple algorithms. Ensemble models, particularly stack-
ing, delivered consistently strong results, while feature-importance and residual analyses confirmed
that the model relied on meaningful financial drivers rather than noise. Scenario testing and multi-
horizon forecasts (1, 7 and 30 days) further demonstrated the system’s ability to anticipate liquidity
changes under delays in collections, shifts in supplier terms or fluctuations in operating performance.

From a managerial standpoint, the framework turns accounting ratios into actionable foresight.
Finance teams can identify upcoming liquidity gaps, optimise short-term funding, and deploy surplus
cash more effectively. Operational teams can quantify the impact of DSU, DPO and OCF changes,
negotiate payment terms with a clear understanding of liquidity consequences, and set project-specific
cash buffers based on actual volatility rather than static policy.

Ultimately, this project shows that by combining rigorous accounting logic, synthetic but realistic
data and modern machine-learning methods, construction firms can transition from reactive cash
management to predictive, strategically guided liquidity control. While future work may extend the
model to portfolio-level optimisation or real-time dashboards, the current system already provides a
practical blueprint for strengthening solvency, improving decision-making and gaining a competitive
edge in one of the most financially fragile industries.


## Bibliography

[1] Statista Research Department. “Construction industry in the U.S.” In: (2025).

[2] Guardian. “Carillion: what went wrong and where does it go from here?” In: (2018).

[3] Tim Stobierski. “How to Read Understand a Cash Flow Statement”. In: (2020).

[4] Marsh. “How Construction Companies Can Manage Their Liquidity Challenges”. In: (2020).

[5] PwC. “PwC Construction and Housebuilding Outlook”. In: (2020).

[6] Forough Farhadi. “Cash Flow in Construction; Comprehensive Guide”. In: (2024).

[7] J.P.Morgan. “Improve your cash flow with DSO and DPO”. In: (2025).

[8] J.P.Morgan. “Your cash conversion cycle—what it is and how to optimize it”. In: (2025).

[9] Corporate Finance Institute. “Operating Cash Flow”. In: (2025).

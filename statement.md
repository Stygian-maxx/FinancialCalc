# Project Statement: Personal Finance Toolkit

> **Course Evaluation Project**: VITyarthi — Build Your Own Project  
> **Document Type**: `statement.md`  

---

## 1. Problem Statement

In today's complex economic landscape, individuals, college students, and retail investors often struggle with financial decision-making due to fragmented, over-complicated, or subscription-gated financial tools. Key challenges include:

1. **Lack of Consolidated Evaluation**: Users must switch between disparate online calculators to estimate simple interest, stock trading fees, insurance needs, mutual fund growth, loan EMIs, and monthly budget safety.
2. **Hidden Trading & Transaction Costs**: Retail equity traders frequently overlook multi-tier statutory charges (STT, GST, Exchange turnover fees, SEBI charges, Stamp Duty) when calculating intraday stock profitability, leading to unexpected trading losses.
3. **Inadequate Emergency Planning & Debt Overhang**: Many young professionals lack a structured mechanism to diagnose their Debt-to-Income (DTI) ratio or determine a tailored emergency fund target based on living expenses.
4. **Tool Access & Privacy Concerns**: Many existing tools require internet connectivity, cloud accounts, or personal financial data sharing.

The **Personal Finance Toolkit** solves these problems by providing an offline, lightweight, unified command-line application that performs transparent financial math, estimates transaction friction, and offers actionable budget diagnostics.

---

## 2. Project Scope

### In-Scope Capabilities
- **Mathematical Estimation Engines**:
  - Simple vs. Compound Interest accural modeling.
  - Full intraday stock trade PnL calculations featuring 6 statutory tax and exchange fee layers.
  - Human life value (income replacement) and health insurance deficit planning.
  - Wealth accumulation projections for lump-sum investments and monthly compounding SIPs.
  - Monthly EMI amortization schedule modeling for housing and personal loans.
- **Financial Advisory Diagnostic**:
  - Automated budget review generating surplus analysis, DTI risk assessment (>36% threshold warning), and 6-month emergency reserve targets.
- **Robust System Operations**:
  - Terminal-based interactive user navigation menu.
  - Comprehensive input validation rejecting invalid strings, negative numbers, non-integer counts, and mathematical infinities.
  - Automated unit testing suite covering functional correctness and boundary exceptions.

### Out-of-Scope Capabilities
- Direct integrations with banking APIs or live stock exchange feeds.
- Persistent database storage (all calculations run locally in memory per session).
- Graphical User Interface (GUI) desktop or web deployment.
- Formal tax filing preparation or regulated financial advice.

---

## 3. Target User Base

1. **College Students & Young Professionals**: Individuals seeking an easy, offline utility to manage monthly budgets, plan emergency savings, and project wealth growth through SIPs.
2. **Retail Equity Traders**: Active traders needing quick, accurate estimates of net trading profits after deducting multi-tier regulatory and brokerage fees.
3. **Prospective Loan Borrowers**: Home and personal loan applicants comparing interest rates, monthly EMI obligations, and total interest expenses before borrowing.
4. **Financial Literacy Educators & Students**: Academic users studying financial algorithms, time-value-of-money concepts, and software validation patterns.

---

## 4. High-Level System Features

| Feature Module | Key Responsibilities & Capabilities |
| :--- | :--- |
| **`Fincalc`** | Computes accrued interest and total balances using Simple and Compound Interest formulas. |
| **`Brokeragecalc`** | Computes turnover, gross PnL, itemized charges (Brokerage, STT, Exchange fee, Stamp Duty, SEBI fee, GST), and net PnL. |
| **`Insurancecalc`** | Determines life insurance cover gap based on income replacement and liabilities, and family health cover deficit. |
| **`MutualFundcalc`** | Calculates compound investment growth over $N$ years for lump sum contributions. |
| **`SIPcalc`** | Models monthly compounding SIP investments over short or long-term horizons. |
| **`Loancalc`** | Calculates monthly EMIs, total interest paid, and total cost of borrowing for personal and housing loans. |
| **`FinAssistant`** | Analyzes monthly cash flows, computes DTI percentage, recommends emergency targets, and outputs financial health suggestions. |
| **`validators`** | Validates numeric inputs, handles range checks, enforces positive whole numbers, and raises standardized errors. |
| **`FinanceApp`** | Provides interactive terminal prompts, formats key-value output dictionaries, handles menu loops, and catches runtime errors. |
| **`calcTests`** | Executes automated unit test verification across mathematical formulas, boundary inputs, and invalid input scenarios. |

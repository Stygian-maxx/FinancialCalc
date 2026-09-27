# Personal Finance Toolkit

> A modular, command-line personal finance and investment modeling suite built in Python for the **VITyarthi — Build Your Own Project** framework.

---

## 📌 Project Overview

The **Personal Finance Toolkit** is an interactive, lightweight software application designed to help individuals, retail traders, and students model key financial decisions. It consolidates financial algorithms—including interest estimations, multi-tier stock trading fee breakdowns, insurance adequacy planning, mutual fund and SIP wealth projections, loan EMI calculations, and automated budget diagnostics—into a unified, menu-driven CLI application.

Built with robust input validation and an automated unit testing suite, the application ensures data integrity, prevents runtime crashes from bad user input, and adheres strictly to software engineering best practices.

---

## ✨ Key Features

The project is structured into **8 core functional modules** accessible via an interactive terminal menu:

1. **Interest Calculator (`Fincalc`)**
   - Supports both **Simple Interest** ($I = P \times r \times t$) and **Compound Interest** ($A = P(1 + r)^t - P$).
   - Returns principal, total interest earned, and final accrued amount.

2. **Intraday Brokerage & Statutory Charge Estimator (`Brokeragecalc`)**
   - Calculates gross profit/loss and itemized transaction costs for intraday stock trades.
   - Factors in 6 distinct statutory charges: Brokerage per order, Securities Transaction Tax (STT), Exchange Turnover Charges, Stamp Duty, SEBI turnover fees, and Goods & Services Tax (GST on brokerage + exchange + SEBI fees).
   - Computes net profit/loss after deducting total charges from turnover.

3. **Life & Health Insurance Cover Planner (`Insurancecalc`)**
   - **Life Cover**: Evaluates required life insurance based on annual income, income replacement period (years), outstanding liabilities, and existing assets.
   - **Health Cover**: Determines family health insurance deficit based on total members, desired cover per person, and current insurance coverage.

4. **Mutual Fund Lump Sum Projection (`MutualFundcalc`)**
   - Projects total future wealth accrued from a lump sum investment using compound annual growth rate formulas over $N$ years.

5. **Systematic Investment Plan (SIP) Simulator (`SIPcalc`)**
   - Simulates monthly compounding SIP growth: $A = M \times \frac{(1 + r)^n - 1}{r}$.
   - Handles edge cases such as zero annual return (calculating pure principal accumulation).

6. **Loan EMI & Interest Amortization Calculator (`Loancalc`)**
   - Computes fixed Equated Monthly Installments (EMI) for **Housing Loans** and **Personal Loans** using the standard amortization formula: $E = P \cdot r \cdot \frac{(1+r)^n}{(1+r)^n - 1}$.
   - Output includes monthly payment, total interest payable over the term, and total repayment amount.

7. **Financial Assistant & Budget Review (`FinAssistant`)**
   - Performs automated budget diagnostics based on monthly take-home income, living expenses, and debt obligations.
   - Calculates **Monthly Surplus**, **Debt-to-Income (DTI) Ratio** (flagging DTI > 36% as high risk), and **Emergency Fund Target** (defaulting to 6 months of expenses).

8. **Automated Input Validation & Exception Chaining (`validators`)**
   - Enforces strict numeric type checking, non-negative range constraints, and positive integer validation for quantities and loan terms.
   - Uses Python exception chaining (`raise ValueError(...) from exc`) to provide clean, readable feedback without program crashes.

9. **Automated Unit Test Suite (`calcTests`)**
   - Integrated unit testing using Python's `unittest` library to verify mathematical accuracy, edge cases, and exception handling.

---

## 📁 Repository Directory Structure

To meet academic guidelines for modular software architecture, the repository is organized into distinct packages and files:

```text
personal_finance_toolkit/
│
├── finance_toolkit/            # Core Package Directory
│   ├── __init__.py             # Package marker
│   ├── validators.py           # Input validation logic (number, positive_int)
│   ├── calculators.py          # Math engines (Fincalc, Brokeragecalc, Insurancecalc, MutualFundcalc, SIPcalc, Loancalc)
│   ├── assistant.py            # Budget diagnostic engine (FinAssistant)
│   └── cli.py                  # Menu-driven User Interface (FinanceApp)
│
├── tests/                      # Automated Test Suite Package
│   ├── __init__.py             # Test package marker
│   └── test_calculators.py     # Unit test cases (calcTests)
│
├── main.py                     # Entry point script
├── README.md                   # Repository overview & setup guide
└── statement.md                # Problem statement & project scope document
```

---

## 🛠️ Technologies & Tools Used

- **Programming Language**: Python 3.10+
- **Built-in Libraries**: `math` (financial powers & numbers), `sys` (CLI argument parsing), `unittest` (automated testing framework)
- **Design Pattern**: Object-Oriented Architecture with static utility methods and menu dispatch maps
- **Version Control**: Git / GitHub

---

## 🚀 Setup & Installation Guide

### Prerequisites
- Python 3.8 or higher installed on your system. Verify installation with:
  ```bash
  python --version
  ```

### Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/personal-finance-toolkit.git
   cd personal-finance-toolkit
   ```

2. **Run the Application**:
   Execute `main.py` directly from the project root:
   ```bash
   python main.py
   ```

---

## 💡 How to Use (Interactive CLI)

Upon running `python main.py`, the application displays the interactive main menu:

```text
Personal Finance Toolkit — estimates only, not financial advice.

1. Interest calculator
2. Intraday brokerage
3. Life or health cover
4. Mutual fund (lump sum)
5. SIP
6. Housing loan
7. Personal loan
8. Fin assistant
0. Exit

Select a section:
```

### Usage Example: Housing Loan EMI Calculation
- Enter `6` at the menu prompt.
- Enter Loan Principal: `2500000`
- Enter Annual Interest Rate (%): `8.5`
- Enter Term in Months: `240`

**Output:**
```text
Housing Loan Estimate
Monthly Payment: 21,695.57
Total Paid: 5,206,936.80
Total Interest: 2,706,936.80
```

---

## 🧪 Testing Instructions

The repository includes a comprehensive unit testing suite (`calcTests`) testing mathematical calculations, boundary conditions, and exception handling.

### Run Automated Unit Tests
To execute all test cases via CLI flag:
```bash
python main.py --test
```

Or using standard Python `unittest`:
```bash
python -m unittest discover -s tests
```

### Expected Test Results:
```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

---

## 📸 Sample Terminal Screenshots / Output

### Financial Assistant Budget Review Output
```text
Budget Review
Monthly Surplus: 25,000.00
Debt To Income Percent: 20.00
Emergency Fund Target: 180,000.00
Suggestions:
- Estimated monthly surplus: 25,000.00.
- Keep monitoring debt payments against income.
- Emergency fund target: 180,000.00.
```

---

## 📜 License & Disclaimer

This software is developed strictly for educational purposes as part of the **VITyarthi — Build Your Own Project** evaluation. Results generated by the tool are estimates and do not constitute formal financial advice.

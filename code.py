import math
import sys
import unittest
from unittest import mock


def number(value, name, minimum=0):


    try:
        value = float(value)

    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a number.") from exc

    if not math.isfinite(value) or value < minimum:
        raise ValueError(f"{name} must be at least {minimum}.")

    return value


def positive_int(value, name):


    try:
        result = int(value)

        if str(value).strip() != str(result):
            raise ValueError
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a positive whole number.") from exc
    if result <= 0:
        raise ValueError(f"{name} must be a positive whole number.")
    return result


class Fincalc:



    @staticmethod
    def calculate(principal, annual_rate, years, method="compound"):
        principal = number(principal, "Principal")
        rate = number(annual_rate, "Annual rate") / 100
        years = number(years, "Years")

        method = method.lower()
        if method == "simple":
            interest = principal * rate * years
        elif method == "compound":
            interest = principal * ((1 + rate) ** years - 1)
        else:
            raise ValueError("Choose simple or compound interest.")

        return {"principal": principal, "interest": interest, "total": principal + interest}


class Brokeragecalc:



    @staticmethod
    def calculate(buy_price, sell_price, quantity, brokerage, stt, exchange, gst, stamp, sebi):
        quantity = positive_int(quantity, "Quantity")
        buy = number(buy_price, "Buy price") * quantity
        sell = number(sell_price, "Sell price") * quantity
        turnover = buy + sell

        brokerage = 2 * number(brokerage, "Brokerage per order")
        exchange_fee = turnover * number(exchange, "Exchange rate") / 100
        stt_fee = sell * number(stt, "STT rate") / 100
        stamp_fee = buy * number(stamp, "Stamp duty rate") / 100
        sebi_fee = turnover * number(sebi, "SEBI fee per crore") / 10_000_000
        gst_fee = (brokerage + exchange_fee + sebi_fee) * number(gst, "GST rate") / 100

        charges = brokerage + exchange_fee + stt_fee + stamp_fee + sebi_fee + gst_fee
        pnl = sell - buy

        return {
            "buy_turnover": buy,
            "sell_turnover": sell,
            "gross_pnl": pnl,
            "brokerage": brokerage,
            "exchange_charges": exchange_fee,
            "stt": stt_fee,
            "stamp_duty": stamp_fee,
            "sebi_charges": sebi_fee,
            "gst": gst_fee,
            "total_charges": charges,
            "net_pnl": pnl - charges,
        }


class Insurancecalc:
    @staticmethod
    def life_cover(annual_income, replacement_years, liabilities, assets):


        need = number(annual_income, "Income") * number(replacement_years, "Years")
        need += number(liabilities, "Liabilities") - number(assets, "Assets")
        return max(0, need)

    @staticmethod
    def health_cover(people, cover_per_person, existing_cover=0):
        total_needed = positive_int(people, "People") * number(cover_per_person, "Cover")
        return max(0, total_needed - number(existing_cover, "Existing cover"))


class MutualFundcalc:



    @staticmethod
    def calculate(investment, annual_return, years):
        invested = number(investment, "Investment")
        rate = number(annual_return, "Annual return") / 100
        value = invested * (1 + rate) ** number(years, "Years")
        return {"invested": invested, "estimated_value": value, "estimated_gain": value - invested}


class SIPcalc:



    @staticmethod
    def calculate(monthly_investment, annual_return, years):


        monthly = number(monthly_investment, "Monthly investment")
        months = int(number(years, "Years") * 12)
        if months < 1:
            raise ValueError("Investment period must be at least one month.")

        rate = number(annual_return, "Annual return") / 1200
        if rate == 0:
            value = monthly * months
        else:
            value = monthly * ((1 + rate) ** months - 1) / rate

        invested = monthly * months
        return {
            "months": months,
            "invested": invested,
            "estimated_value": value,
            "estimated_gain": value - invested,
        }


class Loancalc:



    @staticmethod
    def calculate(principal, annual_rate, months):
        principal = number(principal, "Loan principal")
        months = positive_int(months, "Term in months")
        rate = number(annual_rate, "Annual rate") / 1200

        if rate == 0:
            payment = principal / months
        else:
            payment = principal * rate * (1 + rate) ** months / ((1 + rate) ** months - 1)

        total = payment * months
        return {
            "monthly_payment": payment,
            "total_paid": total,
            "total_interest": total - principal,
        }


class FinAssistant:



    @staticmethod
    def review(income, expenses, debt, emergency_months=6):


        income = number(income, "Monthly income", minimum=0.000001)
        expenses = number(expenses, "Monthly expenses")
        debt = number(debt, "Monthly debt payments")
        months = number(emergency_months, "Emergency-fund months")

        surplus = income - expenses - debt
        target = expenses * months

        tips = []
        if surplus < 0:
            tips.append("Spending and debt exceed income; review your budget.")
        elif surplus == 0:
            tips.append("There is no monthly surplus available for saving.")
        else:
            tips.append(f"Estimated monthly surplus: {surplus:,.2f}.")



        if debt / income > 0.36:
            tips.append("Debt payments are above 36% of income; consider reducing debt.")
        else:
            tips.append("Keep monitoring debt payments against income.")

        tips.append(f"Emergency fund target: {target:,.2f}.")

        return {
            "monthly_surplus": surplus,
            "debt_to_income_percent": debt / income * 100,
            "emergency_fund_target": target,
            "suggestions": tips,
        }


class FinanceApp:



    MENU = (
        "1. Interest calculator",
        "2. Intraday brokerage",
        "3. Life or health cover",
        "4. Mutual fund (lump sum)",
        "5. SIP",
        "6. Housing loan",
        "7. Personal loan",
        "8. Fin assistant",
        "0. Exit",
    )

    @staticmethod
    def ask(prompt):
        return input(prompt).strip()

    @classmethod
    def amount(cls, prompt):
        return number(cls.ask(prompt), prompt.rstrip(": "))

    @classmethod
    def count(cls, prompt):
        return positive_int(cls.ask(prompt), prompt.rstrip(": "))

    @staticmethod
    def show(title, result):
        print(f"\n{title}")
        for key, value in result.items():
            label = key.replace("_", " ").title()
            if key == "suggestions":
                for tip in value:
                    print(f"- {tip}")
            elif isinstance(value, (int, float)):
                print(f"{label}: {value:,.2f}")
            else:
                print(f"{label}: {value}")

    def run_calculation(self, calculator, title, prompts, integer_inputs=()):
        values = [
            self.count(prompt) if index in integer_inputs else self.amount(prompt)
            for index, prompt in enumerate(prompts)
        ]
        operation = getattr(calculator, "calculate", None)
        if operation is None:
            operation = getattr(calculator, "review", None)
        if operation is None:
            raise ValueError(f"{calculator.__name__} has no supported calculation method.")
        self.show(title, operation(*values))

    def interest(self):
        result = Fincalc.calculate(
            self.amount("Principal: "),
            self.amount("Annual rate (%): "),
            self.amount("Years: "),
            self.ask("Simple or compound: "),
        )
        self.show("Interest estimate", result)

    def brokerage(self):
        print("Use your broker's current rates; fees vary.")
        self.run_calculation(
            Brokeragecalc,
            "Intraday estimate",
            (
                "Buy price: ", "Sell price: ", "Quantity: ", "Brokerage per order: ",
                "STT rate (%): ", "Exchange rate (%): ", "GST rate (%): ",
                "Stamp duty rate (%): ", "SEBI fee per crore: ",
            ),
            integer_inputs=(2,),
        )

    def insurance(self):
        kind = self.ask("Life or health? ").lower()
        if kind == "life":
            result = Insurancecalc.life_cover(
                self.amount("Annual income: "),
                self.amount("Years to replace income: "),
                self.amount("Liabilities: "),
                self.amount("Existing assets: "),
            )
        elif kind == "health":
            result = Insurancecalc.health_cover(
                self.count("People covered: "),
                self.amount("Desired cover per person: "),
                self.amount("Existing cover: "),
            )
        else:
            raise ValueError("Choose life or health.")
        self.show("Indicative cover needed", {"estimated_cover": result})

    def investment(self, calculator, title):
        self.run_calculation(calculator, title, (
            "Investment amount: ", "Assumed annual return (%): ", "Years: ",
        ))

    def sip(self):
        self.run_calculation(SIPcalc, "SIP projection", (
            "Monthly investment: ", "Assumed annual return (%): ", "Years: ",
        ))

    def loan(self, title):
        self.run_calculation(Loancalc, title, (
            "Loan principal: ", "Annual rate (%): ", "Term in months: ",
        ), integer_inputs=(2,))

    def assistant(self):
        self.run_calculation(FinAssistant, "Budget review", (
            "Monthly take-home income: ", "Monthly expenses: ",
            "Monthly debt payments: ", "Emergency-fund months: ",
        ))

    def run(self):
        actions = {
            "1": self.interest,
            "2": self.brokerage,
            "3": self.insurance,
            "4": lambda: self.investment(MutualFundcalc, "Mutual fund projection"),
            "5": self.sip,
            "6": lambda: self.loan("Housing loan estimate"),
            "7": lambda: self.loan("Personal loan estimate"),
            "8": self.assistant,
        }

        print("Personal Finance Toolkit — estimates only, not financial advice.")
        while True:
            print("\n" + "\n".join(self.MENU))
            choice = self.ask("Select a section: ")
            if choice == "0":
                print("Goodbye.")
                break

            action = actions.get(choice)
            if action is None:
                print("Choose a number from the menu.")
                continue

            try:
                action()


            except (ValueError, OverflowError) as exc:
                print(f"Input/calculation error: {exc}")


class calcTests(unittest.TestCase):


    def test_interest(self):
        self.assertEqual(Fincalc.calculate(1000, 10, 2, "simple")["total"], 1200)
        self.assertAlmostEqual(Fincalc.calculate(1000, 10, 2)["total"], 1210)

    def test_brokerage_without_fees(self):
        result = Brokeragecalc.calculate(100, 110, 2, 0, 0, 0, 0, 0, 0)
        self.assertEqual(result["net_pnl"], 20)

    def test_insurance(self):
        self.assertEqual(Insurancecalc.life_cover(100000, 10, 50000, 250000), 800000)
        self.assertEqual(Insurancecalc.health_cover(3, 500000, 200000), 1300000)

    def test_investments(self):
        self.assertAlmostEqual(MutualFundcalc.calculate(1000, 10, 2)["estimated_value"], 1210)
        self.assertEqual(SIPcalc.calculate(100, 0, 1)["estimated_value"], 1200)

    def test_loan(self):
        result = Loancalc.calculate(1200, 0, 12)
        self.assertEqual(result["monthly_payment"], 100)
        self.assertEqual(result["total_interest"], 0)

    def test_assistant_and_validation(self):
        self.assertEqual(FinAssistant.review(5000, 3000, 500)["monthly_surplus"], 1500)
        with self.assertRaises(ValueError):
            Loancalc.calculate(-100, 5, 12)
        with self.assertRaises(ValueError):
            positive_int(1.5, "Quantity")

    def test_run_calculation_supports_review_methods(self):
        app = FinanceApp()
        with mock.patch.object(FinanceApp, "amount", side_effect=[5000, 3000, 500, 6]), \
             mock.patch.object(FinanceApp, "count", side_effect=[]):
            app.run_calculation(FinAssistant, "Budget review", (
                "Monthly take-home income: ", "Monthly expenses: ",
                "Monthly debt payments: ", "Emergency-fund months: ",
            ))


if __name__ == "__main__":
    if "--test" in sys.argv:
        unittest.main(argv=[sys.argv[0]])
    else:
        FinanceApp().run()

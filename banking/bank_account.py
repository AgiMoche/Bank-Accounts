from decimal import Decimal


class BankAccount:
    @staticmethod
    def validate_transaction_amount(amount, transaction_type):
        assert isinstance(amount, (int, float, Decimal)), TypeError(
            f"Please provide a value of integer or float type for the {transaction_type} amount"
        )

        assert amount >= 0, ValueError(
            f"The {transaction_type} amount cannot be negative"
        )

        return Decimal(amount)

    def __init__(self, interest_rate, balance=0):
        self.balance = self.validate_transaction_amount(balance, "balance")
        self.interest_rate = self.validate_transaction_amount(interest_rate, "interest rate")

    def deposit(self, amount):
        self.balance = (Decimal(self.balance) + self.validate_transaction_amount(amount, "deposit")).quantize(Decimal("1.00"))

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(
                "You have requested to withdraw an amount that is greater than your current bank account balance"
            )

        self.balance = (Decimal(self.balance) - self.validate_transaction_amount(amount, "withdrawal")).quantize(Decimal("1.00"))

    def compound_interest(self):
        self.balance *= Decimal((1 + self.interest_rate / 1200))

        self.balance = self.balance.quantize(Decimal("1.00"))

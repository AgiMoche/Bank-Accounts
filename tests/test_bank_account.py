from decimal import Decimal
import pytest

from banking.bank_account import BankAccount


@pytest.fixture
def bank_account():
    return BankAccount(3.5, 1000)


def test_bank_account_withdraw(bank_account):
    bank_account.withdraw(amount=500)
    assert bank_account.balance == 500.00


def test_bank_account_deposit(bank_account):
    bank_account.deposit(amount=500)
    assert bank_account.balance == 1500.00


def test_bank_account_balance(bank_account):
    assert bank_account.balance == 1000.00


def test_bank_account_compound_interest(bank_account):
    bank_account.compound_interest()
    assert bank_account.balance == Decimal("1002.92")


def test_bank_account_with_negative_withdrawal_amount(bank_account):
    with pytest.raises(
        AssertionError,
        match="The withdrawal amount cannot be negative",
    ):
        bank_account.validate_transaction_amount(-500, "withdrawal")


def test_bank_account_with_negative_deposit_amount(bank_account):
    with pytest.raises(
        AssertionError,
        match="The deposit amount cannot be negative",
    ):
        bank_account.validate_transaction_amount(-500, "deposit")


def test_for_when_withdrawal_amount_more_than_available_balance(bank_account):
    with pytest.raises(
        ValueError,
        match="You have requested to withdraw an amount that is greater than your current bank account balance",
    ):
        bank_account.withdraw(amount=1500)


def test_negative_interest_rate_input(bank_account):
    with pytest.raises(
        AssertionError,
        match="The interest rate amount cannot be negative",
    ):
        bank_account.validate_transaction_amount(-3, "interest rate")


def test_for_incorrect_balance_data_type(bank_account):
    with pytest.raises(
        AssertionError,
        match="Please provide a value of integer or float type for the balance",
    ):
        bank_account.validate_transaction_amount("500", "balance")


def test_for_incorrect_interest_rate_data_type(bank_account):
    with pytest.raises(
        AssertionError,
        match="Please provide a value of integer or float type for the interest rate",
    ):
        bank_account.validate_transaction_amount("3.5", "interest rate")


def test_withdrawal_for_incorrect_amount_data_type(bank_account):
    with pytest.raises(
        AssertionError,
        match="Please provide a value of integer or float type for the withdrawal amount",
    ):
        bank_account.validate_transaction_amount("500", "withdrawal")


def test_deposit_for_incorrect_amount_data_type(bank_account):
    with pytest.raises(
        AssertionError,
        match="Please provide a value of integer or float type for the deposit amount",
    ):
        bank_account.validate_transaction_amount("500", "deposit")

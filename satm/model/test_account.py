from unittest import TestCase

from .account import Account


pan = '1'
pin = '1234'


class TestAccount(TestCase):
    def test_set_balance(self):
        account = Account(pan, pin)

        account.set_balance(100)

        assert account.balance == 100

    def test_deposit(self):
        account = Account(pan, pin)

        account.set_balance(100)
        account.deposit(200)

        assert account.balance == 300

    def test_withdraw(self):
        account = Account(pan, pin)

        account.set_balance(500)
        account.withdraw(200)

        assert account.balance == 300

    def test_withdraw_illegal_amount(self):
        account = Account(pan, pin)

        account.set_balance(500)
        account.withdraw(600)

        assert account.balance == 500

from unittest import TestCase

from ..model.account import Account
from .terminal_status import *

class TestTerminalStatus(TestCase):

    @classmethod
    def setUpClass(self):
        init_terminal_status(init_accounts())
        self.terminal_status = get_terminal_status()

    def test_reset_terminal_state(self):
        self.terminal_status.current_account = self.terminal_status.accounts[0]
        self.terminal_status.pin_attempts = 2
        self.terminal_status.current_pan = '1'
        self.terminal_status.deposit_withdrawal_amount = '250'

        self.terminal_status.reset_terminal_state()

        assert self.terminal_status.current_account == None
        assert self.terminal_status.pin_attempts == 0
        assert self.terminal_status.current_pan == ''
        assert self.terminal_status.deposit_withdrawal_amount == ''


    def test_reset_pin_entry(self):
        self.terminal_status.numbers_entered = 4
        self.terminal_status.current_pin = '1234'

        self.terminal_status.reset_pin_entry()

        assert self.terminal_status.numbers_entered == 0
        assert self.terminal_status.current_pin == ''

    def test_enter_pin_digit(self):
        self.terminal_status.current_pin = '12'
        self.terminal_status.numbers_entered = 2

        self.terminal_status.enter_pin_digit(3)

        assert self.terminal_status.numbers_entered == 3
        assert self.terminal_status.current_pin == '123'

    def test_pin_completed(self):
        self.terminal_status.current_pin = '123'
        self.terminal_status.numbers_entered = 3

        assert not self.terminal_status.pin_completed()

        self.terminal_status.enter_pin_digit(4)

        assert self.terminal_status.pin_completed()

    def test_get_account(self):
        self.terminal_status.current_account = self.terminal_status.accounts[0]

        account = self.terminal_status.get_account()

        assert account == self.terminal_status.accounts[0]

    def test_find_account_from_pin(self):
        self.terminal_status.current_pan = '1'
        self.terminal_status.current_pin = '1234'

        account = self.terminal_status.find_account_from_pin()

        assert account == self.terminal_status.accounts[0]

    def test_register_pin_attempt_and_validate_lockout(self):
        self.terminal_status.pin_attempts = 1

        assert not self.terminal_status.register_pin_attempt_and_validate_lockout() # 2 attempts
        assert self.terminal_status.register_pin_attempt_and_validate_lockout() # 3 attempts; lockout

    def test_deposit_withdrawal_amount_entry_in_progress(self):
        self.terminal_status.deposit_withdrawal_amount = '1'

        assert self.terminal_status.deposit_withdrawal_amount_entry_in_progress()

    def test_enter_deposit_withdrawal_digit(self):
        self.terminal_status.deposit_withdrawal_amount = '1'

        self.terminal_status.enter_deposit_withdrawal_digit(0)

        assert self.terminal_status.deposit_withdrawal_amount == '10'

    def test_deposit_into_current_account(self):
        self.terminal_status.current_account = self.terminal_status.accounts[0]
        amount_to_deposit = '20'
        self.terminal_status.deposit_withdrawal_amount = amount_to_deposit
        original_amount = self.terminal_status.current_account.balance

        self.terminal_status.deposit_into_current_account()

        assert self.terminal_status.current_account.balance == original_amount + int(amount_to_deposit)
        assert self.terminal_status.deposit_withdrawal_amount == ''


    def test_able_to_process_withdrawal(self):
        self.terminal_status.current_account = self.terminal_status.accounts[0]
        self.terminal_status.deposit_withdrawal_amount = '20'

        assert self.terminal_status.able_to_process_withdrawal()

        self.terminal_status.deposit_withdrawal_amount = '25'

        assert not self.terminal_status.able_to_process_withdrawal()

    def test_withdraw_from_current_account(self):
        self.terminal_status.current_account = self.terminal_status.accounts[0]
        amount_to_withdraw = '20'
        self.terminal_status.deposit_withdrawal_amount = amount_to_withdraw
        original_amount = self.terminal_status.current_account.balance

        self.terminal_status.withdraw_from_current_account()

        assert self.terminal_status.current_account.balance == original_amount - int(amount_to_withdraw)


def init_accounts():
    accounts = []
    account = Account(1, 1234)
    account.set_balance(200)
    accounts.append(account)

    account1 = Account(2, 9090)
    account1.set_balance(6000)
    accounts.append(account1)

    return accounts
from random import *

terminal_status = None

def get_terminal_status():
    return terminal_status


def init_terminal_status(accounts):
    global terminal_status
    if not terminal_status:
        terminal_status = TerminalStatus(accounts)


class TerminalStatus():

    def __init__(self, accounts):
        self.accounts = accounts
        self.current_account = None
        self.current_pan = ''
        self.current_pin = ''
        self.numbers_entered = 0
        self.pin_attempts = 0
        self.deposit_withdrawal_amount = ''

    def reset_terminal_state(self):
        self.current_account = None
        self.current_pan = ''
        self.pin_attempts = 0
        self.deposit_withdrawal_amount = ''
        self.reset_pin_entry()

    def reset_pin_entry(self):
        self.current_pin = ''
        self.numbers_entered = 0

    def enter_pin_digit(self, digit):
        if not self.pin_completed():
            self.current_pin += str(digit)
            self.numbers_entered += 1
        else:
            raise Exception('Attempted to enter pin digits when pin was already complete')

    def pin_completed(self):
        return self.numbers_entered > 3

    def get_account(self):
        if not self.current_account:
            self.current_account = self.find_account_from_pin()

        return self.current_account

    def find_account_from_pin(self):
        for account in self.accounts:
            if account.pin == self.current_pin and account.pan == self.current_pan:
                return account

        return None

    def register_pin_attempt_and_validate_lockout(self):
        self.pin_attempts += 1
        return self.pin_attempts >= 3

    def deposit_withdrawal_amount_entry_in_progress(self):
        return self.deposit_withdrawal_amount != ''

    def enter_deposit_withdrawal_digit(self, digit):
        self.deposit_withdrawal_amount += str(digit)

    def deposit_into_current_account(self):
        self.current_account.deposit(int(self.deposit_withdrawal_amount))
        # Then reset the amount
        self.deposit_withdrawal_amount = ''

    def able_to_process_withdrawal(self):
        return (int(self.total_currency()) >= int(self.deposit_withdrawal_amount)
               and int(self.deposit_withdrawal_amount) % 10 == 0
               and int(self.current_account.balance) >= int(self.deposit_withdrawal_amount))

    def withdraw_from_current_account(self):
        if self.able_to_process_withdrawal():
            self.current_account.withdraw(int(self.deposit_withdrawal_amount))
            amount_withdrawn = self.deposit_withdrawal_amount
            # reset the amount
            self.deposit_withdrawal_amount = ''
            return amount_withdrawn
        else:
            raise Exception('Tried to withdraw from account when unable to process')

    def is_deposit_slot_functional(self):
        rand = randint(1, 10)
        return rand > 2 # Give it an 80% chance of being functional

    def is_withdrawal_slot_functional(self):
        rand = randint(1, 10)
        return rand > 3  # Give it an 70% chance of being functional

    def total_currency(self):
        return randint(50, 1000)

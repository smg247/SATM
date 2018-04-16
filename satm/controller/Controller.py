from ..view.WelcomeView import WelcomeView
from ..view.PINView import PINView
from ..view.SelectTransactionView import SelectTransactionView
from ..view.BalanceView import BalanceView
from ..view.BalancePrintingView import BalancePrintingView
from ..view.IncorrectPINView import IncorrectPINView
from ..view.DepositView import DepositView
from ..view.MalfunctionView import MalfunctionView
from ..view.InsertDepositView import InsertDepositView
from ..view.WithdrawalView import WithdrawalView
from ..view.WithdrawalProcessedView import WithdrawalProcessedView
from ..view.WithdrawalFailedView import WithdrawalFailedView
from ..view.ExitView import ExitView

from .TerminalStatus import *

accounts = []
current_account = None

current_pan = ''
current_pin = ''
numbers_entered = 0
pin_attempts = 0

deposit_withdrawal_amount = ''


def transition_to_welcome(from_view):
    global current_pin, current_account, numbers_entered
    current_account = None
    current_pin = ''
    numbers_entered = 0
    welcome_view = WelcomeView(accounts)
    welcome_view.show()
    from_view.close()


def transition_to_exit(from_view):
    exit_view = ExitView()
    exit_view.show()
    from_view.close()


def transition_to_pin_entry(from_view, pan=None):
    global current_pan
    print('Transitioning to PIN Entry for pan: ' + str(pan))
    reset_pin_entry()
    if pan is not None:
        current_pan = pan
    pin_view = PINView(None)
    pin_view.show()
    from_view.close()


def handle_pin_entry(number, from_view):
    global current_pin, numbers_entered

    if numbers_entered > 3:
        print('Already entered 4 PIN numbers, ignoring this one')
    else:
        numbers_entered += 1
        current_pin += str(number)
        print('pin is now: ' + current_pin)

    new_pin_view = PINView(current_pin)
    new_pin_view.show()
    from_view.close()


def transition_to_transaction_selection(from_view):
    print('Transitioning to transaction selection')
    select_transaction_view = SelectTransactionView()
    select_transaction_view.show()
    from_view.close()


def validate_pin_and_transition(from_view):
    global current_account, pin_attempts

    account = find_account_from_pin(current_pin)
    if account is not None:
        print('Correctly entered PIN for account number: ' + account.pan)
        pin_attempts = 0
        current_account = account
        transition_to_transaction_selection(from_view)
    else:
        print('Incorrectly entered PIN')
        pin_attempts += 1
        if pin_attempts > 2:
            print('PIN attempts exceeded, keeping card')
            quit(1)
        reset_pin_entry()
        incorrect_pin_view = IncorrectPINView()
        incorrect_pin_view.show()


def transition_to_balance_printing(from_view):
    print('Transitioning to balance')
    balance_printing_view = BalancePrintingView(current_account)
    balance_printing_view.show()
    from_view.close()


def transition_to_show_balance(from_view):
    print('Transitioning to showing balance')
    balance_view = BalanceView(current_account)
    balance_view.show()
    from_view.close()


def transition_to_deposit(from_view):
    print('Transitioning to deposit')
    if deposit_withdrawal_amount != '' or is_deposit_slot_functional():
        print('Deposit slot functional')
        deposit_view = DepositView(deposit_withdrawal_amount)
        deposit_view.show()
    else:
        print('Deposit slot not functional')
        malfunction_view = MalfunctionView('deposit')
        malfunction_view.show()

    from_view.close()


def transition_to_withdrawal(from_view):
    print('Transitioning to withdrawal')
    if deposit_withdrawal_amount != '' or is_withdrawal_slot_functional():
        withdrawal_view = WithdrawalView(deposit_withdrawal_amount)
        withdrawal_view.show()
    else:
        print('Withdrawal not functional')
        malfunction_view = MalfunctionView('withdrawal')
        malfunction_view.show()

    from_view.close()


def handle_deposit_withdrawal_amount_entry(number, is_deposit, from_view):
    global deposit_withdrawal_amount
    deposit_withdrawal_amount += str(number)
    print('deposit/withdrawal amount is now: ' + str(deposit_withdrawal_amount))
    if is_deposit:
        transition_to_deposit(from_view)
    else:
        transition_to_withdrawal(from_view)


def transition_to_insert_deposit(from_view):
    print('Transitioning to insert deposit')
    insert_deposit_view = InsertDepositView()
    insert_deposit_view.show()
    from_view.close()


def handle_deposit(from_view):
    global deposit_withdrawal_amount
    print('Deposit slot used with amount of ' + str(deposit_withdrawal_amount))
    current_account.deposit(int(deposit_withdrawal_amount))
    deposit_withdrawal_amount = ''
    transition_to_balance_printing(from_view)


def handle_withdrawal(from_view):
    global deposit_withdrawal_amount
    print('Withdrawal requested for amount of ' + str(deposit_withdrawal_amount))
    if int(total_currency()) >= int(deposit_withdrawal_amount) and int(deposit_withdrawal_amount) % 10 == 0 and int(current_account.balance) >= int(deposit_withdrawal_amount):
        print('Withdrawal processed')
        current_account.withdraw(int(deposit_withdrawal_amount))
        withdrawal_processed_view = WithdrawalProcessedView(deposit_withdrawal_amount)
        withdrawal_processed_view.show()
    else:
        print('Unable to perform withdrawal')
        withdrawal_failed_view = WithdrawalFailedView()
        withdrawal_failed_view.show()

    deposit_withdrawal_amount = ''
    from_view.close()


def find_account_from_pin(pin):
    for account in accounts:
        if account.pin == pin and account.pan == current_pan:
            return account

    return None


def reset_pin_entry():
    global current_pin, numbers_entered
    current_pin = ''
    numbers_entered = 0
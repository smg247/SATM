from PyQt5.QtWidgets import QApplication

from ..view.welcome_view import WelcomeView
from ..view.pin_view import PINView
from ..view.select_transaction_view import SelectTransactionView
from ..view.balance_view import BalanceView
from ..view.balance_printing_view import BalancePrintingView
from ..view.incorrect_pin_view import IncorrectPINView
from ..view.deposit_view import DepositView
from ..view.malfunction_view import MalfunctionView
from ..view.insert_deposit_view import InsertDepositView
from ..view.withdrawal_view import WithdrawalView
from ..view.withdrawal_processed_view import WithdrawalProcessedView
from ..view.withdrawal_failed_view import WithdrawalFailedView
from ..view.exit_view import ExitView

from .terminal_status import get_terminal_status


def transition_to_welcome(from_view):
    terminal_status = get_terminal_status()
    terminal_status.reset_terminal_state()
    welcome_view = WelcomeView(terminal_status.accounts)
    welcome_view.show()
    from_view.close()


def transition_to_exit(from_view):
    exit_view = ExitView()
    exit_view.show()
    from_view.close()


def transition_to_pin_entry(from_view, pan=None):
    print('Transitioning to PIN Entry for pan: ' + str(pan))
    terminal_status = get_terminal_status()
    terminal_status.reset_pin_entry()
    if pan:
        terminal_status.current_pan = pan

    pin_view = PINView(None)
    pin_view.show()
    from_view.close()


def handle_pin_entry(number, from_view):
    terminal_status = get_terminal_status()
    if terminal_status.pin_completed():
        print('Already entered 4 PIN numbers, ignoring this one')
    else:
        terminal_status.enter_pin_digit(number)
        print('pin is now: ' + terminal_status.current_pin)

    new_pin_view = PINView(terminal_status.current_pin)
    new_pin_view.show()
    from_view.close()


def transition_to_transaction_selection(from_view):
    print('Transitioning to transaction selection')
    select_transaction_view = SelectTransactionView()
    select_transaction_view.show()
    from_view.close()


def validate_pin_and_transition(from_view):
    terminal_status = get_terminal_status()
    account = terminal_status.get_account()
    if account:
        print('Correctly entered PIN for account number: ' + account.pan)
        transition_to_transaction_selection(from_view)
    else:
        print('Incorrectly entered PIN')
        if terminal_status.register_pin_attempt_and_validate_lockout():
            print('PIN attempts exceeded, keeping card')
            transition_to_welcome(from_view)
        else:
            terminal_status.reset_pin_entry()
            incorrect_pin_view = IncorrectPINView()
            incorrect_pin_view.show()
            from_view.close()


def transition_to_balance_printing(from_view):
    print('Transitioning to balance')
    terminal_status = get_terminal_status()
    balance_printing_view = BalancePrintingView(terminal_status.get_account())
    balance_printing_view.show()
    from_view.close()


def transition_to_show_balance(from_view):
    print('Transitioning to showing balance')
    terminal_status = get_terminal_status()
    balance_view = BalanceView(terminal_status.get_account())
    balance_view.show()
    from_view.close()


def transition_to_deposit(from_view):
    print('Transitioning to deposit')
    terminal_status = get_terminal_status()
    if terminal_status.deposit_withdrawal_amount_entry_in_progress() or terminal_status.is_deposit_slot_functional():
        print('Deposit slot functional')
        deposit_view = DepositView(terminal_status.deposit_withdrawal_amount)
        deposit_view.show()
    else:
        print('Deposit slot not functional')
        malfunction_view = MalfunctionView('deposit')
        malfunction_view.show()

    from_view.close()


def transition_to_withdrawal(from_view):
    print('Transitioning to withdrawal')
    terminal_status = get_terminal_status()
    if terminal_status.deposit_withdrawal_amount_entry_in_progress() or terminal_status.is_withdrawal_slot_functional():
        withdrawal_view = WithdrawalView(terminal_status.deposit_withdrawal_amount)
        withdrawal_view.show()
    else:
        print('Withdrawal not functional')
        malfunction_view = MalfunctionView('withdrawal')
        malfunction_view.show()

    from_view.close()


def handle_deposit_withdrawal_amount_entry(number, is_deposit, from_view):
    terminal_status = get_terminal_status()
    terminal_status.enter_deposit_withdrawal_digit(number)
    print('deposit/withdrawal amount is now: ' + str(terminal_status.deposit_withdrawal_amount))
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
    terminal_status = get_terminal_status()
    print('Deposit slot used with amount of ' + str(terminal_status.deposit_withdrawal_amount))
    terminal_status.deposit_into_current_account()
    transition_to_balance_printing(from_view)


def handle_withdrawal(from_view):
    terminal_status = get_terminal_status()
    print('Withdrawal requested for amount of ' + str(terminal_status.deposit_withdrawal_amount))
    if terminal_status.able_to_process_withdrawal():
        print('Withdrawal processed')
        amount_withdrawn = terminal_status.withdraw_from_current_account()
        withdrawal_processed_view = WithdrawalProcessedView(amount_withdrawn)
        withdrawal_processed_view.show()
    else:
        print('Unable to perform withdrawal')
        withdrawal_failed_view = WithdrawalFailedView()
        withdrawal_failed_view.show()

    from_view.close()
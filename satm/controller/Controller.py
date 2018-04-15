from ..view.WelcomeView import WelcomeView
from ..view.PINView import PINView
from ..view.SelectTransactionView import SelectTransactionView
from ..view.BalanceView import BalanceView
from ..view.BalancePrintingView import BalancePrintingView
from ..view.IncorrectPINView import IncorrectPINView

accounts = []
current_account = None
current_pin = ''
numbers_entered = 0
pin_attempts = 0

def transition_to_welcome(from_view):
    global current_pin, current_account, numbers_entered
    current_account = None
    current_pin = ''
    numbers_entered = 0
    welcome_view = WelcomeView()
    welcome_view.show()
    from_view.close()

def transition_to_pin_entry(from_view):
    # TODO: for now we are going with the assumption that there is only one account and not going to require entry of the PAN, moving on to PIN screen
    print('Transitioning to PIN Entry')
    reset_pin_entry()
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

def transition_to_deposit(from_view):
    print('Transitioning to deposit')

def transition_to_withdrawal(from_view):
    print('Transitioning to withdrawal')

def find_account_from_pin(pin):
    #TODO: going to need to make sure this matches the PAN at some point
    for account in accounts:
        if account.pin == pin:
            return account

    return None

def reset_pin_entry():
    global current_pin, numbers_entered
    current_pin = ''
    numbers_entered = 0
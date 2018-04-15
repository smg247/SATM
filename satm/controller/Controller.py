from ..view.PINView import PINView

accounts = []
current_pin = ''
numbers_entered = 0

def transition_to_pin_entry(from_view):
    # TODO: for now we are going with the assumption that there is only one account and not going to require entry of the PAN, moving on to PIN screen
    print('Transitioning to PIN Entry')
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

def pin_entry_completed(from_view):
    account = find_account_from_pin(current_pin)
    if account is not None:
        print('Correctly entered PIN for account number: ' + account.pan)
    else:
        print('Incorrectly entered PIN')

    from_view.close()

def find_account_from_pin(pin):
    #TODO: going to need to make sure this matches the PAN at some point
    for account in accounts:
        if account.pin == pin:
            return account

    return None
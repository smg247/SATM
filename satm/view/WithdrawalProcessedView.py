from .BaseView import BaseView


class WithdrawalProcessedView(BaseView):

    def __init__(self, amount):
        super(WithdrawalProcessedView, self).__init__()
        self.cash_dispenser.setText('Cash: $' + str(amount))


    def setScreenContent(self, screen):
        screen.setText('<h1>Your balance is being updated. Please take cash from dispenser. Another transaction? Press R1 to continue. R2 to exit.</h1>')

    def handle_numerical_btn(self, value):
        from ..controller import Controller
        Controller.handle_deposit_withdrawal_amount_entry(value, False, self)

    def handle_side_btn(self, value):
        from satm.controller import Controller

        if value == 'R1':
            Controller.transition_to_transaction_selection(self)
        elif value == 'R2':
            Controller.transition_to_exit(self)
        else:
            print('Invalid option selected, ignoring')


from .BaseView import BaseView


class BalancePrintingView(BaseView):

    def __init__(self, account):
        super(BalancePrintingView, self).__init__()
        self.receipt_slot.setText('BALANCE: $' + str(account.balance))

    def setScreenContent(self, screen):
        screen.setText('<h1>Your new balance is being printed. Another transaction? Press R1 to continue.</h1>')

    def handle_side_btn(self, value):
        from satm.controller import Controller

        if value == 'R1':
            Controller.transition_to_transaction_selection(self)
        else:
            print('Invalid option selected, ignoring')
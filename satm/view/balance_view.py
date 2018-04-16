from .base_view import BaseView


class BalanceView(BaseView):

    def __init__(self, current_account):
        self.current_account = current_account
        super(BalanceView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Balance is: $' + str(self.current_account.balance) + '</h1>' +
                       '<h2>Another transaction? Press R1 to continue</h2>')

    def handle_side_btn(self, value):
        from satm.controller import controller

        if value == 'R1':
            controller.transition_to_transaction_selection(self)
        else:
            print('Invalid option selected, ignoring')
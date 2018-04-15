from .BaseView import BaseView


class BalanceView(BaseView):

    def __init__(self, current_account):
        self.current_account = current_account
        super(BalanceView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Balance is: $' + str(self.current_account.balance) + '</h1>')
from .BaseView import BaseView


class InsertDepositView(BaseView):

    def __init__(self):
        super(InsertDepositView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Please insert deposit into the Deposit Slot</h1>')

    def handle_deposit_slot(self):
        from ..controller import Controller
        Controller.handle_deposit(self)


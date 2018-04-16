from .BaseView import BaseView


class WelcomeView(BaseView):

    def __init__(self, accounts):
        self.accounts = accounts
        super(WelcomeView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Welcome, please insert your ATM card</h1>')

    def handle_card_slot(self):
        from ..controller import Controller
        pan = self.card_slot.currentText()
        Controller.transition_to_pin_entry(self, pan)

    def display_list_of_accounts(self):
        return True


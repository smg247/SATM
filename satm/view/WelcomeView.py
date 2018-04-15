from .BaseView import BaseView


class WelcomeView(BaseView):

    def __init__(self):
        super(WelcomeView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Welcome, please insert your ATM card</h1>')

    def handle_card_slot(self):
        from ..controller import Controller
        Controller.transition_to_pin_entry(self)




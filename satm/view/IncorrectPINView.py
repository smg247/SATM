from .BaseView import BaseView


class IncorrectPINView(BaseView):

    def __init__(self):
        super(IncorrectPINView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Your PIN is incorrect. Please try again. Press R1 to continue.</h1>')

    def handle_side_btn(self, value):
        from satm.controller import Controller

        if value == 'R1':
            Controller.transition_to_pin_entry(self)
        else:
            print('Invalid option selected, ignoring')






from .base_view import BaseView

entries = ['_ _ _ _', '_ _ _ *', '_ _ * *', '_ * * *', '* * * *']

class PINView(BaseView):

    def __init__(self, current_pin):
        if current_pin is None:
            self.current_pin = ''
            self.numbers_entered = 0
        else:
            self.current_pin = current_pin
            self.numbers_entered = len(current_pin)
        super(PINView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Please enter your PIN</h1>' +
                       '<br><br>' +
                       '<h2>' + entries[self.numbers_entered] + '</h2>')

    def handle_numerical_btn(self, value):
        from ..controller import controller # Who knew you could do this? I've got some cyclical imports, this solves it
        controller.handle_pin_entry(value, self)

    def handle_enter_btn(self):
        from ..controller import controller
        controller.validate_pin_and_transition(self)

    def handle_clear_btn(self):
        from ..controller import controller
        controller.transition_to_pin_entry(self)


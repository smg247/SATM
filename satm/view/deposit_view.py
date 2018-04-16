from .base_view import BaseView


class DepositView(BaseView):

    def __init__(self, amount_entered):
        self.amount_entered = amount_entered
        super(DepositView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Enter amount of deposit</h1>' +
                       '<h2>$' + self.amount_entered + '</h2>' +
                       '<h3>Once desired amount entered press "Enter"</h3>')

    def handle_numerical_btn(self, value):
        from ..controller import controller
        controller.handle_deposit_withdrawal_amount_entry(value, True, self)

    def handle_enter_btn(self):
        from ..controller import controller
        controller.transition_to_insert_deposit(self)


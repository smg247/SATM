from .base_view import BaseView


class WithdrawalView(BaseView):

    def __init__(self, amount_entered):
        self.amount_entered = str(amount_entered)
        super(WithdrawalView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Enter amount of withdrawal</h1>' +
                       '<h2>Must be a multiple of $10</h2>' +
                       '<h2>$' + self.amount_entered + '</h2>' +
                       '<h3>Once desired amount entered press "Enter"</h3>')

    def handle_numerical_btn(self, value):
        from ..controller import controller
        controller.handle_deposit_withdrawal_amount_entry(value, False, self)

    def handle_enter_btn(self):
        from ..controller import controller
        controller.handle_withdrawal(self)


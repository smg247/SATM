from .base_view import BaseView


class WithdrawalFailedView(BaseView):

    def __init__(self):
        super(WithdrawalFailedView, self).__init__()


    def setScreenContent(self, screen):
        screen.setText('<h1>Machine can only dispense $10 notes. It is also possible that the machine does not have the sufficient funds available to process. Another transaction? Press R1 to continue. R2 to exit.</h1>')

    def handle_side_btn(self, value):
        from satm.controller import controller

        if value == 'R1':
            controller.transition_to_transaction_selection(self)
        elif value == 'R2':
            controller.transition_to_welcome(self)
        else:
            print('Invalid option selected, ignoring')


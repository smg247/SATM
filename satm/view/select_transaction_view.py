from .base_view import BaseView



class SelectTransactionView(BaseView):

    def __init__(self):
        super(SelectTransactionView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Select transaction:</h1>' +
                       '<h2>balance press R1</h2>' +
                       '<h2>deposit press R2</h2>' +
                       '<h2>withdrawal press R3</h2>')

    def handle_side_btn(self, value):
        from satm.controller import controller

        if value == 'R1':
            controller.transition_to_show_balance(self)
        elif value == 'R2':
            controller.transition_to_deposit(self)
        elif value == 'R3':
            controller.transition_to_withdrawal(self)
        else:
            print ('Invalid option ' + value + ' selected, ignoring')



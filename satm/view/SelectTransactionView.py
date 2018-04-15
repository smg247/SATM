from .BaseView import BaseView



class SelectTransactionView(BaseView):

    def __init__(self):
        super(SelectTransactionView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Select transaction:</h1>' +
                       '<br>' +
                       '<h2>balance > R1</h2>' +
                       '<h2>deposit > R2</h2>' +
                       '<h2>withdrawal > R3</h2>')

    def handle_side_btn(self, value):
        from satm.controller import Controller

        if value == 'R1':
            Controller.transition_to_balance_printing(self)
        elif value == 'R2':
            Controller.transition_to_deposit(self)
        elif value == 'R3':
            Controller.transition_to_withdrawal(self)
        else:
            print ('Invalid option ' + value + ' selected, ignoring')



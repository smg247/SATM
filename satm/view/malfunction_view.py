from .base_view import BaseView


class MalfunctionView(BaseView):

    def __init__(self, type_string):
        self.type_string = type_string
        super(MalfunctionView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Temporarily unable to process ' + self.type_string + '. Another transaction? Press R1 to continue.</h1>')

    def handle_side_btn(self, value):
        from satm.controller import controller

        if value == 'R1':
            controller.transition_to_transaction_selection(self)
        elif value == 'R2':
            controller.transition_to_exit(self)
        else:
            print('Invalid option selected, ignoring')
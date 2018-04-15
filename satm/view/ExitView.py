from .BaseView import BaseView


class ExitView(BaseView):

    def __init__(self):
        super(ExitView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Please take your receipt and ATM card. Thank you.</h1>')




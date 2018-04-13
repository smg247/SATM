from BaseView import BaseView
from PINView import PINView


class WelcomeView(BaseView):

    def __init__(self):
        super(WelcomeView, self).__init__()

    def setScreenContent(self, textEdit):
        textEdit.textCursor().insertHtml('<h1>Welcome, please insert your ATM card</h1>')

    def handle_card_slot(self):
        #TODO: for now we are going with the assumption that there is only one account and not going to require entry of the PAN, moving on to PIN screen
        pin_view = PINView()
        pin_view.show()




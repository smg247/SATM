from BaseView import BaseView


class WelcomeView(BaseView):

    def __init__(self):
        super(WelcomeView, self).__init__()

    def setScreenContent(self, textEdit):
        textEdit.textCursor().insertHtml('<h1>Welcome, please insert your ATM card</h1>')



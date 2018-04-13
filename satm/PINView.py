from BaseView import BaseView


class PINView(BaseView):

    def __init__(self):
        super(PINView, self).__init__()

    def setScreenContent(self, textEdit):
        textEdit.textCursor().insertHtml('<h1>Please enter your PIN</h1>')
from BaseView import BaseView

entries = ['_ _ _ _', '_ _ _ *', '_ _ * *', '_ * * *', '* * * *']

class PINView(BaseView):

    def __init__(self, current_pin):
        if current_pin is None:
            self.current_pin = ''
            self.numbers_entered = 0
        else:
            self.current_pin = current_pin
            self.numbers_entered = len(current_pin)
        super(PINView, self).__init__()

    def setScreenContent(self, screen):
        screen.setText('<h1>Please enter your PIN</h1>' +
                       '<br><br>' +
                       '<h2>' + entries[self.numbers_entered] + '</h2>')

    def handle_numerical_btn(self, value):
        #TODO: all of this logic needs to go within some view transitioning controller it could possibly even have some state on it to make things easier. this is untestable as is.
        self.numbers_entered += 1
        self.current_pin += str(value)
        print('pin is now: ' + self.current_pin)
        if self.numbers_entered < 4:
            new_pin_view = PINView(self.current_pin)
            new_pin_view.show()
            self.close()
        else:
            #TODO: go to next page
            pass

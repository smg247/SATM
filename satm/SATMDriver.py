import sys

from PyQt5.QtWidgets import QApplication, QWidget

from WelcomeView import WelcomeView
from model import Account

accounts = []

def seed_accounts():
    account = Account(1, 1234)
    account.set_balance(200)
    accounts.append(account)

if __name__ == '__main__':
    seed_accounts()
    app = QApplication(sys.argv)
    ex = WelcomeView()
    sys.exit(app.exec_())

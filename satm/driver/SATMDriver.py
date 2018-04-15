import sys

from PyQt5.QtWidgets import QApplication, QWidget

from satm.view import WelcomeView
from satm.model import Account
from satm.controller import Controller

def seed_accounts():
    accounts = []
    account = Account(1, 1234)
    account.set_balance(200)
    accounts.append(account)

    account1 = Account(2, 9090)
    account1.set_balance(6000)
    accounts.append(account1)

    return accounts

if __name__ == '__main__':
    Controller.accounts = seed_accounts()
    app = QApplication(sys.argv)
    ex = WelcomeView()
    sys.exit(app.exec_())

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from satm.view import WelcomeView
from satm.model import Account
from satm.controller.terminal_status import init_terminal_status


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
    app = QApplication(sys.argv)
    accounts = seed_accounts()
    terminal_status = init_terminal_status(accounts)
    window = WelcomeView(accounts)
    sys.exit(app.exec_())

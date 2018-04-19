from unittest import TestCase

from pytestqt import qtbot

from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton, QApplication

from satm.model.account import Account
from satm.view import *
from .terminal_status import *


def test_card_entry(qtbot):
    accounts, _ = set_up_accounts_and_terminal_status()
    welcome_view = WelcomeView(accounts)
    qtbot.addWidget(welcome_view)

    qtbot.keyClicks(welcome_view.card_slot, '1')

    assert_screen_shows(PINView)


def test_valid_pin_entry(qtbot):
    _, terminal_status = set_up_accounts_and_terminal_status()
    terminal_status.current_pan = '1'
    pin_view = PINView(None)
    qtbot.addWidget(pin_view)

    qtbot.mouseClick(pin_view.btn_1, QtCore.Qt.LeftButton)
    qtbot.mouseClick(pin_view.btn_2, QtCore.Qt.LeftButton)
    qtbot.mouseClick(pin_view.btn_3, QtCore.Qt.LeftButton)
    qtbot.mouseClick(pin_view.btn_4, QtCore.Qt.LeftButton)
    qtbot.mouseClick(pin_view.enter_btn, QtCore.Qt.LeftButton)

    assert_screen_shows(SelectTransactionView)


def test_invalid_pin_entry(qtbot):
    _, terminal_status = set_up_accounts_and_terminal_status()
    terminal_status.pin_attempts = 2
    pin_view = PINView(None)
    qtbot.addWidget(pin_view)

    qtbot.mouseClick(pin_view.btn_9, QtCore.Qt.LeftButton)
    qtbot.mouseClick(pin_view.btn_9, QtCore.Qt.LeftButton)
    qtbot.mouseClick(pin_view.btn_9, QtCore.Qt.LeftButton)
    qtbot.mouseClick(pin_view.btn_9, QtCore.Qt.LeftButton)
    qtbot.mouseClick(pin_view.enter_btn, QtCore.Qt.LeftButton)

    assert_screen_shows(WelcomeView)


def set_up_accounts_and_terminal_status():
    global terminal_status
    terminal_status = None
    accounts = []
    account = Account('1', '1234')
    account.balance = 500
    accounts.append(account)
    init_terminal_status(accounts)
    new_terminal_status = get_terminal_status()
    return accounts, new_terminal_status


def assert_screen_shows(view):
    widgets = QApplication.topLevelWidgets()
    for widget in widgets:
        assert (not widget.isActiveWindow()) or isinstance(widget, view)

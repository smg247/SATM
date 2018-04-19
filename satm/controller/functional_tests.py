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

    assert_screen_shows_and_get_new_screen(PINView)


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

    assert_screen_shows_and_get_new_screen(SelectTransactionView)


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

    assert_screen_shows_and_get_new_screen(WelcomeView)


def test_balance_inquiry(qtbot):
    accounts, terminal_status = set_up_accounts_and_terminal_status()
    terminal_status.current_account = accounts[0]
    select_transaction_view = SelectTransactionView()
    qtbot.addWidget(select_transaction_view)

    qtbot.mouseClick(select_transaction_view.r1_btn, QtCore.Qt.LeftButton)

    assert_screen_shows_and_get_new_screen(BalanceView)


def test_deposit(qtbot):
    accounts, terminal_status = set_up_accounts_and_terminal_status()
    terminal_status.current_account = accounts[0]
    # monkey patch deposit slot to always be functional
    terminal_status.is_deposit_slot_functional = lambda:True
    select_transaction_view = SelectTransactionView()
    qtbot.addWidget(select_transaction_view)

    # choose deposit
    qtbot.mouseClick(select_transaction_view.r2_btn, QtCore.Qt.LeftButton)
    deposit_view = assert_screen_shows_and_get_new_screen(DepositView)

    # enter amount of $10
    qtbot.addWidget(deposit_view)
    qtbot.mouseClick(deposit_view.btn_1, QtCore.Qt.LeftButton)
    qtbot.mouseClick(deposit_view.btn_0, QtCore.Qt.LeftButton)
    qtbot.mouseClick(deposit_view.enter_btn, QtCore.Qt.LeftButton)
    insert_deposit_view = assert_screen_shows_and_get_new_screen(InsertDepositView)

    # put money in slot
    qtbot.addWidget(insert_deposit_view)
    qtbot.mouseClick(insert_deposit_view.deposit_slot, QtCore.Qt.LeftButton)
    assert_screen_shows_and_get_new_screen(BalancePrintingView)


def test_deposit_jammed(qtbot):
    accounts, terminal_status = set_up_accounts_and_terminal_status()
    terminal_status.current_account = accounts[0]
    # monkey patch deposit slot to always be jammed
    terminal_status.is_deposit_slot_functional = lambda: False
    select_transaction_view = SelectTransactionView()
    qtbot.addWidget(select_transaction_view)

    qtbot.mouseClick(select_transaction_view.r2_btn, QtCore.Qt.LeftButton)
    assert_screen_shows_and_get_new_screen(MalfunctionView)


def test_withdrawal(qtbot):
    accounts, terminal_status = set_up_accounts_and_terminal_status()
    terminal_status.current_account = accounts[0]
    # monkey patch withdrawal slot to always be functional
    terminal_status.is_withdrawal_slot_functional = lambda: True
    select_transaction_view = SelectTransactionView()
    qtbot.addWidget(select_transaction_view)

    # choose withdrawal
    qtbot.mouseClick(select_transaction_view.r3_btn, QtCore.Qt.LeftButton)
    withdrawal_view = assert_screen_shows_and_get_new_screen(WithdrawalView)

    # enter amount of $10
    qtbot.addWidget(withdrawal_view)
    qtbot.mouseClick(withdrawal_view.btn_1, QtCore.Qt.LeftButton)
    qtbot.mouseClick(withdrawal_view.btn_0, QtCore.Qt.LeftButton)
    qtbot.mouseClick(withdrawal_view.enter_btn, QtCore.Qt.LeftButton)
    withdrawal_processed_view = assert_screen_shows_and_get_new_screen(WithdrawalProcessedView)

    # exit
    qtbot.addWidget(withdrawal_processed_view)
    qtbot.mouseClick(withdrawal_processed_view.r2_btn, QtCore.Qt.LeftButton)
    assert_screen_shows_and_get_new_screen(ExitView)


def test_withdrawal_invalid_amount(qtbot):
    accounts, terminal_status = set_up_accounts_and_terminal_status()
    terminal_status.current_account = accounts[0]
    # monkey patch withdrawal slot to always be functional
    terminal_status.is_withdrawal_slot_functional = lambda: True
    terminal_status.total_currency = lambda: 1000
    select_transaction_view = SelectTransactionView()
    qtbot.addWidget(select_transaction_view)

    # choose withdrawal
    qtbot.mouseClick(select_transaction_view.r3_btn, QtCore.Qt.LeftButton)
    withdrawal_view = assert_screen_shows_and_get_new_screen(WithdrawalView)

    # enter amount of $88
    qtbot.addWidget(withdrawal_view)
    qtbot.mouseClick(withdrawal_view.btn_8, QtCore.Qt.LeftButton)
    qtbot.mouseClick(withdrawal_view.btn_8, QtCore.Qt.LeftButton)
    qtbot.mouseClick(withdrawal_view.enter_btn, QtCore.Qt.LeftButton)
    assert_screen_shows_and_get_new_screen(WithdrawalFailedView)


def test_withdrawal_insufficient_funds(qtbot):
    accounts, terminal_status = set_up_accounts_and_terminal_status()
    terminal_status.current_account = accounts[0]
    # monkey patch withdrawal slot to always be functional
    terminal_status.is_withdrawal_slot_functional = lambda: True
    terminal_status.total_currency = lambda: 1000
    select_transaction_view = SelectTransactionView()
    qtbot.addWidget(select_transaction_view)

    # choose withdrawal
    qtbot.mouseClick(select_transaction_view.r3_btn, QtCore.Qt.LeftButton)
    withdrawal_view = assert_screen_shows_and_get_new_screen(WithdrawalView)

    # enter amount of $600
    qtbot.addWidget(withdrawal_view)
    qtbot.mouseClick(withdrawal_view.btn_6, QtCore.Qt.LeftButton)
    qtbot.mouseClick(withdrawal_view.btn_0, QtCore.Qt.LeftButton)
    qtbot.mouseClick(withdrawal_view.btn_0, QtCore.Qt.LeftButton)
    qtbot.mouseClick(withdrawal_view.enter_btn, QtCore.Qt.LeftButton)
    assert_screen_shows_and_get_new_screen(WithdrawalFailedView)


def test_withdrawal_terminal_insufficient_funds(qtbot):
    accounts, terminal_status = set_up_accounts_and_terminal_status()
    terminal_status.current_account = accounts[0]
    # monkey patch withdrawal slot to always be functional
    terminal_status.is_withdrawal_slot_functional = lambda: True
    terminal_status.total_currency = lambda: 200
    select_transaction_view = SelectTransactionView()
    qtbot.addWidget(select_transaction_view)

    # choose withdrawal
    qtbot.mouseClick(select_transaction_view.r3_btn, QtCore.Qt.LeftButton)
    withdrawal_view = assert_screen_shows_and_get_new_screen(WithdrawalView)

    # enter amount of $300
    qtbot.addWidget(withdrawal_view)
    qtbot.mouseClick(withdrawal_view.btn_3, QtCore.Qt.LeftButton)
    qtbot.mouseClick(withdrawal_view.btn_0, QtCore.Qt.LeftButton)
    qtbot.mouseClick(withdrawal_view.btn_0, QtCore.Qt.LeftButton)
    qtbot.mouseClick(withdrawal_view.enter_btn, QtCore.Qt.LeftButton)
    assert_screen_shows_and_get_new_screen(WithdrawalFailedView)

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


def assert_screen_shows_and_get_new_screen(view):
    widgets = QApplication.topLevelWidgets()
    for widget in widgets:
        assert (not widget.isActiveWindow()) or isinstance(widget, view)

    for widget in widgets:
        if isinstance(widget, view):
            return widget

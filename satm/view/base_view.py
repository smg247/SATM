from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox
from PyQt5.QtCore import Qt


class BaseView(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Simple ATM'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        overall_layout = QVBoxLayout()

        screen_area_layout = QHBoxLayout()
        screen_area_layout.addLayout(self.initScreenButtons(True))
        screen_area_layout.addWidget(self.initScreen())
        screen_area_layout.addLayout(self.initScreenButtons(False))
        overall_layout.addLayout(screen_area_layout)

        button_area_layout = QHBoxLayout()
        button_area_layout.addWidget(self.initReceiptSlot())
        button_area_layout.addLayout(self.initNumericalKeypad())
        button_area_layout.addLayout(self.initCardSlotAndButtons())
        overall_layout.addLayout(button_area_layout)

        overall_layout.addLayout(self.initDepositAndDispenser())

        self.setLayout(overall_layout)
        self.show()

    def initScreen(self):
        screen = QLabel()
        screen.setWordWrap(True)
        screen.setAlignment(Qt.AlignCenter)
        screen.setFixedWidth(600)
        screen.setStyleSheet('QLabel { background-color : white; }')
        self.setScreenContent(screen)

        return screen


    def initScreenButtons(self, leftSide):
        layout = QVBoxLayout()
        if leftSide:
            layout.addWidget(QPushButton('L1'))
            layout.addWidget(QPushButton('L2'))
            layout.addWidget(QPushButton('L3'))
            layout.addWidget(QPushButton('L4'))
        else:
            self.r1_btn = QPushButton('R1')
            self.r1_btn.clicked.connect(lambda: self.handle_side_btn('R1'))
            layout.addWidget(self.r1_btn)

            self.r2_btn = QPushButton('R2')
            self.r2_btn.clicked.connect(lambda: self.handle_side_btn('R2'))
            layout.addWidget(self.r2_btn)

            self.r3_btn = QPushButton('R3')
            self.r3_btn.clicked.connect(lambda: self.handle_side_btn('R3'))
            layout.addWidget(self.r3_btn)

            self.r4_btn = QPushButton('R4')
            self.r4_btn.clicked.connect(lambda: self.handle_side_btn('R4'))
            layout.addWidget(self.r4_btn)

        return layout

    def initNumericalKeypad(self):
        layout = QVBoxLayout()

        row_layout = QHBoxLayout()
        self.btn_1 = QPushButton('1')
        self.btn_1.clicked.connect(lambda:self.handle_numerical_btn(1))
        row_layout.addWidget(self.btn_1)

        self.btn_2 = QPushButton('2')
        self.btn_2.clicked.connect(lambda: self.handle_numerical_btn(2))
        row_layout.addWidget(self.btn_2)

        self.btn_3 = QPushButton('3')
        self.btn_3.clicked.connect(lambda: self.handle_numerical_btn(3))
        row_layout.addWidget(self.btn_3)

        layout.addLayout(row_layout)

        row_layout = QHBoxLayout()
        self.btn_4 = QPushButton('4')
        self.btn_4.clicked.connect(lambda: self.handle_numerical_btn(4))
        row_layout.addWidget(self.btn_4)

        self.btn_5 = QPushButton('5')
        self.btn_5.clicked.connect(lambda: self.handle_numerical_btn(5))
        row_layout.addWidget(self.btn_5)

        self.btn_6 = QPushButton('6')
        self.btn_6.clicked.connect(lambda: self.handle_numerical_btn(6))
        row_layout.addWidget(self.btn_6)

        layout.addLayout(row_layout)

        row_layout = QHBoxLayout()
        self.btn_7 = QPushButton('7')
        self.btn_7.clicked.connect(lambda: self.handle_numerical_btn(7))
        row_layout.addWidget(self.btn_7)

        self.btn_8 = QPushButton('8')
        self.btn_8.clicked.connect(lambda: self.handle_numerical_btn(8))
        row_layout.addWidget(self.btn_8)

        self.btn_9 = QPushButton('9')
        self.btn_9.clicked.connect(lambda: self.handle_numerical_btn(9))
        row_layout.addWidget(self.btn_9)

        layout.addLayout(row_layout)

        row_layout = QHBoxLayout()
        self.btn_0 = QPushButton('0')
        self.btn_0.clicked.connect(lambda: self.handle_numerical_btn(0))
        row_layout.addWidget(self.btn_0)
        layout.addLayout(row_layout)

        return layout

    def initReceiptSlot(self):
        self.receipt_slot = QPushButton('Printed Receipt')
        return self.receipt_slot

    def initCardSlotAndButtons(self):
        layout = QVBoxLayout()

        card_slot_layout = QHBoxLayout()
        card_slot_layout.addWidget(QLabel('Card Slot:'))
        self.card_slot = QComboBox()
        if self.display_list_of_accounts():
            self.card_slot.addItem('Select PAN')
            self.account_selection = dict()
            for account in self.accounts:
                self.account_selection[account.pan] = self.card_slot.addItem(account.pan)
        else:
            self.card_slot.addItem('CARD INSERTED')

        self.card_slot.activated[str].connect(lambda:self.handle_card_slot())
        card_slot_layout.addWidget(self.card_slot)
        layout.addLayout(card_slot_layout)

        self.enter_btn = QPushButton('Enter')
        self.enter_btn.clicked.connect(lambda: self.handle_enter_btn())
        layout.addWidget(self.enter_btn)

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.clicked.connect(lambda: self.handle_clear_btn())
        layout.addWidget(self.clear_btn)

        self.cancel_btn = QPushButton('Cancel')
        self.cancel_btn.clicked.connect(lambda: self.handle_cancel_btn())
        layout.addWidget(self.cancel_btn)

        return layout

    def initDepositAndDispenser(self):
        layout = QHBoxLayout()
        self.cash_dispenser = QPushButton('Cash Dispenser')
        layout.addWidget(self.cash_dispenser)
        self.deposit_slot = QPushButton('Deposit Slot')
        self.deposit_slot.clicked.connect(lambda: self.handle_deposit_slot())
        layout.addWidget(self.deposit_slot)

        return layout

    def handle_card_slot(self):
        print('card slot pressed, controller for this screen ignores this')

    def handle_enter_btn(self):
        print('enter button pressed, controller for this screen ignores this')

    def handle_clear_btn(self):
        print('clear button pressed, controller for this screen ignores this')

    def handle_cancel_btn(self):
        from ..controller import controller
        print('cancel button pressed, always returns to welcome')
        controller.transition_to_welcome(self)

    def handle_numerical_btn(self, value):
        print(str(value) + ' was pressed, controller for this screen ignores this')

    def handle_side_btn(self, value):
        print(str(value) + ' was pressed, controller for this screen ignores this')

    def handle_deposit_slot(self):
        print('Deposit Slot pressed, controller for this screen ignores this')

    def display_list_of_accounts(self):
        return False
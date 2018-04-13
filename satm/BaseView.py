from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class BaseView(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Simple ATM'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 1000
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
        textEdit = QTextEdit()
        textEdit.setReadOnly(True)

        cursor = textEdit.textCursor()
        cursor.insertHtml('<br><br>')

        # This is a call to the required subclass method
        self.setScreenContent(textEdit)

        block_format = cursor.blockFormat()
        block_format.setAlignment(Qt.AlignCenter)
        cursor.mergeBlockFormat(block_format)
        return textEdit

    def initScreenButtons(self, leftSide):
        layout = QVBoxLayout()
        if leftSide:
            layout.addWidget(QPushButton('L1'))
            layout.addWidget(QPushButton('L2'))
            layout.addWidget(QPushButton('L3'))
            layout.addWidget(QPushButton('L4'))
        else:
            layout.addWidget(QPushButton('R1'))
            layout.addWidget(QPushButton('R2'))
            layout.addWidget(QPushButton('R3'))
            layout.addWidget(QPushButton('R4'))

        return layout

    #TODO: I think this should be its own class, might help with the controller interactions
    def initNumericalKeypad(self):
        layout = QVBoxLayout()

        row_layout = QHBoxLayout()
        row_layout.addWidget(QPushButton('1'))
        row_layout.addWidget(QPushButton('2'))
        row_layout.addWidget(QPushButton('3'))
        layout.addLayout(row_layout)

        row_layout = QHBoxLayout()
        row_layout.addWidget(QPushButton('4'))
        row_layout.addWidget(QPushButton('5'))
        row_layout.addWidget(QPushButton('6'))
        layout.addLayout(row_layout)

        row_layout = QHBoxLayout()
        row_layout.addWidget(QPushButton('7'))
        row_layout.addWidget(QPushButton('8'))
        row_layout.addWidget(QPushButton('9'))
        layout.addLayout(row_layout)

        row_layout = QHBoxLayout()
        row_layout.addWidget(QPushButton('0'))
        layout.addLayout(row_layout)

        return layout

    def initReceiptSlot(self):
        return QPushButton('Printed Receipt')

    def initCardSlotAndButtons(self):
        layout = QVBoxLayout()

        self.card_slot = QPushButton('Card Slot')
        self.card_slot.clicked.connect(lambda:self.handle_card_slot())
        layout.addWidget(self.card_slot)

        layout.addWidget(QPushButton('Enter'))
        layout.addWidget(QPushButton('Clear'))
        layout.addWidget(QPushButton('Cancel'))

        return layout

    def initDepositAndDispenser(self):
        layout = QHBoxLayout()
        layout.addWidget(QPushButton('Cash Dispenser'))
        layout.addWidget(QPushButton('Deposit Slot'))

        return layout

    def handle_card_slot(self):
        print('card slot pressed, controller for this screen ignores this')

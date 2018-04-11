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
        layout = QVBoxLayout()
        layout.addWidget(self.initScreen())
        layout.addLayout(self.initKeypad())
        self.setLayout(layout)
        self.show()

    def initScreen(self):
        textEdit = QTextEdit()
        textEdit.setReadOnly(True)

        cursor = textEdit.textCursor()
        cursor.insertHtml('<br><br>')
        self.setScreenContent(textEdit)
        block_format = cursor.blockFormat()
        block_format.setAlignment(Qt.AlignCenter)
        cursor.mergeBlockFormat(block_format)
        return textEdit

    #TODO: I think this should be its own class, might help with the controller interactions
    def initKeypad(self):
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


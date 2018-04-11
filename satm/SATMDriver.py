import sys

from PyQt5.QtWidgets import QApplication, QWidget

from WelcomeView import WelcomeView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WelcomeView()
    sys.exit(app.exec_())

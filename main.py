
from PyQt5.QtWidgets import QApplication,  QWidget
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
import sys

from ATM.Form import LoginForm

class MainWindow(qtw.QWidget):

      def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.setWindowTitle('ATM App')

            # create widgets
            btn_registration = qtw.QPushButton('Registration')
            btn_login = qtw.QPushButton('Login')
            self.setGeometry(1000, 200, 200, 60)

            #create main layout
            main_layout = qtw.QHBoxLayout(self)
            main_layout.addWidget(btn_registration)
            main_layout.addWidget(btn_login)

            btn_login.clicked.connect(self.onBtnLoginClick)

            self.show()

      @qtc.pyqtSlot(bool)
      def onBtnLoginClick(self, *args):
            self.form = LoginForm()
            self.form.show()

if __name__ == '__main__':
      app = qtw.QApplication(sys.argv)

      window = MainWindow()

      sys.exit(app.exec_())

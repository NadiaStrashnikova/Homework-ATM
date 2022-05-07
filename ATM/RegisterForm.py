from PyQt5 import QtWidgets as qtw
from ATM.clients import ClientsList
from ATM.Ui_RegisterWidget import Ui_Form

class RegisterForm(Ui_Form, qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
from PyQt5 import QtWidgets as qtw
from ATM.clients import ClientsList
from ATM.Ui_FormWidget import Ui_Form

class m_Form(Ui_Form):
    entered_pin_count = 0

    def __init__(self,w)->None:
        self.setupUi(w)

        self.all_clients = ClientsList()

        self.btn_CheckName.clicked.connect(self.get_real_client)
        self.btn_CheckPin.clicked.connect(self.get_pin)
        self.btn_Action.clicked.connect(self.client_make_choice)
        self.btn_Close.clicked.connect(self.close_app)

    def get_real_client(self):
        name = self.le_UserName.text()
        self.real_client = self.all_clients.check_if_client_exists(name)
        if self.real_client == None:
            msg_box = qtw.QMessageBox()
            msg_box.setIcon(qtw.QMessageBox.Information)
            msg_box.setText("There is no such user.")
            msg_box.exec()
        else:
            self.le_PIN.setDisabled(False)
            self.le_PIN.setPlaceholderText('Enter PIN')
            self.btn_CheckPin.setDisabled(False)

    def get_pin(self):
        self.entered_pin_count += 1
        if self.entered_pin_count < 4:
            new_pin = self.le_PIN.text()
            if new_pin == self.real_client.pin:
                self.lbl_Balance_value.setText(str(self.real_client.balance))
                self.rb_withdraw.setDisabled(False)
                self.rb_launder.setDisabled(False)
                self.le_SumToOperate.setDisabled(False)
                self.btn_Action.setDisabled(False)
            else:
                msg_box = qtw.QMessageBox()
                msg_box.setIcon(qtw.QMessageBox.Information)
                msg_box.setText("Wrong PIN")
                msg_box.exec()
        else:
            msg_box = qtw.QMessageBox()
            msg_box.setIcon(qtw.QMessageBox.Information)
            msg_box.setText("The card is blocked")
            msg_box.exec()
            exit()

    def client_make_choice(self):
        if self.rb_launder.isChecked():
            self.money_laundering()
        elif self.rb_withdraw.isChecked():
            self.withdrawing_money()

    def withdrawing_money(self):
        self.is_numbered_entered()
        tegli_suma = float(self.le_SumToOperate.text())
        if self.real_client.balance < tegli_suma:
            msg_box = qtw.QMessageBox()
            msg_box.setIcon(qtw.QMessageBox.Information)
            msg_box.setText("The value is more than you have. Enter new value")
            msg_box.exec()
        else:
            self.real_client.subtract_from_balance(tegli_suma)
            self.lbl_Balance_value.setText(str(self.real_client.balance))

    def money_laundering(self):
        self.is_numbered_entered()
        add_s = float(self.le_SumToOperate.text())
        self.real_client.add_to_balance(add_s)
        self.lbl_Balance_value.setText(str(self.real_client.balance))

    def is_numbered_entered(self):
        text = self.le_SumToOperate.text()
        text.replace('.','')
        text.replace(',', '')
        if not text.isnumeric():
            msg_box = qtw.QMessageBox()
            msg_box.setIcon(qtw.QMessageBox.Information)
            msg_box.setText("Enter only digits")
            msg_box.exec()
            self.le_SumToOperate.setText('0.00')

    def close_app(self):
        exit()
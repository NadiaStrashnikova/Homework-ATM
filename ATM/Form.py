from PyQt5 import QtCore, QtWidgets
from ATM.clients import ClientsList
from ATM.Ui_FormWidget import Ui_Form

class m_Form(Ui_Form):
    def __init__(self,w)->None:
        self.setupUi(w)

        #self.all_clients = ClientsList()

        self.btn_CheckName.clicked.connect(self.get_real_client)
        self.btn_CheckPin.clicked.connect(self.get_pin)
        self.pushButton.clicked.connect(self.client_make_choice)
        self.pushButton.setText('Calculate')
        #self.btn_CheckName.clicked.connect(self.get_real_client)

    def get_real_client(self):
        self.all_clients = ClientsList()
        #all_clients.load_clients()
        name = self.le_UserName.text()
        self.real_client = self.all_clients.check_if_client_exists(name)
        if self.real_client == None:
            exit()
        self.le_PIN.setDisabled(False)
        self.le_PIN.setPlaceholderText('Enter PIN')
        self.btn_CheckPin.setDisabled(False)

    def get_pin(self):
        ok = False
        for _ in range(1, 4):
            new_pin = self.le_PIN.text()
            if new_pin == self.real_client.pin:
                ok = True
                break
        if not ok:
            print('Картата е блокирана')
            exit()

        self.le_Balance.setText(str(self.real_client.balance))
        self.rb_withdraw.setDisabled(False)
        self.rb_launder.setDisabled(False)
        self.le_Balance.setDisabled(False)
        self.le_SumToOperate.setDisabled(False)
        self.pushButton.setDisabled(False)

    def client_make_choice(self):
        if self.rb_launder.isChecked():
            self.money_laundering()
        elif self.rb_withdraw.isChecked():
            self.withdrawing_money()

    def withdrawing_money(self):
        tegli_suma = float(self.le_SumToOperate.text())
        while self.real_client.balance < tegli_suma:
            tegli_suma = float(input('Сумата е повече от наличното. Колко теглите:'))
        self.real_client.subtract_from_balance(tegli_suma)
        self.le_Balance.setText(str(self.real_client.balance))
        exit()

    def money_laundering(self):
        add_s = float(self.le_SumToOperate.text())
        self.real_client.add_to_balance(add_s)
        self.le_Balance.setText(str(self.real_client.balance))
        exit()

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from ATM.clients import ClientsList
from ATM.Ui_RegisterWidget import Ui_Form
from ATM.db import DB

class RegisterForm(Ui_Form, qtw.QWidget):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		self.btnSubmit.clicked.connect(self.onBtnSubmitClick)
		self.btnCancel.clicked.connect(self.onBtnCloseClick)
		self.db = DB('root', '123Proba321', 'test')

	@qtc.pyqtSlot(bool)
	def onBtnSubmitClick(self):
		user_name = self.leUserName.text()
		user_pasword = self.lePass.text()
		print(user_name, user_pasword)

		# HW: add your code, which will check if user exists in DB
		if self.db.insert_user(user_name=user_name, password=user_pasword):
			self.handleInsertSuccess()
		else:
			self.handleInsertFail()

	def handleInsertSuccess(self):
		msg_box = qtw.QMessageBox()
		msg_box.setIcon(qtw.QMessageBox.Information)
		msg_box.setText("User is successfuly inserted in!")
		msg_box.setInformativeText("Some informative text")
		msg_box.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
		msg_box.setDefaultButton(qtw.QMessageBox.Ok)
		msg_box.exec()

	def handleInsertFail(self):
		msg_box = qtw.QMessageBox()
		msg_box.setIcon(qtw.QMessageBox.Critical)
		msg_box.setText("User is not loged in")
		# msg_box.setInformativeText("Some informative text");
		msg_box.setStandardButtons(qtw.QMessageBox.Ok)
		msg_box.setDefaultButton(qtw.QMessageBox.Ok)
		msg_box.buttonClicked.connect(lambda btn: print(btn.text()))
		msg_box.exec()

	def onBtnCloseClick(self):
		self.close()

if __name__ == '__main__':
	db = DB('root', '123Proba321','test')

	# let's use some hard-coded values for test:
	user_name = 'Maria'
	password = 'maria123'

	if db.authenticate(user_name=user_name, password=password):
		print('User is valid')
	else:
		print('Invalid user name or password')
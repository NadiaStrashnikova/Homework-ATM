# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(315, 290)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.frml_login = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.frml_login.setContentsMargins(0, 0, 0, 0)
        self.frml_login.setObjectName("frml_login")
        self.lbl_UserName = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_UserName.setObjectName("lbl_UserName")
        self.frml_login.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_UserName)
        self.le_UserName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_UserName.setObjectName("le_UserName")
        self.frml_login.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_UserName)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frml_login.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.btn_CheckName = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_CheckName.setObjectName("btn_CheckName")
        self.frml_login.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_CheckName)
        self.lbl_PIN = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_PIN.setObjectName("lbl_PIN")
        self.frml_login.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_PIN)
        self.le_PIN = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_PIN.setEnabled(False)
        self.le_PIN.setObjectName("le_PIN")
        self.frml_login.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_PIN)
        self.btn_CheckPin = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_CheckPin.setEnabled(False)
        self.btn_CheckPin.setObjectName("btn_CheckPin")
        self.frml_login.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btn_CheckPin)
        self.formLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 130, 291, 61))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.frml_action = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.frml_action.setContentsMargins(0, 0, 0, 0)
        self.frml_action.setSpacing(0)
        self.frml_action.setObjectName("frml_action")
        self.le_SumToOperate = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.le_SumToOperate.setEnabled(False)
        self.le_SumToOperate.setObjectName("le_SumToOperate")
        self.frml_action.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.le_SumToOperate)
        self.rb_withdraw = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.rb_withdraw.setEnabled(False)
        self.rb_withdraw.setCheckable(True)
        self.rb_withdraw.setChecked(False)
        self.rb_withdraw.setObjectName("rb_withdraw")
        self.frml_action.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rb_withdraw)
        spacerItem1 = QtWidgets.QSpacerItem(18, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.frml_action.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.rb_launder = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.rb_launder.setEnabled(False)
        self.rb_launder.setObjectName("rb_launder")
        self.frml_action.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rb_launder)
        self.btn_Action = QtWidgets.QPushButton(self.formLayoutWidget_3)
        self.btn_Action.setEnabled(False)
        self.btn_Action.setObjectName("btn_Action")
        self.frml_action.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.btn_Action)
        self.btn_Close = QtWidgets.QPushButton(Form)
        self.btn_Close.setGeometry(QtCore.QRect(30, 250, 236, 23))
        self.btn_Close.setObjectName("btn_Close")
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(60, 200, 151, 31))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbl_Balance = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lbl_Balance.setObjectName("lbl_Balance")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_Balance)
        self.lbl_Balance_value = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lbl_Balance_value.setObjectName("lbl_Balance_value")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lbl_Balance_value)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_UserName.setText(_translate("Form", "User name:"))
        self.btn_CheckName.setText(_translate("Form", "Check name"))
        self.lbl_PIN.setText(_translate("Form", "PIN:"))
        self.btn_CheckPin.setText(_translate("Form", "Check pin"))
        self.rb_withdraw.setText(_translate("Form", "Withdraw"))
        self.rb_launder.setText(_translate("Form", "Launder"))
        self.btn_Action.setText(_translate("Form", "Do action"))
        self.btn_Close.setText(_translate("Form", "Close"))
        self.lbl_Balance.setText(_translate("Form", "Balance"))
        self.lbl_Balance_value.setText(_translate("Form", "0.00"))

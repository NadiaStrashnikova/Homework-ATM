# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(315, 261)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 180, 281, 31))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lbl_Balance = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.lbl_Balance.setObjectName("lbl_Balance")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_Balance)
        self.le_Balance = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.le_Balance.setObjectName("le_Balance")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_Balance)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 281, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbl_UserName = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_UserName.setObjectName("lbl_UserName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_UserName)
        self.le_UserName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_UserName.setObjectName("le_UserName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_UserName)
        self.lbl_PIN = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_PIN.setObjectName("lbl_PIN")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_PIN)
        self.le_PIN = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_PIN.setObjectName("le_PIN")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_PIN)
        self.Btn_Close = QtWidgets.QPushButton(Form)
        self.Btn_Close.setGeometry(QtCore.QRect(100, 220, 75, 23))
        self.Btn_Close.setObjectName("Btn_Close")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 281, 81))
        self.groupBox.setObjectName("groupBox")
        self.rb_withdraw = QtWidgets.QRadioButton(self.groupBox)
        self.rb_withdraw.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.rb_withdraw.setObjectName("rb_withdraw")
        self.rb_launder = QtWidgets.QRadioButton(self.groupBox)
        self.rb_launder.setGeometry(QtCore.QRect(160, 20, 82, 17))
        self.rb_launder.setObjectName("rb_launder")
        self.le_SumToOperate = QtWidgets.QLineEdit(self.groupBox)
        self.le_SumToOperate.setGeometry(QtCore.QRect(20, 50, 241, 21))
        self.le_SumToOperate.setObjectName("le_SumToOperate")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_Balance.setText(_translate("Form", "Balance"))
        self.lbl_UserName.setText(_translate("Form", "User name:"))
        self.lbl_PIN.setText(_translate("Form", "PIN:"))
        self.Btn_Close.setText(_translate("Form", "Close"))
        self.groupBox.setTitle(_translate("Form", "Choose action:"))
        self.rb_withdraw.setText(_translate("Form", "Withdraw"))
        self.rb_launder.setText(_translate("Form", "Launder"))

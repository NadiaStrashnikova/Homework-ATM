# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(351, 180)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 311, 158))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.frm_layout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.frm_layout.setContentsMargins(0, 0, 0, 0)
        self.frm_layout.setObjectName("frm_layout")
        self.lbl_user_name = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_user_name.setObjectName("lbl_user_name")
        self.frm_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_user_name)
        self.lbl_user_pin = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_user_pin.setObjectName("lbl_user_pin")
        self.frm_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lbl_user_pin)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frm_layout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.le_user_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_user_name.setObjectName("le_user_name")
        self.frm_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_user_name)
        self.le_uesr_pin = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_uesr_pin.setObjectName("le_uesr_pin")
        self.frm_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_uesr_pin)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frm_layout.setItem(4, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.btnSubmit = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnSubmit.setObjectName("btnSubmit")
        self.frm_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.btnSubmit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.frm_layout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.btnCancel = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btnCancel.setObjectName("btnCancel")
        self.frm_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.btnCancel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_user_name.setText(_translate("Form", "Input user name"))
        self.lbl_user_pin.setText(_translate("Form", "Input user PIN"))
        self.btnSubmit.setText(_translate("Form", "Register user"))
        self.btnCancel.setText(_translate("Form", "Close"))

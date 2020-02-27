# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

import project_library, hashlib


class Ui_MainWindow(object):
    def setupUi(self, RegisterPage):
        self.RegisterPage = RegisterPage
        RegisterPage.setObjectName("RegisterPage")
        RegisterPage.resize(592, 531)
        self.centralwidget = QtWidgets.QWidget(RegisterPage)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.R_displayname_input = QtWidgets.QLineEdit(self.centralwidget)
        self.R_displayname_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.R_displayname_input.setObjectName("R_displayname_input")
        self.verticalLayout.addWidget(self.R_displayname_input)
        self.R_email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.R_email_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.R_email_input.setObjectName("R_email_input")
        self.verticalLayout.addWidget(self.R_email_input)
        self.R_password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.R_password_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.R_password_input.setObjectName("R_password_input")
        self.R_password_input.setEchoMode(QLineEdit.Password)
        self.verticalLayout.addWidget(self.R_password_input)
        self.R_confirmpass_input = QtWidgets.QLineEdit(self.centralwidget)
        self.R_confirmpass_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.R_confirmpass_input.setObjectName("R_confirmpass_input")
        self.R_confirmpass_input.setEchoMode(QLineEdit.Password)
        self.verticalLayout.addWidget(self.R_confirmpass_input)
        self.R_regist_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.R_regist_Btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.R_regist_Btn.setObjectName("R_regist_Btn")
        self.verticalLayout.addWidget(self.R_regist_Btn)

        self.R_warning = QtWidgets.QLabel(self.centralwidget)
        self.R_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.R_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.R_warning.setMaximumSize(QtCore.QSize(16777215, 25))
        self.R_warning.setObjectName("R_warning")
        self.verticalLayout.addWidget(self.R_warning)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        RegisterPage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RegisterPage)
        self.statusbar.setObjectName("statusbar")
        RegisterPage.setStatusBar(self.statusbar)

        self.retranslateUi(RegisterPage)
        QtCore.QMetaObject.connectSlotsByName(RegisterPage)

        self.R_regist_Btn.clicked.connect(self.regist)

    def regist(self):
        if self.R_displayname_input.text() == '' or self.R_email_input.text() == '' or\
                self.R_password_input.text() == '' or self.R_confirmpass_input.text() == '':
            self.setWarningText('Please Fill In All Field')
            print('>> Please Fill In All Field')
        else:
            if self.R_password_input.text() != self.R_confirmpass_input.text():
                self.setWarningText('Password And Confirm Password Do Not Match!')
                print('>> password and confirm password do not match!')

            else:
                if project_library.register(self.R_email_input.text(),
                                            hashlib.md5(self.R_password_input.text().encode()).hexdigest(),
                                            self.R_displayname_input.text()):
                    print('>> go back to Login Page')
                    self.RegisterPage.hide()
                else:
                    self.setWarningText('Username Already Used')
                    print('>> Username Already Used')


    def setWarningText(self, text):
        self.R_warning.setText("""< html > < head / > < body > < p > < span
            style =\" color:#ff0000;\">{}</span></p></body></html>""".format(text))

    def retranslateUi(self, RegisterPage):
        _translate = QtCore.QCoreApplication.translate
        RegisterPage.setWindowTitle(_translate("RegisterPage", "RegisterPage"))
        self.R_displayname_input.setPlaceholderText(_translate("RegisterPage", "Display Name"))
        self.R_email_input.setPlaceholderText(_translate("RegisterPage", "Email"))
        self.R_password_input.setPlaceholderText(_translate("RegisterPage", "Password"))
        self.R_confirmpass_input.setPlaceholderText(_translate("RegisterPage", "Confirm Password"))
        self.R_regist_Btn.setText(_translate("RegisterPage", "Regist"))
        self.R_warning.setText(_translate("RegisterPage", ""))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    RegisterPage = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(RegisterPage)
    RegisterPage.show()
    sys.exit(app.exec_())

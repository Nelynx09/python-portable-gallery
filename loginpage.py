# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

import project_library, hashlib


class Ui_MainWindow(object):
    def setupUi(self, LoginPage):
        self.LoginPage = LoginPage
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(632, 600)
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.L_title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_title.sizePolicy().hasHeightForWidth())
        self.L_title.setSizePolicy(sizePolicy)
        self.L_title.setMaximumSize(QtCore.QSize(16777215, 500))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.L_title.setFont(font)
        self.L_title.setAlignment(QtCore.Qt.AlignCenter)
        self.L_title.setObjectName("L_title")
        self.verticalLayout_2.addWidget(self.L_title)
        self.L_email_input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_email_input.sizePolicy().hasHeightForWidth())
        self.L_email_input.setSizePolicy(sizePolicy)
        self.L_email_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.L_email_input.setObjectName("L_email_input")
        self.verticalLayout_2.addWidget(self.L_email_input)
        self.L_pass_input = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_pass_input.sizePolicy().hasHeightForWidth())
        self.L_pass_input.setSizePolicy(sizePolicy)
        self.L_pass_input.setMaximumSize(QtCore.QSize(16777215, 50))
        self.L_pass_input.setObjectName("L_pass_input")
        self.L_pass_input.setEchoMode(QLineEdit.Password)
        self.verticalLayout_2.addWidget(self.L_pass_input)
        self.L_regist = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_regist.sizePolicy().hasHeightForWidth())
        self.L_regist.setSizePolicy(sizePolicy)
        self.L_regist.setMaximumSize(QtCore.QSize(16777215, 50))
        self.L_regist.setObjectName("L_regist")
        self.verticalLayout_2.addWidget(self.L_regist)
        self.L_login = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.L_login.sizePolicy().hasHeightForWidth())
        self.L_login.setSizePolicy(sizePolicy)
        self.L_login.setMaximumSize(QtCore.QSize(16777215, 50))
        self.L_login.setObjectName("L_login")
        self.verticalLayout_2.addWidget(self.L_login)
        LoginPage.setCentralWidget(self.centralwidget)
        self.L_warning = QtWidgets.QLabel(self.centralwidget)
        self.L_warning.setMaximumSize(QtCore.QSize(16777215, 25))
        self.L_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.L_warning.setObjectName("L_warning")
        self.verticalLayout_2.addWidget(self.L_warning)

        self.statusbar = QtWidgets.QStatusBar(LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

        self.L_login.clicked.connect(self.login)
        self.L_regist.clicked.connect(self.goRegister)

    def login(self):
        check = project_library.login(
            self.L_email_input.text(),
            hashlib.md5(self.L_pass_input.text().encode()).hexdigest())
        if self.L_email_input.text() == '' or self.L_pass_input.text() == '' or check is None:
            self.setWarningText('Your Username or Password Not Correct!')
        else:
            print('>> go to HomePage')
            import main_window
            self.window = QtWidgets.QMainWindow()
            self.ui = main_window.Ui_MainWindow()
            self.ui.setupUi(self.window, check['_id'])
            self.window.show()
            self.LoginPage.hide()

    def setWarningText(self, text):
        self.L_warning.setText("""< html > < head / > < body > < p > < span
            style =\" color:#ff0000;\">{}</span></p></body></html>""".format(text))

    def goRegister(self):
        print('>> go to RegisterPage')
        import registerpage
        self.window = QtWidgets.QMainWindow()
        self.ui = registerpage.Ui_MainWindow()
        self.ui.setupUi(self.window, )
        self.window.show()

    def retranslateUi(self, MainWindow):
        # TODO: secure password
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("LoginPage", "LoginPage"))
        self.L_title.setText(_translate("LoginPage", "Portable Gallery"))
        self.L_email_input.setPlaceholderText(_translate("LoginPage", "Email"))
        self.L_pass_input.setPlaceholderText(_translate("LoginPage", "Password"))
        self.L_regist.setText(_translate("LoginPage", "Register"))
        self.L_login.setText(_translate("LoginPage", "Login"))
        self.L_warning.setText(_translate("LoginPage", ""))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())

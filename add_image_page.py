# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_image_page.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import project_library
from tkinter import filedialog


class Ui_MainWindow(object):
    def setupUi(self, AddImagePage,
                main_page
                ):
        self.AddImagePage = AddImagePage
        AddImagePage.setObjectName("AddImagePage")
        AddImagePage.resize(633, 600)
        self.centralwidget = QtWidgets.QWidget(AddImagePage)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.A_caption_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.A_caption_textEdit.setObjectName("A_caption_textEdit")
        self.verticalLayout_2.addWidget(self.A_caption_textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.A_selectimage_btn = QtWidgets.QPushButton(self.centralwidget)
        self.A_selectimage_btn.setObjectName("A_selectimage_btn")
        self.horizontalLayout.addWidget(self.A_selectimage_btn)
        self.A_upload_btn = QtWidgets.QPushButton(self.centralwidget)
        self.A_upload_btn.setObjectName("A_upload_btn")
        self.horizontalLayout.addWidget(self.A_upload_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.A_preview_img = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_preview_img.sizePolicy().hasHeightForWidth())
        self.A_preview_img.setSizePolicy(sizePolicy)
        self.A_preview_img.setAlignment(QtCore.Qt.AlignCenter)
        self.A_preview_img.setObjectName("A_preview_img")
        self.verticalLayout_2.addWidget(self.A_preview_img)
        AddImagePage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddImagePage)
        self.statusbar.setObjectName("statusbar")
        AddImagePage.setStatusBar(self.statusbar)

        self.retranslateUi(AddImagePage)
        QtCore.QMetaObject.connectSlotsByName(AddImagePage)

        self.mainpage = main_page

        self.A_upload_btn.setEnabled(False)
        self.filepath = ''

        self.A_upload_btn.clicked.connect(self.uploadImage)
        self.A_selectimage_btn.clicked.connect(self.openFileSelectWindow)

        self.default_filepath = ''

    def openFileSelectWindow(self):

        filepath = QFileDialog.getOpenFileName(filter="Images (*.png *.xpm *.jpg *.jpeg)")

        print(filepath[0])
        if filepath[0] != '':
            self.A_upload_btn.setEnabled(True)
            if self.default_filepath != filepath[0]:
                print(filepath[0])
                self.default_filepath = filepath[0]
                pm = QtGui.QPixmap()
                pm.loadFromData(project_library.getImage(project_library.get_preview_image(self.default_filepath)))
                self.A_preview_img.setPixmap(pm)

            self.default_filepath = filepath[0]

        else:
            self.A_upload_btn.setEnabled(False)


    def uploadImage(self):
        project_library.upload_image_by_path(self.default_filepath, self.A_caption_textEdit.toPlainText(), self.mainpage.userid)
        self.AddImagePage.hide()
        self.mainpage.refresh()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("AddImagePage", "AddImagePage"))
        self.A_caption_textEdit.setPlaceholderText(_translate("AddImagePage", "Type Your Caption Here"))
        self.A_selectimage_btn.setText(_translate("AddImagePage", "Select Image"))
        self.A_upload_btn.setText(_translate("AddImagePage", "Upload"))
        self.A_preview_img.setText(_translate("AddImagePage", ""))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

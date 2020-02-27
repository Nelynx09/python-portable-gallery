# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manage_image_page.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import project_library


class Ui_MainWindow2(object):
    def setupUi(self, ManageImagePage, img_id, main_page, img_old_caption):
        self.ManageImagePage = ManageImagePage
        ManageImagePage.setObjectName("ManageImagePage")
        ManageImagePage.resize(597, 600)
        self.centralwidget = QtWidgets.QWidget(ManageImagePage)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.M_caption_textedit = QtWidgets.QTextEdit(self.centralwidget)
        self.M_caption_textedit.setObjectName("M_caption_textedit")
        self.verticalLayout_2.addWidget(self.M_caption_textedit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.M_delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.M_delete_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.M_delete_btn.setObjectName("M_delete_btn")
        self.horizontalLayout.addWidget(self.M_delete_btn)
        self.M_save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.M_save_btn.setObjectName("M_save_btn")
        self.horizontalLayout.addWidget(self.M_save_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        ManageImagePage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ManageImagePage)
        self.statusbar.setObjectName("statusbar")
        ManageImagePage.setStatusBar(self.statusbar)

        self.retranslateUi(ManageImagePage)
        QtCore.QMetaObject.connectSlotsByName(ManageImagePage)

        self.imgid = img_id
        self.main_page = main_page
        self.M_caption_textedit.setText(img_old_caption)

        self.M_save_btn.clicked.connect(self.save)
        self.M_delete_btn.clicked.connect(self.delete_image)

    def save(self):
        print(self.imgid)
        print(self.M_caption_textedit.toPlainText())
        newText = self.M_caption_textedit.toPlainText()
        project_library.edit_caption(self.imgid, newText)

        self.main_page.refresh()
        self.ManageImagePage.hide()

    def delete_image(self):
        project_library.delete_image(self.imgid)

        self.main_page.refresh()
        self.ManageImagePage.hide()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("ManageImagePage", "ManageImagePage"))
        self.label.setText(_translate("ManageImagePage",
                                      "<html><head/><body><p><span style=\" font-weight:600;\">Caption</span></p></body></html>"))
        self.M_caption_textedit.setHtml(_translate("ManageImagePage",
                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">old caption</p></body></html>"))
        self.M_delete_btn.setText(_translate("ManageImagePage", "Delete this image"))
        self.M_save_btn.setText(_translate("ManageImagePage", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ManageImagePage = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(ManageImagePage, 'i0', 'testt')
    ManageImagePage.show()
    sys.exit(app.exec_())

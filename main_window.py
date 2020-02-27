# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import project_library


class Ui_MainWindow(object):
    def setupUi(self, AppMainWindow, userid):
        self.AppMainWindow = AppMainWindow
        AppMainWindow.setObjectName("MainWindow")
        AppMainWindow.resize(647, 629)
        self.centralwidget = QtWidgets.QWidget(AppMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_feed = QtWidgets.QWidget()
        self.tab_feed.setObjectName("tab_feed")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_feed)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.H_img = QtWidgets.QLabel(self.tab_feed)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.H_img.sizePolicy().hasHeightForWidth())
        self.H_img.setSizePolicy(sizePolicy)
        self.H_img.setAlignment(QtCore.Qt.AlignCenter)
        self.H_img.setObjectName("H_img")
        self.gridLayout_3.addWidget(self.H_img, 0, 0, 1, 1)
        self.H_img_like_btn = QtWidgets.QPushButton(self.tab_feed)
        self.H_img_like_btn.setObjectName("H_img_like_btn")
        self.gridLayout_3.addWidget(self.H_img_like_btn, 5, 0, 1, 1)
        self.horizontalWidget = QtWidgets.QWidget(self.tab_feed)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.H_prev_btn = QtWidgets.QPushButton(self.horizontalWidget)
        self.H_prev_btn.setObjectName("H_prev_btn")
        self.horizontalLayout_6.addWidget(self.H_prev_btn)
        self.H_next_btn = QtWidgets.QPushButton(self.horizontalWidget)
        self.H_next_btn.setObjectName("H_next_btn")
        self.horizontalLayout_6.addWidget(self.H_next_btn)
        self.gridLayout_3.addWidget(self.horizontalWidget, 6, 0, 1, 1)
        self.horizontalWidget1 = QtWidgets.QWidget(self.tab_feed)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget1.sizePolicy().hasHeightForWidth())
        self.horizontalWidget1.setSizePolicy(sizePolicy)
        self.horizontalWidget1.setObjectName("horizontalWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.H_img_user = QtWidgets.QLabel(self.horizontalWidget1)
        self.H_img_user.setObjectName("H_img_user")
        self.horizontalLayout_5.addWidget(self.H_img_user)
        self.H_img_like = QtWidgets.QLabel(self.horizontalWidget1)
        self.H_img_like.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.H_img_like.setObjectName("H_img_like")
        self.horizontalLayout_5.addWidget(self.H_img_like)
        self.gridLayout_3.addWidget(self.horizontalWidget1, 3, 0, 1, 1)
        self.horizontalWidget2 = QtWidgets.QWidget(self.tab_feed)
        self.horizontalWidget2.setObjectName("horizontalWidget2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalWidget2)
        self.horizontalLayout_9.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.H_img_caption = QtWidgets.QLabel(self.horizontalWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.H_img_caption.sizePolicy().hasHeightForWidth())
        self.H_img_caption.setSizePolicy(sizePolicy)
        self.H_img_caption.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.H_img_caption.setWordWrap(True)
        self.H_img_caption.setObjectName("H_img_caption")
        self.horizontalLayout_9.addWidget(self.H_img_caption)
        self.gridLayout_3.addWidget(self.horizontalWidget2, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab_feed, "")
        self.tab_friend = QtWidgets.QWidget()
        self.tab_friend.setObjectName("tab_friend")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_friend)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.F_text_4 = QtWidgets.QLabel(self.tab_friend)
        self.F_text_4.setAlignment(QtCore.Qt.AlignCenter)
        self.F_text_4.setObjectName("F_text_4")
        self.gridLayout_4.addWidget(self.F_text_4, 1, 3, 1, 1)
        self.F_btn_3 = QtWidgets.QPushButton(self.tab_friend)
        self.F_btn_3.setMinimumSize(QtCore.QSize(16777215, 30))
        self.F_btn_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.F_btn_3.setObjectName("F_btn_3")
        self.gridLayout_4.addWidget(self.F_btn_3, 2, 2, 1, 1)
        self.F_text_3 = QtWidgets.QLabel(self.tab_friend)
        self.F_text_3.setAlignment(QtCore.Qt.AlignCenter)
        self.F_text_3.setObjectName("F_text_3")
        self.gridLayout_4.addWidget(self.F_text_3, 1, 2, 1, 1)
        self.F_btn_1 = QtWidgets.QPushButton(self.tab_friend)
        self.F_btn_1.setMinimumSize(QtCore.QSize(16777215, 30))
        self.F_btn_1.setMaximumSize(QtCore.QSize(16777215, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F_btn_1.sizePolicy().hasHeightForWidth())
        self.F_btn_1.setSizePolicy(sizePolicy)
        self.F_btn_1.setObjectName("F_btn_1")
        self.gridLayout_4.addWidget(self.F_btn_1, 2, 0, 1, 1)
        self.F_btn_6 = QtWidgets.QPushButton(self.tab_friend)
        self.F_btn_6.setMinimumSize(QtCore.QSize(16777215, 30))
        self.F_btn_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.F_btn_6.setObjectName("F_btn_6")
        self.gridLayout_4.addWidget(self.F_btn_6, 4, 1, 1, 1)
        self.F_text_8 = QtWidgets.QLabel(self.tab_friend)
        self.F_text_8.setAlignment(QtCore.Qt.AlignCenter)
        self.F_text_8.setObjectName("F_text_8")
        self.gridLayout_4.addWidget(self.F_text_8, 3, 3, 1, 1)
        self.F_btn_2 = QtWidgets.QPushButton(self.tab_friend)
        self.F_btn_2.setMinimumSize(QtCore.QSize(16777215, 30))
        self.F_btn_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.F_btn_2.setMaximumSize(QtCore.QSize(16777215, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F_btn_2.sizePolicy().hasHeightForWidth())
        self.F_btn_2.setSizePolicy(sizePolicy)
        self.F_btn_2.setObjectName("F_btn_2")
        self.gridLayout_4.addWidget(self.F_btn_2, 2, 1, 1, 1)
        self.F_text_5 = QtWidgets.QLabel(self.tab_friend)
        self.F_text_5.setAlignment(QtCore.Qt.AlignCenter)
        self.F_text_5.setObjectName("F_text_5")
        self.gridLayout_4.addWidget(self.F_text_5, 3, 0, 1, 1)
        self.F_text_6 = QtWidgets.QLabel(self.tab_friend)
        self.F_text_6.setAlignment(QtCore.Qt.AlignCenter)
        self.F_text_6.setObjectName("F_text_6")
        self.gridLayout_4.addWidget(self.F_text_6, 3, 1, 1, 1)
        self.F_text_1 = QtWidgets.QLabel(self.tab_friend)
        self.F_text_1.setAlignment(QtCore.Qt.AlignCenter)
        self.F_text_1.setObjectName("F_text_1")
        self.gridLayout_4.addWidget(self.F_text_1, 1, 0, 1, 1)
        self.F_text_7 = QtWidgets.QLabel(self.tab_friend)
        self.F_text_7.setAlignment(QtCore.Qt.AlignCenter)
        self.F_text_7.setObjectName("F_text_7")
        self.gridLayout_4.addWidget(self.F_text_7, 3, 2, 1, 1)
        self.F_btn_8 = QtWidgets.QPushButton(self.tab_friend)
        self.F_btn_8.setMinimumSize(QtCore.QSize(16777215, 30))
        self.F_btn_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.F_btn_8.setObjectName("F_btn_8")
        self.gridLayout_4.addWidget(self.F_btn_8, 4, 3, 1, 1)
        self.F_btn_7 = QtWidgets.QPushButton(self.tab_friend)
        self.F_btn_7.setMinimumSize(QtCore.QSize(16777215, 30))
        self.F_btn_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.F_btn_7.setObjectName("F_btn_7")
        self.gridLayout_4.addWidget(self.F_btn_7, 4, 2, 1, 1)
        self.F_btn_5 = QtWidgets.QPushButton(self.tab_friend)
        self.F_btn_5.setMinimumSize(QtCore.QSize(16777215, 30))
        self.F_btn_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.F_btn_5.setObjectName("F_btn_5")
        self.gridLayout_4.addWidget(self.F_btn_5, 4, 0, 1, 1)
        self.F_text_2 = QtWidgets.QLabel(self.tab_friend)
        self.F_text_2.setAlignment(QtCore.Qt.AlignCenter)
        self.F_text_2.setObjectName("F_text_2")
        self.gridLayout_4.addWidget(self.F_text_2, 1, 1, 1, 1)
        self.F_btn_4 = QtWidgets.QPushButton(self.tab_friend)
        self.F_btn_4.setMinimumSize(QtCore.QSize(16777215, 30))
        self.F_btn_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.F_btn_4.setObjectName("F_btn_4")
        self.gridLayout_4.addWidget(self.F_btn_4, 2, 3, 1, 1)
        self.horizontalWidget3 = QtWidgets.QWidget(self.tab_friend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget3.sizePolicy().hasHeightForWidth())
        self.horizontalWidget3.setSizePolicy(sizePolicy)
        self.horizontalWidget3.setObjectName("horizontalWidget3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalWidget3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.F_prev_btn = QtWidgets.QPushButton(self.horizontalWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F_prev_btn.sizePolicy().hasHeightForWidth())
        self.F_prev_btn.setSizePolicy(sizePolicy)
        self.F_prev_btn.setObjectName("F_prev_btn")
        self.horizontalLayout_7.addWidget(self.F_prev_btn)
        self.F_page = QtWidgets.QLabel(self.horizontalWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F_page.sizePolicy().hasHeightForWidth())
        self.F_page.setSizePolicy(sizePolicy)
        self.F_page.setObjectName("F_page")
        self.horizontalLayout_7.addWidget(self.F_page)
        self.F_next_btn = QtWidgets.QPushButton(self.horizontalWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F_next_btn.sizePolicy().hasHeightForWidth())
        self.F_next_btn.setSizePolicy(sizePolicy)
        self.F_next_btn.setObjectName("F_next_btn")
        self.horizontalLayout_7.addWidget(self.F_next_btn)
        self.gridLayout_4.addWidget(self.horizontalWidget3, 6, 0, 1, 4)
        self.F_lineinput = QtWidgets.QLineEdit(self.tab_friend)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.F_lineinput.setFont(font)
        self.F_lineinput.setObjectName("F_lineinput")
        self.gridLayout_4.addWidget(self.F_lineinput, 0, 0, 1, 3)
        self.F_search_btn = QtWidgets.QPushButton(self.tab_friend)
        self.F_search_btn.setObjectName("F_search_btn")
        self.gridLayout_4.addWidget(self.F_search_btn, 0, 3, 1, 1)
        self.tabWidget.addTab(self.tab_friend, "")
        self.tab_profile = QtWidgets.QWidget()
        self.tab_profile.setObjectName("tab_profile")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_profile)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget4 = QtWidgets.QWidget(self.tab_profile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget4.sizePolicy().hasHeightForWidth())
        self.horizontalWidget4.setSizePolicy(sizePolicy)
        self.horizontalWidget4.setObjectName("horizontalWidget4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.P_addImageButton = QtWidgets.QPushButton(self.horizontalWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P_addImageButton.sizePolicy().hasHeightForWidth())
        self.P_addImageButton.setSizePolicy(sizePolicy)
        self.P_addImageButton.setObjectName("P_addImageButton")
        self.horizontalLayout_2.addWidget(self.P_addImageButton)
        self.P_logoutButton = QtWidgets.QPushButton(self.horizontalWidget4)
        self.P_logoutButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.P_logoutButton.setObjectName("P_logoutButton")
        self.horizontalLayout_2.addWidget(self.P_logoutButton)
        self.verticalLayout.addWidget(self.horizontalWidget4)
        self.gridWidget = QtWidgets.QWidget(self.tab_profile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setObjectName("gridWidget")
        self.profileGridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.profileGridLayout.setObjectName("profileGridLayout")
        self.P_img = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P_img.sizePolicy().hasHeightForWidth())
        self.P_img.setSizePolicy(sizePolicy)
        self.P_img.setAlignment(QtCore.Qt.AlignCenter)
        self.P_img.setObjectName("P_img")
        self.profileGridLayout.addWidget(self.P_img, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.P_img_caption = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P_img_caption.sizePolicy().hasHeightForWidth())
        self.P_img_caption.setSizePolicy(sizePolicy)
        self.P_img_caption.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.P_img_caption.setWordWrap(True)
        self.P_img_caption.setObjectName("P_img_caption")
        self.horizontalLayout_10.addWidget(self.P_img_caption)
        self.profileGridLayout.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.P_img_total_like = QtWidgets.QLabel(self.gridWidget)
        self.P_img_total_like.setObjectName("P_img_total_like")
        self.horizontalLayout_11.addWidget(self.P_img_total_like)
        self.profileGridLayout.addLayout(self.horizontalLayout_11, 4, 0, 1, 1)
        self.horizontalWidget5 = QtWidgets.QWidget(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget5.sizePolicy().hasHeightForWidth())
        self.horizontalWidget5.setSizePolicy(sizePolicy)
        self.horizontalWidget5.setObjectName("horizontalWidget5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.P_img_user = QtWidgets.QLabel(self.horizontalWidget5)
        self.P_img_user.setObjectName("P_img_user")
        self.horizontalLayout_4.addWidget(self.P_img_user)
        self.P_img_manage = QtWidgets.QPushButton(self.horizontalWidget5)
        self.P_img_manage.setObjectName("P_img_manage")
        self.horizontalLayout_4.addWidget(self.P_img_manage)
        self.profileGridLayout.addWidget(self.horizontalWidget5, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.gridWidget)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.tab_profile)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalWidget_2.sizePolicy().hasHeightForWidth())
        self.horizontalWidget_2.setSizePolicy(sizePolicy)
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.P_prev_btn = QtWidgets.QPushButton(self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P_prev_btn.sizePolicy().hasHeightForWidth())
        self.P_prev_btn.setSizePolicy(sizePolicy)
        self.P_prev_btn.setObjectName("P_prev_btn")
        self.horizontalLayout_3.addWidget(self.P_prev_btn)
        self.P_next_btn = QtWidgets.QPushButton(self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P_next_btn.sizePolicy().hasHeightForWidth())
        self.P_next_btn.setSizePolicy(sizePolicy)
        self.P_next_btn.setObjectName("P_next_btn")
        self.horizontalLayout_3.addWidget(self.P_next_btn)
        self.verticalLayout.addWidget(self.horizontalWidget_2)
        self.tabWidget.addTab(self.tab_profile, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        AppMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AppMainWindow)
        self.statusbar.setObjectName("statusbar")
        AppMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AppMainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AppMainWindow)

        self.P_logoutButton.clicked.connect(self.logout)

        self.userid = userid

        self.H_index = 0
        self.H_data = []
        self.P_index = 0
        self.P_data = []
        self.F_index = 0
        self.F_data = []

        self.widget = {
            'h': {
                'index': self.H_index,
                'data': self.H_data,
                'img': self.H_img,
                'owner': self.H_img_user,
                'caption': self.H_img_caption,
                'like': self.H_img_like,
                'nextbtn': self.H_next_btn,
                'prevbtn': self.H_prev_btn
            },
            'p': {
                'index': self.P_index,
                'data': self.P_data,
                'img': self.P_img,
                'owner': self.P_img_user,
                'caption': self.P_img_caption,
                'like': self.P_img_total_like,
                'nextbtn': self.P_next_btn,
                'prevbtn': self.P_prev_btn
            },
            'f': {
                'index': self.F_index,
                'data': self.F_data,
                'nameWidget': [self.F_text_1, self.F_text_2, self.F_text_3, self.F_text_4, self.F_text_5, self.F_text_6,
                               self.F_text_7, self.F_text_8],
                'addBtnwidget': [self.F_btn_1, self.F_btn_2, self.F_btn_3, self.F_btn_4, self.F_btn_5, self.F_btn_6,
                                 self.F_btn_7, self.F_btn_8],
                'nextbtn': self.F_next_btn,
                'prevbtn': self.F_prev_btn
            }
        }

        self.set_app_data()

        self.H_next_btn.clicked.connect(lambda: self.go_next_page('h'))
        self.H_prev_btn.clicked.connect(lambda: self.go_prev_page('h'))

        self.P_next_btn.clicked.connect(lambda: self.go_next_page('p'))
        self.P_prev_btn.clicked.connect(lambda: self.go_prev_page('p'))

        self.F_next_btn.clicked.connect(lambda: self.go_next_page('f'))
        self.F_prev_btn.clicked.connect(lambda: self.go_prev_page('f'))

        self.H_img_like_btn.clicked.connect(self.like_image)

        self.F_search_btn.clicked.connect(self.search_username)

        self.P_img_manage.clicked.connect(self.goManagePage)

        self.P_addImageButton.clicked.connect(self.goAddImagePage)

    def set_app_data(self):
        self.load_feed_data()

        self.widget['h']['prevbtn'].setEnabled(False)
        self.widget['h']['nextbtn'].setEnabled(False)
        self.render_image('h')

        self.widget['p']['prevbtn'].setEnabled(False)
        self.widget['p']['nextbtn'].setEnabled(False)
        self.render_image('p')

        print('set F')
        self.render_user_list()
        self.widget['f']['prevbtn'].setEnabled(False)
        self.widget['f']['nextbtn'].setEnabled(False)
        self.render_pagenum()

    def load_feed_data(self):
        self.widget['h']['data'] = project_library.get_feed_image_data(self.userid)
        self.load_profile_data()

    def load_profile_data(self):
        print('load P')
        self.widget['p']['data'] = []
        for x in self.widget['h']['data']:
            if x['owner'] == self.userid:
                self.widget['p']['data'].append(x)
        print(self.widget['p']['data'])
        # self.widget['p']['data'] = project_library.get_all_user_image_data(userid)

    def render_image(self, page):
        _index = self.widget[page]['index']
        if len(self.widget[page]['data']) > 0:
            pm = QtGui.QPixmap()
            pm.loadFromData(project_library.getImage(self.widget[page]['data'][_index]['imagestr']))
            self.widget[page]['img'].setPixmap(pm)
            self.widget[page]['owner'].setText(
                '<b>{}</b>'.format(project_library.getOwnerName(self.widget[page]['data'][_index]['owner'])))
            self.widget[page]['caption'].setText(self.widget[page]['data'][_index]['caption'])
            self.widget[page]['like'].setText('{} LIKES'.format(self.widget[page]['data'][_index]['like']))
            print(f"last {page}: {self.check_last(page)} = bc: {self.widget[page]['index']}")
            print(f"first {page}: {self.check_first(page)}")
            self.widget[page]['prevbtn'].setEnabled(not self.check_first(page))
            self.widget[page]['nextbtn'].setEnabled(not self.check_last(page))

            if page == 'p':
                self.P_img_manage.show()
            elif page == 'h':
                self.H_img_like_btn.show()

        else:
            self.widget[page]['img'].setText("LET'S UPLOAD SOME\nXD")
            self.widget[page]['owner'].setText('')
            self.widget[page]['caption'].setText('')
            self.widget[page]['like'].setText('')
            self.widget[page]['prevbtn'].hide()
            self.widget[page]['nextbtn'].hide()
            if page == 'p':
                self.widget[page]['img'].setText("Upload Something\n;)")
                self.P_img_manage.hide()
            elif page == 'h':
                self.widget[page]['img'].setText("Follow someone\nor\nUpload Something\nXD")
                self.H_img_like_btn.hide()

    def render_user_list(self):
        listname = self.widget['f']['data']
        _start_index = self.widget['f']['index'] * 8
        _last_index = _start_index + 8
        print(_start_index)
        print(_last_index)
        print(len(listname))
        for i in range(_start_index, _last_index):
            _index = i - _start_index
            if len(listname) > i:
                _user_id = listname[i]['_id']
                self.widget['f']['nameWidget'][_index].setText(listname[i]['displayname'])
                if listname[i]['_id'] in project_library.get_user_friend(self.userid):
                    self.widget['f']['addBtnwidget'][_index].setText('Unfollow')
                    self.widget['f']['addBtnwidget'][_index].clicked.connect(
                        lambda checked, _id=listname[i]['_id'],
                               btn=self.widget['f']['addBtnwidget'][_index]: self.unfollowBtnClicked(_id, btn))
                else:
                    self.widget['f']['addBtnwidget'][_index].setText('Follow')
                    self.widget['f']['addBtnwidget'][_index].clicked.connect(
                        lambda checked, _id=listname[i]['_id'],
                               btn=self.widget['f']['addBtnwidget'][_index]: self.followBtnClicked(_id, btn))
                self.widget['f']['addBtnwidget'][_index].show()
            else:
                self.widget['f']['nameWidget'][_index].setText('')
                self.widget['f']['addBtnwidget'][_index].hide()

    def followBtnClicked(self, follower_id, btn):
        project_library.follow(self.userid, follower_id)
        btn.setText('Unfollow')
        btn.disconnect()
        btn.clicked.connect(
            lambda checked, uid=follower_id,
                   btn=btn: self.unfollowBtnClicked(uid, btn))
        self.load_feed_data()
        self.render_image('h')

    def unfollowBtnClicked(self, follower_id, btn):
        project_library.unfollow(self.userid, follower_id)
        btn.setText('Follow')
        btn.disconnect()
        btn.clicked.connect(
            lambda checked, uid=follower_id,
                   btn=btn: self.followBtnClicked(uid, btn))
        self.load_feed_data()
        self.render_image('h')

    def check_first(self, page):
        return self.widget[page]['index'] <= 0

    def check_last(self, page):
        if page == 'f':
            return self.widget[page]['index'] >= len(self.widget[page]['data']) / 8 - 1
        return self.widget[page]['index'] >= len(self.widget[page]['data']) - 1

    def go_next_page(self, page):
        self.widget[page]['index'] += 1
        # print(self.widget[page]['index'])

        if page != 'f':
            self.render_image(page)
        else:
            print('next')
            self.render_pagenum()
            self.render_user_list()

        if not self.widget[page]['prevbtn'].isEnabled():
            self.widget[page]['prevbtn'].setEnabled(True)
        if self.check_last(page):
            self.widget[page]['nextbtn'].setEnabled(False)

    def go_prev_page(self, page):
        self.widget[page]['index'] -= 1
        # print(self.widget[page]['index'])

        if page != 'f':
            self.render_image(page)
        else:
            print('next')
            self.render_pagenum()
            self.render_user_list()

        if not self.widget[page]['nextbtn'].isEnabled():
            self.widget[page]['nextbtn'].setEnabled(True)
        if self.check_first(page):
            self.widget[page]['prevbtn'].setEnabled(False)

    def render_pagenum(self):
        self.F_page.setText(f"{self.widget['f']['index'] + 1}")

    def search_username(self):
        print('search')
        self.widget['f']['index'] = 0
        self.widget['f']['data'] = project_library.get_user_by_word(self.F_lineinput.text(), self.userid)
        self.render_user_list()
        if len(self.widget['f']['data']) > 8:
            self.widget['f']['nextbtn'].setEnabled(True)

    # TODO: if already liked cant like again

    def like_image(self):
        img = self.widget['h']['data'][self.widget['h']['index']]
        project_library.like(img['_id'])

        self.load_feed_data()
        self.render_image('h')
        self.render_image('p')

    def logout(self):
        print('>> go to LoginPage')
        import loginpage
        self.window = QtWidgets.QMainWindow()
        self.ui = loginpage.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.AppMainWindow.hide()

    def goManagePage(self):
        print('>> go to ManagePage')
        img_data = self.widget['p']['data'][self.widget['p']['index']]
        img_id = img_data['_id']
        img_old_caption = img_data['caption']

        import manage_image_page
        self.window = QtWidgets.QMainWindow()
        self.ui = manage_image_page.Ui_MainWindow2()
        self.ui.setupUi(self.window, img_id, self, img_old_caption)
        self.window.show()
        # self.MainWindowUI.hide()

    def goAddImagePage(self):
        print('>> go to ManagePage')
        import add_image_page
        self.window = QtWidgets.QMainWindow()
        self.ui = add_image_page.Ui_MainWindow()
        self.ui.setupUi(self.window, self)
        self.window.show()

    def refresh(self):
        self.load_feed_data()
        self.render_image('h')
        self.render_image('p')

    def retranslateUi(self, AppMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AppMainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.H_img.setText(_translate("MainWindow", "Follow someone\nor\nUpload Something\nXD"))
        self.H_img_like_btn.setText(_translate("MainWindow", "like"))
        self.H_prev_btn.setText(_translate("MainWindow", "prev"))
        self.H_next_btn.setText(_translate("MainWindow", "next"))
        self.H_img_user.setText(_translate("MainWindow", "USR"))
        self.H_img_like.setText(_translate("MainWindow", "17 Likes"))
        self.H_img_caption.setText(_translate("MainWindow", "Caption"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_feed), _translate("MainWindow", "Home"))
        self.F_text_4.setText(_translate("MainWindow", "4TextLabel"))
        self.F_btn_3.setText(_translate("MainWindow", "3Add"))
        self.F_text_3.setText(_translate("MainWindow", "3TextLabel"))
        self.F_btn_1.setText(_translate("MainWindow", "1Add"))
        self.F_btn_6.setText(_translate("MainWindow", "6Add"))
        self.F_text_8.setText(_translate("MainWindow", "8TextLabel"))
        self.F_btn_2.setText(_translate("MainWindow", "2Add"))
        self.F_text_5.setText(_translate("MainWindow", "5TextLabel"))
        self.F_text_6.setText(_translate("MainWindow", "6TextLabel"))
        self.F_text_1.setText(_translate("MainWindow", "01TextLabel"))
        self.F_text_7.setText(_translate("MainWindow", "7TextLabel"))
        self.F_btn_8.setText(_translate("MainWindow", "8Add"))
        self.F_btn_7.setText(_translate("MainWindow", "7Add"))
        self.F_btn_5.setText(_translate("MainWindow", "5Add"))
        self.F_text_2.setText(_translate("MainWindow", "2TextLabel"))
        self.F_btn_4.setText(_translate("MainWindow", "4Add"))
        self.F_prev_btn.setText(_translate("MainWindow", "Prev"))
        self.F_page.setText(_translate("MainWindow", "TextLabel"))
        self.F_next_btn.setText(_translate("MainWindow", "Next"))
        self.F_lineinput.setPlaceholderText(_translate("MainWindow", " Type Username Here"))
        self.F_search_btn.setText(_translate("MainWindow", "search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_friend), _translate("MainWindow", "Friend"))
        self.P_addImageButton.setText(_translate("MainWindow", "Add Image"))
        self.P_logoutButton.setText(_translate("MainWindow", "logout"))
        self.P_img.setText(_translate("MainWindow", "Upload Something\nXD"))
        self.P_img_caption.setText(_translate("MainWindow", "Caption"))
        self.P_img_total_like.setText(_translate("MainWindow", "total Like"))
        self.P_img_user.setText(_translate("MainWindow", "USR1"))
        self.P_img_manage.setText(_translate("MainWindow", "Manage"))
        self.P_prev_btn.setText(_translate("MainWindow", "Prev"))
        self.P_next_btn.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_profile), _translate("MainWindow", "Profile"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AppMainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(AppMainWindow)
    AppMainWindow.show()
    sys.exit(app.exec_())

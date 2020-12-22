# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QQ.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from socket import *
import chatroom_ui
import personal_ui
from Dialog_add import Ui_Dialog
import sys

'''groupchat_ui = QtWidgets.QWidget()
ui2 = chatroom_ui.Ui_MainWindow()
ui2.setupUi(groupchat_ui)
'''

'''personalchat_ui = QtWidgets.QWidget()
ui3 = personal_ui.Ui_Dialog()
ui3.setupUi(personalchat_ui)'''

menu_ui = QtWidgets.QWidget()
ui4 = Ui_Dialog()
ui4.setupUi(menu_ui)

class Ui_MainWindowt(object):

    def __init__(self, s):
        self.s =s
        self.buffsize = 1024

    def setupUit(self, MainWindow):
        self.MainWindow=MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(326, 627)
        self.MainWindow.setMinimumSize(QtCore.QSize(326, 627))
        self.MainWindow.setMaximumSize(QtCore.QSize(326, 627))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/QQ1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 331, 141))
        self.frame.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(120, 30, 70, 65))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-image:url(image/qq.jpeg)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(125, 100, 91, 21))
        self.label.setStyleSheet("background-color: rgb(85, 255, 255);\n""color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(294, 0, 31, 23))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 0, 31, 23))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 140, 326, 35))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(0, 2, 163, 35))
        self.pushButton.setStyleSheet("background-color: rgb(255, 239, 239);")
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 2, 171, 35))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 248, 248);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/wechat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 171, 331, 451))
        self.listWidget.setIconSize(QtCore.QSize(45, 45))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/信息论群头像.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/通信原理群头像.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/通信电子线路群头像.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/微机原理群头像.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.listWidget.addItem(item)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(-3, 171, 331, 441))
        self.treeWidget.setAutoScrollMargin(10)
        self.treeWidget.setIconSize(QtCore.QSize(40, 40))
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setIndentation(6)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setToolTip(0, "")
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_1.setFont(0, font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/头像1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon6)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("image/头像2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon7)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("image/头像3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon8)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_1.setFont(0, font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("image/头像4.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon9)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("image/头像5.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon10)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("image/头像6.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon11)

        #self.setCentralWidget(self.treeWidget)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.menuevent)
        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.listWidget.hide)
        self.pushButton_2.clicked.connect(self.listWidget.show)
        self.pushButton.clicked.connect(self.treeWidget.show)
        self.pushButton_2.clicked.connect(self.treeWidget.hide)
        self.pushButton_4.clicked.connect(MainWindow.showMinimized)

        self.listWidget.itemClicked.connect(self.group_req)
        self.treeWidget.itemClicked.connect(self.personal)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "QQ"))
        self.label.setText(_translate("MainWindow", "2097557613"))
        self.pushButton_3.setText(_translate("MainWindow", "关闭"))
        self.pushButton_4.setText(_translate("MainWindow", "隐藏"))
        self.pushButton.setText(_translate("MainWindow", "好友"))
        self.pushButton_2.setText(_translate("MainWindow", "群聊"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)  # 不排序
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "信息论群"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "通信原理群"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "通信电子线路群"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "微机原理群"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "好友列表"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "朋友"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "201813347"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "201813348"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "201813349"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "家人"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "201813350"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "同学"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "201813351"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "好友"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "201813352"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    def group_req(self, item):
        self.grouptitle=item.text()
        print(item.text())
        self.user = self.label.text()
        group_chat=['wechat_req']
        group_chat.append(self.grouptitle)
        group_chat.append(self.user)
        group_chat = '$%'.join(group_chat)
        self.s.send(group_chat.encode())
        self.group_setup(item)

    def group_setup(self, item):
        self.grouptitle = item.text()
        self.user = self.label.text()

        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/QQ1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        item.setText(str(self.user))

        groupchat_ui = QtWidgets.QWidget()
        ui2 = chatroom_ui.Ui_MainWindow(self.s, self.grouptitle, self.user)
        ui2.setupUi(groupchat_ui)

        groupchat_ui.show()
        ui2.textBrowser.clear()
        ui2.label_2.setText(self.grouptitle)

        ui2.recv_thead()
        ui2.dj_send()
        ui2.dj_quit(groupchat_ui)

    def personal(self, item):
        self.user = self.label.text()
        self.personaltitle = item.text(0)
        if self.personaltitle!='朋友' and self.personaltitle!='同学' and self.personaltitle!='家人' and self.personaltitle!='好友':


            personalchat_ui = QtWidgets.QWidget()
            ui3 = personal_ui.Ui_Dialog(self.s, self.user, self.personaltitle)
            ui3.setupUi(personalchat_ui)
            personalchat_ui.show()

            ui3.label.setText(self.personaltitle)
            print('my title is: '+self.personaltitle)
            ui3.pel_recv()
            ui3.pel_send()
            ui3.voice_chat()
            ui3.file_send()
            ui3.voice_chat_down()
            ui3.quit_window(personalchat_ui)
            ui3.textBrowser.clear()

    def menuevent(self):
        self.treetext = self.treeWidget.currentItem().text(0)

        if self.treetext == '同学' or self.treetext == '朋友' or self.treetext == '家人' or self.treetext == '好友' or str(self.treetext).isdigit()==False:

            pmenu1 = QtWidgets.QMenu(self.MainWindow)
            AddGroupAct = QtWidgets.QAction("添加分组", pmenu1)
            pmenu1.addAction(AddGroupAct)
            AddGroupAct.triggered.connect(self.addgroup)

            insertm = QtWidgets.QAction("添加好友", pmenu1)
            pmenu1.addAction(insertm)
            insertm.triggered.connect(self.addfriend)
            pmenu1.exec_(QtGui.QCursor.pos())
        else:
            pmenu2 = QtWidgets.QMenu(self.MainWindow)
            deletem = QtWidgets.QAction("删除", pmenu2)
            pmenu2.addAction(deletem)
            deletem.triggered.connect(self.deletefriend)

            pSubMenu = QtWidgets.QMenu("转移联系人至", pmenu2)
            pm1 = QtWidgets.QAction("朋友", pSubMenu)
            pSubMenu.addAction(pm1)
            pm1.triggered.connect(self.movefriend)
            pm2 = QtWidgets.QAction("家人", pSubMenu)
            pSubMenu.addAction(pm2)
            pm2.triggered.connect(self.movefriend)
            pm3 = QtWidgets.QAction("同学", pSubMenu)
            pSubMenu.addAction(pm3)
            pm3.triggered.connect(self.movefriend)
            pm4 = QtWidgets.QAction("好友", pSubMenu)
            pSubMenu.addAction(pm4)
            pm4.triggered.connect(self.movefriend)
            pmenu2.addMenu(pSubMenu)
            pmenu2.exec_(QtGui.QCursor.pos())

    def addgroup(self):
        menu_ui.show()
        menu_ui.setWindowTitle("添加分组")
        ui4.label.setText("新组名：")

        def gettext():
            groupname = ui4.lineEdit.text()
            if groupname != '':
                root5 = QtWidgets.QTreeWidgetItem(self.treeWidget)
                root5.setText(0, groupname)
                self.treeWidget.addTopLevelItem(root5)
                menu_ui.close()
            else:
                QtWidgets.QMessageBox.information(self.MainWindow, '提示', '组名不能为空!', QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close,
                                                  QtWidgets.QMessageBox.Close)

        ui4.pushButton.clicked.connect(gettext)

    def addfriend(self):
        selectroot = self.treeWidget.currentItem()
        menu_ui.show()
        menu_ui.setWindowTitle("添加好友")
        ui4.label.setText("好友名：")

        def gettext():
            groupname = ui4.lineEdit.text()
            if groupname != '':
                root5 = QtWidgets.QTreeWidgetItem(selectroot)
                root5.setText(0, groupname)
                font = QtGui.QFont()
                font.setPointSize(10)
                root5.setFont(0, font)
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap("image/chatbk.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                root5.setIcon(0, icon6)
                menu_ui.close()
            else:
                QtWidgets.QMessageBox.information(self.MainWindow, '提示', '好友名不能为空!', QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close,
                                                  QtWidgets.QMessageBox.Close)

        ui4.pushButton.clicked.connect(gettext)

    def deletefriend(self):
        self.treeWidget.currentItem().setText(0, ' ')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(""), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.currentItem().setIcon(0, icon)

    def movefriend(self):
        pass






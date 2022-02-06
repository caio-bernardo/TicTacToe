# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\maria\OneDrive\Documentos\MeusProjetos\TicTacToe\game\interface\game_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from interface.rcc import resource
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(545, 703)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/tic_tac_toe_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.start_page = QtWidgets.QWidget()
        self.start_page.setObjectName("start_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.start_page)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(self.start_page)
        self.title_label.setMinimumSize(QtCore.QSize(0, 90))
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 2000000))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.frame_2 = QtWidgets.QFrame(self.start_page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.img_label = QtWidgets.QLabel(self.frame_2)
        self.img_label.setEnabled(True)
        self.img_label.setMaximumSize(QtCore.QSize(502, 300))
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap(":/resources/Jogo_da_velha_-_tic_tac_toe.png"))
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.img_label.setObjectName("img_label")
        self.verticalLayout_4.addWidget(self.img_label)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame = QtWidgets.QFrame(self.start_page)
        self.frame.setMinimumSize(QtCore.QSize(0, 250))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 11, 0, 11)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_1p = QtWidgets.QPushButton(self.frame)
        self.btn_1p.setMinimumSize(QtCore.QSize(300, 50))
        self.btn_1p.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn_1p.setFont(font)
        self.btn_1p.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_1p.setStyleSheet("QPushButton{\n"
"border-color: rgb(66, 66, 66);\n"
"border: 2px solid;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(56, 209, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-color: rgb(16, 244, 255);\n"
"background-color: rgb(6, 135, 255);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.btn_1p.setObjectName("btn_1p")
        self.verticalLayout_2.addWidget(self.btn_1p)
        self.btn_2p = QtWidgets.QPushButton(self.frame)
        self.btn_2p.setMinimumSize(QtCore.QSize(300, 50))
        self.btn_2p.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_2p.setFont(font)
        self.btn_2p.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_2p.setStyleSheet("QPushButton{\n"
"border-color: rgb(66, 66, 66);\n"
"border: 2px solid;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(56, 209, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-color: rgb(16, 244, 255);\n"
"background-color: rgb(6, 135, 255);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.btn_2p.setObjectName("btn_2p")
        self.verticalLayout_2.addWidget(self.btn_2p)
        self.btn_exit = QtWidgets.QPushButton(self.frame)
        self.btn_exit.setMinimumSize(QtCore.QSize(300, 50))
        self.btn_exit.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setStyleSheet("QPushButton{\n"
"border-color: rgb(66, 66, 66);\n"
"border: 2px solid;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(56, 209, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border-color: rgb(16, 244, 255);\n"
"background-color: rgb(6, 135, 255);\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.btn_exit.setFlat(False)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout_2.addWidget(self.btn_exit)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.start_page)
        self.board_page = QtWidgets.QWidget()
        self.board_page.setObjectName("board_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.board_page)
        self.verticalLayout_6.setContentsMargins(11, 0, 11, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.board_page)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.crrnt_ply_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.crrnt_ply_label.setFont(font)
        self.crrnt_ply_label.setAlignment(QtCore.Qt.AlignCenter)
        self.crrnt_ply_label.setObjectName("crrnt_ply_label")
        self.horizontalLayout.addWidget(self.crrnt_ply_label)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_grid8 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_grid8.sizePolicy().hasHeightForWidth())
        self.btn_grid8.setSizePolicy(sizePolicy)
        self.btn_grid8.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_grid8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_grid8.setFont(font)
        self.btn_grid8.setStyleSheet("background-color: rgb(241, 241, 241)")
        self.btn_grid8.setText("")
        self.btn_grid8.setObjectName("btn_grid8")
        self.gridLayout.addWidget(self.btn_grid8, 4, 2, 1, 1)
        self.btn_grid9 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_grid9.sizePolicy().hasHeightForWidth())
        self.btn_grid9.setSizePolicy(sizePolicy)
        self.btn_grid9.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_grid9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_grid9.setFont(font)
        self.btn_grid9.setStyleSheet("background-color: rgb(241, 241, 241)")
        self.btn_grid9.setText("")
        self.btn_grid9.setObjectName("btn_grid9")
        self.gridLayout.addWidget(self.btn_grid9, 4, 3, 1, 1)
        self.btn_grid4 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_grid4.sizePolicy().hasHeightForWidth())
        self.btn_grid4.setSizePolicy(sizePolicy)
        self.btn_grid4.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_grid4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_grid4.setFont(font)
        self.btn_grid4.setStyleSheet("background-color: rgb(241, 241, 241)")
        self.btn_grid4.setText("")
        self.btn_grid4.setObjectName("btn_grid4")
        self.gridLayout.addWidget(self.btn_grid4, 2, 0, 1, 1)
        self.btn_grid5 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_grid5.sizePolicy().hasHeightForWidth())
        self.btn_grid5.setSizePolicy(sizePolicy)
        self.btn_grid5.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_grid5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_grid5.setFont(font)
        self.btn_grid5.setStyleSheet("background-color: rgb(241, 241, 241)")
        self.btn_grid5.setText("")
        self.btn_grid5.setObjectName("btn_grid5")
        self.gridLayout.addWidget(self.btn_grid5, 2, 2, 1, 1)
        self.btn_grid7 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_grid7.sizePolicy().hasHeightForWidth())
        self.btn_grid7.setSizePolicy(sizePolicy)
        self.btn_grid7.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_grid7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_grid7.setFont(font)
        self.btn_grid7.setStyleSheet("background-color: rgb(241, 241, 241)")
        self.btn_grid7.setText("")
        self.btn_grid7.setObjectName("btn_grid7")
        self.gridLayout.addWidget(self.btn_grid7, 4, 0, 1, 1)
        self.btn_grid1 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_grid1.sizePolicy().hasHeightForWidth())
        self.btn_grid1.setSizePolicy(sizePolicy)
        self.btn_grid1.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_grid1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_grid1.setFont(font)
        self.btn_grid1.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.btn_grid1.setText("")
        self.btn_grid1.setCheckable(False)
        self.btn_grid1.setAutoExclusive(False)
        self.btn_grid1.setObjectName("btn_grid1")
        self.gridLayout.addWidget(self.btn_grid1, 0, 0, 1, 1)
        self.btn_grid2 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_grid2.sizePolicy().hasHeightForWidth())
        self.btn_grid2.setSizePolicy(sizePolicy)
        self.btn_grid2.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_grid2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_grid2.setFont(font)
        self.btn_grid2.setStyleSheet("background-color: rgb(241, 241, 241);")
        self.btn_grid2.setText("")
        self.btn_grid2.setObjectName("btn_grid2")
        self.gridLayout.addWidget(self.btn_grid2, 0, 2, 1, 1)
        self.btn_grid3 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_grid3.sizePolicy().hasHeightForWidth())
        self.btn_grid3.setSizePolicy(sizePolicy)
        self.btn_grid3.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_grid3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_grid3.setFont(font)
        self.btn_grid3.setStyleSheet("background-color: rgb(241, 241, 241)")
        self.btn_grid3.setText("")
        self.btn_grid3.setObjectName("btn_grid3")
        self.gridLayout.addWidget(self.btn_grid3, 0, 3, 1, 1)
        self.btn_grid6 = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_grid6.sizePolicy().hasHeightForWidth())
        self.btn_grid6.setSizePolicy(sizePolicy)
        self.btn_grid6.setMinimumSize(QtCore.QSize(100, 100))
        self.btn_grid6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_grid6.setFont(font)
        self.btn_grid6.setStyleSheet("background-color: rgb(241, 241, 241)")
        self.btn_grid6.setText("")
        self.btn_grid6.setObjectName("btn_grid6")
        self.gridLayout.addWidget(self.btn_grid6, 2, 3, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.stackedWidget.addWidget(self.board_page)
        self.result_page = QtWidgets.QWidget()
        self.result_page.setObjectName("result_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.result_page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.result_page)
        self.frame_6.setMaximumSize(QtCore.QSize(545, 676))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.result_label = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(25)
        self.result_label.setFont(font)
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName("result_label")
        self.verticalLayout_8.addWidget(self.result_label)
        self.result_img_label = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_img_label.sizePolicy().hasHeightForWidth())
        self.result_img_label.setSizePolicy(sizePolicy)
        self.result_img_label.setMaximumSize(QtCore.QSize(523, 449))
        self.result_img_label.setText("")
        self.result_img_label.setPixmap(QtGui.QPixmap(":/resources/tie_game.png"))
        self.result_img_label.setScaledContents(True)
        self.result_img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_img_label.setObjectName("result_img_label")
        self.verticalLayout_8.addWidget(self.result_img_label)
        self.btn_return_2_main = QtWidgets.QCommandLinkButton(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.btn_return_2_main.setFont(font)
        self.btn_return_2_main.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_return_2_main.setIconSize(QtCore.QSize(50, 50))
        self.btn_return_2_main.setDescription("")
        self.btn_return_2_main.setObjectName("btn_return_2_main")
        self.verticalLayout_8.addWidget(self.btn_return_2_main)
        self.verticalLayout_7.addWidget(self.frame_6, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.result_page)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.bottom_label = QtWidgets.QLabel(self.centralwidget)
        self.bottom_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.bottom_label.setFont(font)
        self.bottom_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bottom_label.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.bottom_label.setText("")
        self.bottom_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bottom_label.setIndent(10)
        self.bottom_label.setObjectName("bottom_label")
        self.verticalLayout_3.addWidget(self.bottom_label)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe"))
        self.title_label.setText(_translate("MainWindow", "Tic Tac Toe"))
        self.btn_1p.setText(_translate("MainWindow", "Single Player"))
        self.btn_1p.setShortcut(_translate("MainWindow", "Return"))
        self.btn_2p.setText(_translate("MainWindow", "Two Players"))
        self.btn_2p.setShortcut(_translate("MainWindow", "Return"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        self.btn_exit.setShortcut(_translate("MainWindow", "Esc"))
        self.label_2.setText(_translate("MainWindow", "Current Player:"))
        self.crrnt_ply_label.setText(_translate("MainWindow", "Player 1"))
        self.label.setText(_translate("MainWindow", "RESULTS"))
        self.result_label.setText(_translate("MainWindow", "Tie Game"))
        self.btn_return_2_main.setText(_translate("MainWindow", "Go Back to Main Page"))

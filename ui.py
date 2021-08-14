# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calcrDsdQr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(276, 302)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txtResult = QLineEdit(self.centralwidget)
        self.txtResult.setObjectName(u"txtResult")

        self.verticalLayout.addWidget(self.txtResult)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setMinimumSize(QSize(61, 51))
        self.btn1.setMaximumSize(QSize(61, 51))
        self.btn1.setText(u"1")

        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)

        self.btn4 = QPushButton(self.centralwidget)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setMinimumSize(QSize(61, 51))
        self.btn4.setMaximumSize(QSize(61, 51))
        self.btn4.setText(u"4")

        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)

        self.btn5 = QPushButton(self.centralwidget)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setMinimumSize(QSize(61, 51))
        self.btn5.setMaximumSize(QSize(61, 51))
        self.btn5.setText(u"5")

        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)

        self.btn8 = QPushButton(self.centralwidget)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setMinimumSize(QSize(61, 51))
        self.btn8.setMaximumSize(QSize(61, 51))
        self.btn8.setText(u"8")

        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)

        self.btnPlus = QPushButton(self.centralwidget)
        self.btnPlus.setObjectName(u"btnPlus")
        self.btnPlus.setMinimumSize(QSize(61, 51))
        self.btnPlus.setMaximumSize(QSize(61, 51))
        self.btnPlus.setText(u"+")

        self.gridLayout.addWidget(self.btnPlus, 3, 3, 1, 1)

        self.btn3 = QPushButton(self.centralwidget)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setMinimumSize(QSize(61, 51))
        self.btn3.setMaximumSize(QSize(61, 51))
        self.btn3.setText(u"3")

        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)

        self.btn2 = QPushButton(self.centralwidget)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setMinimumSize(QSize(61, 51))
        self.btn2.setMaximumSize(QSize(61, 51))
        self.btn2.setText(u"2")

        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)

        self.btn9 = QPushButton(self.centralwidget)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setMinimumSize(QSize(61, 51))
        self.btn9.setMaximumSize(QSize(61, 51))
        self.btn9.setText(u"9")

        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)

        self.btnMinus = QPushButton(self.centralwidget)
        self.btnMinus.setObjectName(u"btnMinus")
        self.btnMinus.setMinimumSize(QSize(61, 51))
        self.btnMinus.setMaximumSize(QSize(61, 51))
        self.btnMinus.setText(u"-")

        self.gridLayout.addWidget(self.btnMinus, 2, 3, 1, 1)

        self.btnClear = QPushButton(self.centralwidget)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setMinimumSize(QSize(61, 51))
        self.btnClear.setMaximumSize(QSize(61, 51))
        self.btnClear.setText(u"C")

        self.gridLayout.addWidget(self.btnClear, 3, 0, 1, 1)

        self.btnDivide = QPushButton(self.centralwidget)
        self.btnDivide.setObjectName(u"btnDivide")
        self.btnDivide.setMinimumSize(QSize(61, 51))
        self.btnDivide.setMaximumSize(QSize(61, 51))
        self.btnDivide.setText(u"/")

        self.gridLayout.addWidget(self.btnDivide, 0, 3, 1, 1)

        self.btn6 = QPushButton(self.centralwidget)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setMinimumSize(QSize(61, 51))
        self.btn6.setMaximumSize(QSize(61, 51))
        self.btn6.setText(u"6")

        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)

        self.btn0 = QPushButton(self.centralwidget)
        self.btn0.setObjectName(u"btn0")
        self.btn0.setMinimumSize(QSize(61, 51))
        self.btn0.setMaximumSize(QSize(61, 51))
        self.btn0.setText(u"0")

        self.gridLayout.addWidget(self.btn0, 3, 1, 1, 1)

        self.btnEqual = QPushButton(self.centralwidget)
        self.btnEqual.setObjectName(u"btnEqual")
        self.btnEqual.setMinimumSize(QSize(61, 51))
        self.btnEqual.setMaximumSize(QSize(61, 51))
        self.btnEqual.setText(u"=")

        self.gridLayout.addWidget(self.btnEqual, 3, 2, 1, 1)

        self.btnMultiply = QPushButton(self.centralwidget)
        self.btnMultiply.setObjectName(u"btnMultiply")
        self.btnMultiply.setMinimumSize(QSize(61, 51))
        self.btnMultiply.setMaximumSize(QSize(61, 51))
        self.btnMultiply.setText(u"*")

        self.gridLayout.addWidget(self.btnMultiply, 1, 3, 1, 1)

        self.btn7 = QPushButton(self.centralwidget)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setMinimumSize(QSize(61, 51))
        self.btn7.setMaximumSize(QSize(61, 51))
        self.btn7.setText(u"7")

        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 276, 29))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi
 

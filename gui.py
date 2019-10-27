# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_IpF.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(344, 297)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(344, 297))
        MainWindow.setMaximumSize(QtCore.QSize(344, 297))
        MainWindow.setStyleSheet("QTableWidget {\n"
"    outline: 0;\n"
"}\n"
"QTableWidget::item:selected {background-color:transparent; border: 0px }\n"
"QTableWidget::item:focus { background-color:transparent;  border: 0px }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(3, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = MyTable(self.centralwidget)
        self.tableWidget.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);\n"
"")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_nomePc = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_nomePc.setObjectName("comboBox_nomePc")
        self.horizontalLayout.addWidget(self.comboBox_nomePc)
        self.bot_cerca = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bot_cerca.sizePolicy().hasHeightForWidth())
        self.bot_cerca.setSizePolicy(sizePolicy)
        self.bot_cerca.setObjectName("bot_cerca")
        self.horizontalLayout.addWidget(self.bot_cerca)
        self.bot_esci = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bot_esci.sizePolicy().hasHeightForWidth())
        self.bot_esci.setSizePolicy(sizePolicy)
        self.bot_esci.setStyleSheet("")
        self.bot_esci.setObjectName("bot_esci")
        self.horizontalLayout.addWidget(self.bot_esci)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.spinnerWidget = QtWidgets.QWidget(self.centralwidget)
        self.spinnerWidget.setStyleSheet("/*background-color: rgb(255, 255, 0);*/")
        self.spinnerWidget.setObjectName("spinnerWidget")
        self.horizontalLayout_2.addWidget(self.spinnerWidget)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 344, 21))
        self.menubar.setObjectName("menubar")
        self.menuImpostazioni = QtWidgets.QMenu(self.menubar)
        self.menuImpostazioni.setObjectName("menuImpostazioni")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGenerale = QtWidgets.QAction(MainWindow)
        self.actionGenerale.setObjectName("actionGenerale")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuImpostazioni.addAction(self.actionGenerale)
        self.menuImpostazioni.addSeparator()
        self.menuImpostazioni.addAction(self.actionAbout)
        self.menubar.addAction(self.menuImpostazioni.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IpFinder"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "WelCome!"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.bot_cerca.setText(_translate("MainWindow", "Cerca"))
        self.bot_esci.setText(_translate("MainWindow", "Esci"))
        self.menuImpostazioni.setTitle(_translate("MainWindow", "Impostazioni"))
        self.actionGenerale.setText(_translate("MainWindow", "Generale"))
        self.actionAbout.setText(_translate("MainWindow", "About..."))
from mytable import MyTable


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

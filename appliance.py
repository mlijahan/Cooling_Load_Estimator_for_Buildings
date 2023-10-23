

from PyQt6 import QtCore, QtGui, QtWidgets
import numpy as np


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setMinimumSize(QtCore.QSize(640, 480))
        Dialog.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("srcs/oven_6301569.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(75, 100, 491, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.line = QtWidgets.QFrame(parent=Dialog)
        self.line.setGeometry(QtCore.QRect(0, 70, 641, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(500, 420, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 422, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(230, 30, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 28, 131, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 26, 71, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(360, 27, 161, 24))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(13, 430, 141, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 426, 81, 24))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_6 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 420, 121, 31))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def total_apps(self):
        self.appswat = []
        self.ROW = self.tableWidget.rowCount()
        for row in range(self.ROW):
            self.appswat.append(float(self.tableWidget.item(row, 3).text()))
        self.total_appwat = sum(self.appswat)
        return np.round(self.total_appwat,2)

    def delete_row_app(self):
        self.ROW = self.tableWidget.rowCount()
        for row in range(self.ROW+1):
            self.tableWidget.removeRow(row)

    def delete_total_totalapp(self):
        self.lineEdit_2.clear()
        self.comboBox.setCurrentIndex(0)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Heat gain from appliances "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Appliance Type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Appliance Number"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Appliance total Watt"))
        self.pushButton.setText(_translate("Dialog", "Save"))
        self.pushButton_2.setText(_translate("Dialog", "Calculation"))
        self.label_3.setText(_translate("Dialog", "Select Light :"))
        self.pushButton_3.setText(_translate("Dialog", "Add New Appliance"))
        self.pushButton_4.setText(_translate("Dialog", "Add to List"))
        self.label_2.setText(_translate("Dialog", "Heat gain from Appliance :"))
        self.pushButton_6.setText(_translate("Dialog", "Clear"))




# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employee_search.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_empSearchDialog(object):
    def setupUi(self, empSearchDialog):
        empSearchDialog.setObjectName("empSearchDialog")
        empSearchDialog.resize(697, 296)
        empSearchDialog.setStyleSheet("background-color:rgb(170, 255, 255)")
        self.label = QtWidgets.QLabel(empSearchDialog)
        self.label.setGeometry(QtCore.QRect(270, 40, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(empSearchDialog)
        self.lineEdit.setGeometry(QtCore.QRect(150, 80, 431, 20))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(empSearchDialog)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 47, 13))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tableView = QtWidgets.QTableView(empSearchDialog)
        self.tableView.setGeometry(QtCore.QRect(60, 120, 551, 81))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(empSearchDialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 230, 75, 23))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(empSearchDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 230, 75, 23))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(empSearchDialog)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 230, 75, 23))
        font = QtGui.QFont()
        font.setFamily("System")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(empSearchDialog)
        QtCore.QMetaObject.connectSlotsByName(empSearchDialog)

    def retranslateUi(self, empSearchDialog):
        _translate = QtCore.QCoreApplication.translate
        empSearchDialog.setWindowTitle(_translate("empSearchDialog", "Employee Search Box"))
        self.label.setText(_translate("empSearchDialog", "Employee Search Box"))
        self.label_2.setText(_translate("empSearchDialog", "Search"))
        self.pushButton.setText(_translate("empSearchDialog", "Search"))
        self.pushButton_2.setText(_translate("empSearchDialog", "Use"))
        self.pushButton_3.setText(_translate("empSearchDialog", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    empSearchDialog = QtWidgets.QDialog()
    ui = Ui_empSearchDialog()
    ui.setupUi(empSearchDialog)
    empSearchDialog.show()
    sys.exit(app.exec_())


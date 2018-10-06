import sys
from signup import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView
from PyQt5 import QtSql
from PyQt5 import QtCore

class empr_form(Dialog):

    def __init__(self):
        super().__init__()
        self.signup = Ui_HRM_User_view()
        self.signup.setupUi(self)
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('hrm_users.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('users')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal,"id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "National ID")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Registration id")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Registration Date")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "First Name")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Middle Name")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Last Name")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "DOB")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "User Name")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Phone")
        self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Email")
        self.model.setHeaderData(11, QtCore.Qt.Horizontal, "Password")
        self.signup.tableWidget_records.setModel(self.model)
        self.signup.pushButton_reg.clicked.connect(self.addToDb)
        self.show()
        self.signup.pushButton_update.clicked.connect(self.updaterow)
        self.signup.pushButton_login.clicked.connect(self.welcomeWindowShow())
        self.signup.pushButton_delete.clicked.connect(self.delrow)
        self.i = self.model.rowCount()
        self.signup.lcdNumber_user_id.display(self.i)
        print(self.signup.tableWidget_records.currentIndex().row())

    def welcomeWindowShow(self):
        self.welcomeWindow = QMainWindow
        self.ui = Ui_HRM_User_view()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()

    def addToDb(self):
        import string
        import random

        # Just alphanumeric characters
        chars = string.alphabets + string.digits

        # Alphanumeric + special characters
        chars = string.digits + string.digits + string.punctuation

        pwdSize = 10

        print().join((random.choice(chars)) for x in range(pwdSize))
        print(self.i)
        self.model.insertRows(self.i,1)
        self.model.setData(self.model.index(self.i, 1), self.signup.lineEdit_IDNo.text())
        self.model.setData(self.model.index(self.i, 2), self.signup.lineEdit_regNo.text())
        self.model.setData(self.model.index(self.i, 3), self.signup.lineEdit_regDt.text())
        self.model.setData(self.model.index(self.i, 4), self.signup.lineEdit_fn.text())
        self.model.setData(self.model.index(self.i, 5), self.signup.lineEdit_mn.text())
        self.model.setData(self.model.index(self.i, 6), self.signup.lineEdit_ln.text())
        self.model.setData(self.model.index(self.i, 7), self.signup.dateEdit_dob.text())
        self.model.setData(self.model.index(self.i, 8), self.signup.lineEdit_tell.text())
        self.model.setData(self.model.index(self.i, 9), self.signup.lineEdit_email.text())
        self.model.setData(self.model.index(self.i, 10), self.signup.lineEdit_pswrd.text())
        self.model.submitAll()
        self.i += 1
        self.signup.lcdNumber_user_id.display(self.i)

    def delrow(self):
        if self.signup.tableWidget_records.currentIndex().row() > -1:
            self.model.removeRow(self.signup.tableWidget_records.currentIndex().row())
            self.i -= 1
            self.model.select()
            self.signup.lcdNumber_user_id.display(self.i)
        else:
            QMessageBox.question(self,'Message', "Please select a row would you like to delete", QMessageBox.Ok)
            self.show()

    def updaterow(self):
        if self.signup.tableWidget_records.currentIndex().row() > -1:
            record = self.model.record(self.signup.tableWidget_records.currentIndex().row())
            record.setValue("National ID", self.signup.lineEdit_IDNo.text())
            record.setValue("Registration ID", self.signup.lineEdit_regNo.text())
            record.setValue("Registration Date", self.signup.lineEdit_regDt.text())
            record.setValue("First Name", self.signup.lineEdit_fn.text())
            record.setValue("Middle Name", self.signup.lineEdit_mn.text())
            record.setValue("Last Name", self.signup.lineEdit_ln.text())
            record.setValue("DOB", self.signup.dateEdit_dob.text())
            record.setValue("User Name", self.signup.lineEdit_un.text())
            record.setValue("Phone", self.signup.lineEdit_tell.text())
            record.setValue("Email", self.signup.lineEdit_email.text())
            record.setValue("Password", self.signup.lineEdit_pswrd.text())
            self.model.setRecord(self.signup.tableWidget_records.currentIndex().row(), record)
        else:
            QMessageBox.question(self,'Message', "Please select a row would you like to update", QMessageBox.Ok)
            self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frm = empr_form()
    frm.showMaximized()
    sys.exit(app.exec_())

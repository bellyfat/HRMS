import sys
from signup import *
from admin_raw import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView, QMenuBar, QStatusBar, QDialog
from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui
import sqlite3



class RegForm(QDialog):
    def __init__(self):
        super().__init__()
        self.signup = Ui_HRM_Signup_view()
        self.signup.setupUi(self)
        self.show()

        self.signup.pushButton_signup.clicked.connect(self.create_account)
        self.signup.pushButton_back.clicked.connect(self.back_home)
        self.signup.pushButton_login.clicked.connect(self.login_user)

        menubar = QtWidgets.QMenuBar(self)
        menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        menubar.setObjectName("menubar")
        filemenu = menubar.addMenu("File")

        open = filemenu.addAction("Open")
        # actionFile.setTearOffEnabled(enabled)
        filemenu.addSeparator()
        filemenu.addAction("Quit")

        viewmenu = menubar.addMenu("View")
        editmenu = menubar.addMenu("Edit")
        searchmenu = menubar.addMenu("Search")
        toolmenu = menubar.addMenu("Tools")
        helpmenu = menubar.addMenu("Help")
        menubar.addMenu("Edit")
        menubar.addMenu("View")
        menubar.addMenu("Help")



    def create_table(self):

        try:
            conn = sqlite3.connect('database_hrm.db')
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS superusers(User_id INTEGER PRIMARY KEY AUTOINCREMENT,"
          " First_Name VARCHAR(20),"
          " Middle_Name VARCHAR,"
          " Last_Name VARCHAR,"
          " User_Name VARCHAR,"
          " Phone INTEGER,"
          " Email VARCHAR,"
          " Password VARCHAR,"
          " DOB VARCHAR,"
          " User_role VARCHAR,"
          " Gender VARCHAR)")

            QMessageBox.information(self, 'User', "Table Data created  Successfully", QMessageBox.Ok)
            conn.commit()
            c.close()
            conn.close()
            self.enter_data()
        except:
            self.enter_data()
            QMessageBox.information(self, 'Success', "Info Added Successfully !!!", QMessageBox.Ok)
            c.close()
            conn.close()

    def create_account(self):
        gender = None
        fn = self.signup.lineEdit_fn.text()
        mn = self.signup.lineEdit_mn.text()
        ln = self.signup.lineEdit_ln.text()
        un = self.signup.lineEdit_un.text()
        phone = self.signup.lineEdit_tell.text()
        email = self.signup.lineEdit_email.text()
        password = self.signup.lineEdit_pswrd.text()
        dob = self.signup.dateEdit_dob.text()
        urole = 'Administrator'

        if self.signup.radioButton_m.isChecked():
            gender = 'Male'
        if self.signup.radioButton_f.isChecked():
            gender = 'Female'

        print(fn, mn, ln, un, phone, email, password, dob, urole, gender)

        try:
            conn = sqlite3.connect('database_hrm.db')
            c = conn.cursor()

            c.execute("INSERT INTO superusers(First_Name, Middle_Name, Last_Name, User_Name, Phone, Email, Password, DOB, User_role, Gender)"
            "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(fn,mn,ln,un,phone,email,password,dob,urole,gender))

            conn.commit()
            c.close()
            conn.close()
        except ValueError:
            QMessageBox.information(self, 'Error', "Data Inserted  Not Success", QMessageBox.Ok)



    def clear1(self):
        self.signup.radioButton_m.isChecked(False)
        self.signup.radioButton_f.isChecked(False)
        self.signup.lineEdit_fn.setText('')
        self.signup.lineEdit_mn.setText('')
        self.signup.lineEdit_ln.setText('')
        self.signup.lineEdit_un.setText('')
        self.signup.lineEdit_tell.setText('')
        self.signup.lineEdit_email.setText('')
        self.signup.lineEdit_pswrd.setText('')
        self.signup.dateEdit_dob.setText('12/7/2018')



    def back_home(self):
        #self.exit_action = QtWidgets.qApp.quit()
        self.window = HRMForm(self)
        self.window.showMaximized()
        self.close(self)

    def login_user(self):
        self.close(self)
        self.window = HRMForm()
        self.window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frm = RegForm()
    frm.show()
    sys.exit(app.exec_())

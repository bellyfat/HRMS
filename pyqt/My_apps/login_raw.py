import sys
from login import *
from admin_raw import *
from signup_raw import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView, QStatusBar, QMenuBar, QStatusBar
from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui
import sqlite3

class LoginForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = Ui_HRM_Login_view()
        self.login.setupUi(self)
        self.show()

        self.login.pushButton_login.clicked.connect(self.login_user)
        self.login.pushButton_back.clicked.connect(self.back_home)
        self.login.pushButton_signup.clicked.connect(self.new_user)

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

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)




    def login_user(self):

        with sqlite3.connect('database_hrm.db') as db:
            c = db.cursor()

        un = self.login.lineEdit_un.text()
        password = self.login.lineEdit_pass.text()

        c.execute('SELECT * FROM superusers WHERE User_Name = ? and Password = ?', (un, password))
        data = c.fetchone()
        db.commit()
        if data != None:
            QMessageBox.information(self, 'Message', "Logged Successfully !!!", QMessageBox.Ok)
            self.back_home
        else:
            QMessageBox.information(self, 'Error', "No Account With That Username And Password", QMessageBox.Ok)



    def clear1(self):
        self.login.radioButton_m.isChecked(False)
        self.login.radioButton_f.isChecked(False)
        self.login.lineEdit_fn.setText('')
        self.login.lineEdit_mn.setText('')
        self.login.lineEdit_ln.setText('')
        self.login.lineEdit_un.setText('')
        self.login.lineEdit_tell.setText('')
        self.login.lineEdit_email.setText('')
        self.login.lineEdit_pswrd.setText('')
        self.login.dateEdit_dob.setText('12/7/2018')

    def back_home(self):
        self.window= None
        # self.exit_action = QtWidgets.qApp.quit()
        self.window = HRMForm()
        self.window.showMaximized()
        LoginForm.destroy(self)

    def new_user(self):
        HRMForm.destroy(self)
        self.window = RegForm()
        self.window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frm = LoginForm()
    frm.showMaximized()
    sys.exit(app.exec_())

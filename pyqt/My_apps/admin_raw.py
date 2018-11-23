import sys
from base import *
from EmployeeForm import *
from ClientForm import *
from WorkerForm import *
from signup_raw import *
from login import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView, QMenuBar, QStatusBar, QProgressBar, QDialog
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, pyqtSignal
import sqlite3
from functools import partial
import PyQt5.uic as uic
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter






###########################################################################################################################################
##############################################dashForm start##################################################################################
class HRMForm(QMainWindow):

    def __init__(self):
        super(HRMForm, self).__init__()
        self.dashboard = Ui_HRM_Dashboard_view()
        self.login = LoginDialog()

        self.dashboard.setupUi(self)

        #self.createProgressBar()

        self.dashboard.actionNewEmployee.triggered.connect(lambda:self.new_employee())
        self.dashboard.actionNewWorker.triggered.connect(lambda: self.new_worker())
        self.dashboard.actionNewClient.triggered.connect(lambda: self.new_client())
        self.dashboard.actionQiut_Application.triggered.connect(lambda: self.close())
        self.dashboard.pushButton_user_login.clicked.connect(lambda: self.login_user())
        self.dashboard.pushButton_user_reg.clicked.connect(lambda: self.new_user())

        self.dashboard.toolButton_print.clicked.connect(self.createPrintDialog)

        self.login.got_username.connect(self.show_it)


        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)



    def dashboardWindowShow(self):
        self.dashboardWindow = QMainWindow()
        self.ui = Ui_HRM_Dashboard_view()
        self.ui.setupUi(self.dashboardWindow)
        HRMForm.destroy(self)
        self.dashboardWindow.showMaximized()

        self.createProgressBar()

    def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.advanceProgressBar)
        timer.start(1000)

    def advanceProgressBar(self):
        curVal = self.progressBar.value()
        maxVal = self.progressBar.maximum()
        self.progressBar.setValue(curVal + (maxVal - curVal) / 100)


    def new_employee(self):
        HRMForm.close(self)
        self.window = EmployeeForm()
        self.window.showMaximized()

    def new_user(self):
        HRMForm.destroy(self)
        self.window = RegForm()
        self.window.show()


    def login_user(self):
        HRMForm.destroy(self)
        self.window = LoginDialog()
        self.window.show()

    def new_client(self):
        HRMForm.close(self)
        self.window = ClientForm()
        self.window.showMaximized()


    def new_worker(self):
        HRMForm.close(self)
        self.window = WorkerForm()
        self.window.showMaximized()


    def new_employer(self):
        HRM.destroy(self)
        UsersEmployer.show()


    def register_staff(self):
        HRM.destroy(self)
        UsersStaff()


    def show_it(self, the_username):
        self.dashboard.label_welcome_username.setText(the_username)


    def createPrintDialog(self):

        mylist =[]

        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.dashboard.label_welcome_username.print_(printer)


###########################################################################################################################################
##############################################dashForm end##################################################################################

class LoginDialog(QDialog, Ui_HRM_Login_view):

    got_username = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        QDialog.__init__(self, *args, **kwargs)
        self.login = Ui_HRM_Login_view()
        self.login.setupUi(self)



        self.login.pushButton_login.clicked.connect(lambda: self.login_check())




    def login_check(self):
        with sqlite3.connect('database_hrm.db') as db:
            c = db.cursor()

        self.un = self.login.lineEdit_un.text()
        password = self.login.lineEdit_pass.text()
        c.execute('SELECT * FROM superusers WHERE User_Name = ? and Password = ?', (self.un, password))
        data = c.fetchone()
        db.commit()
        if data!=None:
            QMessageBox.information(self, 'Message', "Logged Successfully !!!", QMessageBox.Ok)
            self.accept()
        else:
            QMessageBox.information(self, 'Error',
                                    "No Account With That Username And Password\nPlease check your Credatials",
                                    QMessageBox.Ok)

    def comfirm(self):

        self.value = self.login.lineEdit_un.text()
        self.got_username.emit(self.value)
        print (self.value)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginDialog()
    w = HRMForm()
    w.hide()
    if login.exec_() == QtWidgets.QDialog.Accepted:


        w.showMaximized()

    sys.exit(app.exec_())

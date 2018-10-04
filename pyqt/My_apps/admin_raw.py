import sys
from base import *
from EmployeeForm import *
from ClientForm import *
from WorkerForm import *
from signup_raw import *
from login_raw import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView, QMenuBar, QStatusBar, QProgressBar
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
import sqlite3






###########################################################################################################################################
##############################################dashForm start##################################################################################
class HRMForm(QMainWindow):

    def __init__(self):
        super().__init__()
        self.dashboard = Ui_HRM_Dashboard_view()

        self.dashboard.setupUi(self)

        self.createProgressBar()

        self.dashboard.actionNewEmployee.triggered.connect(lambda:self.new_employee())
        self.dashboard.actionNewWorker.triggered.connect(lambda: self.new_worker())
        self.dashboard.actionNewClient.triggered.connect(lambda: self.new_client())
        self.dashboard.pushButton_user_login.clicked.connect(lambda : self.login_user())
        self.dashboard.pushButton_user_reg.clicked.connect(lambda : self.new_user())

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.show()

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
        HRMForm.destroy(self)
        self.window = EmployeeForm()
        self.window.showMaximized()

    def new_user(self):
        HRMForm.destroy(self)
        self.window = RegForm()
        self.window.show()


    def login_user(self):
        HRMForm.destroy(self)
        self.window = LoginForm()
        self.window.show()

    def new_client(self):
        HRMForm.destroy(self)
        self.window = ClientForm()
        self.window.showMaximized()


    def new_worker(self):
        HRMForm.destroy(self)
        self.window = WorkerForm()
        self.window.showMaximized()


    def new_employer(self):
        HRM.destroy(self)
        UsersEmployer.show()


    def register_staff(self):
        HRM.destroy(self)
        UsersStaff()



###########################################################################################################################################
##############################################dashForm end##################################################################################


if __name__ == '__main__':
    app = QApplication(sys.argv)

    frm = HRMForm()
    frm.showMaximized()
    sys.exit(app.exec_())


import sys
from workers import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView, QMenuBar, QStatusBar
from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui
import sqlite3
from dashboard_raw import Ui_HRM_Dashboard_view


def db():
    with sqlite3.connect('database_hrm.dbconn') as dbconn:
        c = dbconn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS user_workers(User_id  INTEGER PRIMARY KEY AUTOINCREMENT,"
    "National_ID VARCHAR (20),"
    "Registration_Date   VARCHAR,"
    "Registration_Number VARCHAR (20),"
    "Worker_hrm_code VARCHAR (20),"
    "Company_Name VARCHAR (50),"
    "KRA_PIN VARCHAR (20),"
    "First_Name          VARCHAR (20),"
    "Middle_Name         VARCHAR (20),"
    "Last_Name           VARCHAR (20),"
    "Gender          VARCHAR (20),"
    "Phone               INTEGER (10),"
    "Email               VARCHAR (50),"
    "Address             VARCHAR (50),"
    "Experience_level           INTEGER(5),"
    "Skills          VARCHAR (20),"
    "Availability          VARCHAR (20),"
    "Employer          VARCHAR (20),"
    "Payment_Mode        VARCHAR (20),"
    "DOB          VARCHAR,"
    "User_role          VARCHAR (20))")

    dbconn.commit()
    c.close()
    dbconn.close()

class form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.workers = Ui_HRM_Workers_view()
        self.workers.setupUi(self)
        self.show()


        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database_hrm.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('user_workers')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal,"User_id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal,"National_ID")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal,"Registration_Date")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal,"Registration_Number")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal,"Worker_hrm_code")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal,"Company_Name")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal,"KRA_PIN")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal,"First_Name")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal,"Middle_Name")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal,"Last_Name")
        self.model.setHeaderData(10, QtCore.Qt.Horizontal,"Gender")
        self.model.setHeaderData(11, QtCore.Qt.Horizontal,"Phone")
        self.model.setHeaderData(12, QtCore.Qt.Horizontal,"Email")
        self.model.setHeaderData(13, QtCore.Qt.Horizontal,"Address")
        self.model.setHeaderData(14, QtCore.Qt.Horizontal,"Experience_level")
        self.model.setHeaderData(15, QtCore.Qt.Horizontal,"Skills")
        self.model.setHeaderData(16, QtCore.Qt.Horizontal,"Availability")
        self.model.setHeaderData(17, QtCore.Qt.Horizontal,"Employer")
        self.model.setHeaderData(18, QtCore.Qt.Horizontal,"Payment_Mode")
        self.model.setHeaderData(19, QtCore.Qt.Horizontal,"DOB")
        self.model.setHeaderData(20, QtCore.Qt.Horizontal,"User_role")
        self.workers.tableWidget_records.setModel(self.model)
        self.i = self.model.rowCount()
        self.workers.lcdNumber_user_id.display(self.i)
        
        self.workers.pushButton_reg.clicked.connect(self.addToDb)
        self.workers.pushButton_back.clicked.connect(self.dashboardWindowShow)

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

    def addToDb(self):

        nid = self.workers.lineEdit_IDNo.text()
        reg_date = self.workers.dateTimeEdit_stamp.text()
        reg_no = self.workers.lineEdit_regNo.text()
        hrm_code = self.workers.lineEdit_hrm_code.text()
        kra = self.workers.lineEdit_kra_pin.text()
        fn = self.workers.lineEdit_fn.text()
        mn = self.workers.lineEdit_mn.text()
        ln = self.workers.lineEdit_ln.text()
        phone = self.workers.lineEdit_tell.text()
        email = self.workers.lineEdit_email.text()
        # address = self.workers.lineEdit_address.text()
        exp = self.workers.spinBox_experience.text()
        dob = self.workers.dateEdit_dob.text()
        skill = self.workers.comboBox_skill.currentText()
        urole = 'Worker'
        gender = None

        if self.workers.radioButton_m.isChecked():
            gender = 'Male'
        if self.workers.radioButton_f.isChecked():
            gender = 'Female'

        print(nid, reg_date, kra, fn, mn, ln, gender, phone, email, dob, urole, exp,skill)


        with sqlite3.connect('database_hrm.db') as dbconn:
            c = dbconn.cursor()
        c.execute(
            "INSERT INTO user_workers(National_ID, Registration_Date, KRA_PIN, First_Name, Middle_Name, Last_Name, Gender, Phone, Email, DOB, User_role)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (nid, reg_date, kra, fn, mn, ln, gender, phone, email, dob, urole))

        QMessageBox.information(self, 'Success', "Info Added Successfully !!!", QMessageBox.Ok)
        print('Account Created Successfully')
        self.i += 1
        self.workers.lcdNumber_user_id.display(self.i)
       # self.clear1()
        dbconn.commit()
        c.close()
        dbconn.close()

    def clear1(self):
        self.workers.radioButton_m.isChecked(False)
        self.workers.radioButton_f.isChecked(False)
        self.workers.lineEdit_fn.setText('')
        self.workers.lineEdit_mn.setText('')
        self.workers.lineEdit_ln.setText('')
        self.workers.lineEdit_un.setText('')
        self.workers.lineEdit_tell.setText('')
        self.workers.lineEdit_email.setText('')
        self.workers.lineEdit_pswrd.setText('')
        self.workers.dateEdit_dob.setText('12/7/2018')



    def dashboardWindowShow(self):
        self.dashboardWindow = QMainWindow()
        self.ui = Ui_HRM_Dashboard_view()
        self.ui.setupUi(self.dashboardWindow)
        form.destroy(self)
        self.dashboardWindow.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db()
    frm = form()
    frm.showMaximized()
    sys.exit(app.exec_())

import sys
from employee import *
from admin_raw import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView, QMenuBar, QStatusBar, qApp
from PyQt5 import QtSql
from PyQt5.QtCore import QDateTime, QDate, QTime, Qt
from PyQt5 import QtCore, QtGui
import sqlite3
import random
import string


def db():
    with sqlite3.connect('database_hrm.db') as dbconn:
        c = dbconn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS user_employees(User_id  INTEGER PRIMARY KEY AUTOINCREMENT,"
              "National_ID VARCHAR (20),"
              "Registration_Date   VARCHAR,"
              "Registration_Number VARCHAR (20),"
              "Employee_hrm_code VARCHAR (20),"
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
              "timestamp          VARCHAR,"
              "User_role          VARCHAR (20))")

    dbconn.commit()
    c.close()
    dbconn.close()


class EmployeeForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.employee = Ui_HRM_Employee_view()
        self.employee.setupUi(self)

        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database_hrm.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('user_employees')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal,"User_id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "National_ID")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Registration_Date")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Registration_Number")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Employee_hrm_code")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Company_Name")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "KRA_PIN")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "First_Name")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Middle_Name")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Last_Name")
        self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Gender")
        self.model.setHeaderData(11, QtCore.Qt.Horizontal, "Phone")
        self.model.setHeaderData(12, QtCore.Qt.Horizontal, "Email")
        self.model.setHeaderData(13, QtCore.Qt.Horizontal, "Address")
        self.model.setHeaderData(14, QtCore.Qt.Horizontal, "Experience_level")
        self.model.setHeaderData(15, QtCore.Qt.Horizontal, "Skills")
        self.model.setHeaderData(16, QtCore.Qt.Horizontal, "Availability")
        self.model.setHeaderData(17, QtCore.Qt.Horizontal, "Employer")
        self.model.setHeaderData(18, QtCore.Qt.Horizontal, "Payment_Mode")
        self.model.setHeaderData(19, QtCore.Qt.Horizontal, "DOB")
        self.model.setHeaderData(20, QtCore.Qt.Horizontal, "User_role")
        self.employee.tableWidget_records.setModel(self.model)
        self.i = self.model.rowCount()
        self.employee.lcdNumber_user_id.display(self.i)

        self.datetime = QDateTime.currentDateTime()
        stamp = self.datetime.toString(Qt.DefaultLocaleLongDate)
        self.employee.dateTime_stamp.setText(stamp)
        print (stamp)

        menubar = QtWidgets.QMenuBar(self)
        menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        menubar.setObjectName("menubar")
        filemenu = menubar.addMenu("File")

        open = filemenu.addAction("Open")
        # actionFile.setTearOffEnabled(enabled)
        filemenu.addSeparator()
        quit = filemenu.addAction("Quit")
        quit.triggered.connect(lambda: self.back_home())


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

        self.show()


        self.employee.pushButton_reg.clicked.connect(self.addToDb)
        # self.employee.pushButton_update.clicked.connect(self.updaterow)
        self.employee.pushButton_back.clicked.connect(QtWidgets.qApp.quit)
        self.employee.pushButton_delete.clicked.connect(self.delrow)
        a = self.random_string_generator()
        print (a)
        self.employee.lineEdit_hrm_code.setText("HRM-"+a)

    def random_string_generator(self, size=6, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))




    def addToDb(self):

        print(self.i)
        hrm_code = self.random_string_generator()

        nid = self.employee.lineEdit_IDNo.text()
        reg_date =  self.datetime.toString(Qt.DefaultLocaleLongDate)
        reg_no = self.employee.lineEdit_regNo.text()
        hrm_code = self.employee.lineEdit_hrm_code.text()
        kra = self.employee.lineEdit_kra_pin.text()
        fn = self.employee.lineEdit_fn.text()
        mn = self.employee.lineEdit_mn.text()
        ln = self.employee.lineEdit_ln.text()
        phone = self.employee.lineEdit_tell.text()
        email = self.employee.lineEdit_email.text()
        #address = self.employee.textEdit_address
        address = '20100 NAKURU'
        exp = self.employee.spinBox_experience.text()
        dob = self.employee.dateEdit_dob.text()
        skill = self.employee.comboBox_skill.currentText()
        urole = 'Employee'
        gender = None
        available = None
        payby = None


        self.datetime = QDateTime.currentDateTime()

        stamp = self.datetime.toString(Qt.DefaultLocaleLongDate)
        self.employee.dateTime_stamp.setText(stamp)
        print (stamp)
        print (self.datetime)

        if self.employee.radioButton_m.isChecked():
            gender = 'Male'
        elif self.employee.radioButton_f.isChecked():
            gender = 'Female'
        else:
            gender = None

        if self.employee.radioButton_hr.isChecked():
            payby = 'per Hour'
        elif self.employee.radioButton_day.isChecked():
            payby = 'per Day'

        elif self.employee.radioButton_wk5.isChecked():
            payby = 'per Week(5 days)'
        elif self.employee.radioButton_wk6.isChecked():
            payby = 'per Week(6 days)'

        elif self.employee.radioButton_wk7.isChecked():
            payby = 'per Week(7 days)'
        elif self.employee.radioButton_mth21.isChecked():
            payby = 'per Month(21 days)'

        elif self.employee.radioButton_mth25.isChecked():
            payby = 'per Month(25 days)'
        else:
            payby = None

        if self.employee.radioButton_imm.isChecked():
            available = 'Immediatelly'
        elif self.employee.radioButton_aday.isChecked():
            available = 'A day Notice'

        elif self.employee.radioButton_2wks.isChecked():
            available = 'Two weeks Notice'
        elif self.employee.radioButton_1wk.isChecked():
            available = 'A week Notice'

        elif self.employee.radioButton_1mth.isChecked():
            available = 'A month  Notice'
        else:
            available = None


        print(nid, reg_date, hrm_code, kra, fn, mn, ln, gender, payby, available, phone, email,address, dob, stamp, urole, exp, skill)

        with sqlite3.connect('database_hrm.db') as dbconn:
            c = dbconn.cursor()
        c.execute(
            "INSERT INTO user_employees(National_ID, Registration_Date,Employee_hrm_code, KRA_PIN, First_Name, Middle_Name, Last_Name, Gender,Availability,Payment_Mode, Phone, Email,Address, DOB, User_role,Experience_level,Skills)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (nid, reg_date,hrm_code, kra, fn, mn, ln, gender,available,payby, phone, email,address, dob, urole, exp, skill))

        QMessageBox.information(self, 'Success', "Info Added Successfully !!!", QMessageBox.Ok)
        print('Info Added Successfully')

        self.i += 1
        self.model.select()
        self.employee.lcdNumber_user_id.display(self.i)

        # self.clear1()
        dbconn.commit()
        c.close()
        dbconn.close()

    def delrow(self):

        if self.employee.tableWidget_records.currentIndex().row() > -1:
            self.model.removeRow(self.employee.tableWidget_records.currentIndex().row())
            self.i -= 1
            self.employee.lcdNumber_user_id.display(self.i)
        else:
            QMessageBox.question(self, 'Message', "Please select a row would you like to delete", QMessageBox.Ok)
            self.show()

    def clear1(self):
        self.employee.radioButton_m.isChecked(False)
        self.employee.radioButton_f.isChecked(False)
        self.employee.lineEdit_fn.setText('')
        self.employee.lineEdit_mn.setText('')
        self.employee.lineEdit_ln.setText('')
        self.employee.lineEdit_un.setText('')
        self.employee.lineEdit_tell.setText('')
        self.employee.lineEdit_email.setText('')
        self.employee.lineEdit_pswrd.setText('')
        self.employee.dateEdit_dob.setText()

    def back_home(self):
        #self.exit_action = QtWidgets.qApp.quit()
        self.window = HRMForm()
        self.window.showMaximized()
        EmployeeForm.destroy(self)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    db()
    frm = EmployeeForm()
    frm.showMaximized()
    sys.exit(app.exec_())

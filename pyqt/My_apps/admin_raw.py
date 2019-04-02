import sys
from base import *
from clients import *
from payroll import *
from employee import *
from receipts import *
import random
import string
from employee_search import *
from WorkerForm import *
from signup import *
from login import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView, QMenuBar, QStatusBar, QProgressBar, \
    QDialog
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer, pyqtSignal
import sqlite3
from functools import partial
import PyQt5.uic as uic
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtCore import QTimer, pyqtSignal, pyqtSlot
from PyQt5.QtCore import QDateTime, QDate, QTime, Qt


###########################################################################################################################################
##############################################Project start##################################################################################


# =====================================================ClientForm Begin======================================================================


class ClientForm(QMainWindow):

    def __init__(self, master=None):
        QMainWindow.__init__(self, master)

        self.nid = 0
        self.invoice = ''
        self.company_name = ''
        self.kra_pin = ''
        self.fn_rep = ''
        self.mn_rep = ''
        self.ln_rep = ''
        self.tell_rep = ''
        self.email_rep = ''

        self.clients = Ui_HRM_Clients_view()
        self.clients.setupUi(self)
        # self.dbu = db.DatabaseUtility('UsernamePassword_DB', 'masterTable')
        self.init_window()

    def init_window(self):
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.clients.comboBox_clients_list.currentTextChanged.connect(self.search_combobox_changed)

        self.clients.pushButton_reg.clicked.connect(self.set_data)
        self.clients.pushButton_back.clicked.connect(lambda: self.back_home())
        # self.clients.pushButton_login.clicked.connect(self.connection)
        self.clients.toolButton_search.clicked.connect(EmployeeSearch)
        self.clients.pushButton_checkout.clicked.connect(lambda: self.show_pay())
        # self.clients.tabWidget_record.currentIndexChanged['int'].connect(self.search_combobox)

        # print(self.clients.tableWidget_records.currentIndex().row())
        # print(self.clients.tableView_workers_old.currentIndex().row())
        # print(self.clients.tableView_workers.currentIndex().row())

        self.show_client_view()
        self.show_employee_view()
        self.show_reg_code()
        self.search_combobox()

    def show_reg_code(self):
        a = self.random_string_generator()
        # print(a)
        self.clients.lineEdit_invoice_new.setText("HRMksh" + a)
        self.clients.lineEdit_invoice_old.setText("HRMksh" + a)
        a = self.random_string_generator()
        # print(a)
        self.clients.lineEdit_regNo_new.setText("HRM" + a)

        self.clients.lineEdit_regNo_old.setText("HRM" + a)
        self.datetime = QDateTime.currentDateTime()
        self.stamp = self.datetime.toString(Qt.DefaultLocaleLongDate)
        self.clients.lineEdit_stampNew.setText(self.stamp)
        self.clients.lineEdit_stampOld.setText(self.stamp)

        self.show_client_view()
        self.show_employee_view()

    def search_combobox(self):
        conn = sqlite3.connect('database_hrm.db')
        c = conn.cursor()
        c.execute('SELECT Company_Name from user_clients')
        rows = c.fetchall()
        if rows != None:

            for row in rows:
                # print(row)
                self.clients.comboBox_clients_list.addItems(row)

        c.close()

    def search_combobox_changed(self):

        client = self.clients.comboBox_clients_list.currentText()

        conn = sqlite3.connect('database_hrm.db')
        c = conn.cursor()

        sql = '''SELECT  User_id,
        National_ID,
        Registration_Date,
        Registration_Number,
        Company_Name,
        KRA_PIN,
        First_Name,
        Middle_Name,
        Last_Name,
        Phone,
        Email,
        Address, 
        Workforce,
        Skills,
        User_role from user_clients WHERE Company_Name= ?'''
        c.execute(sql, [client])
        rows = c.fetchall()

        if client != '':
            for self.data in rows:
                print(self.data[0])
                self.nid = self.data[1]
                self.company_name = self.data[5]
                self.kra_pin = self.data[6]
                self.fn_rep = self.data[7]
                self.mn_rep = self.data[8]
                self.ln_rep = self.data[9]
                self.tell_rep = self.data[10]
                self.email_rep = self.data[11]

                self.show_data(self.nid, self.company_name, self.kra_pin, self.fn_rep, self.mn_rep, self.ln_rep,
                               self.tell_rep, self.email_rep)

                c.close()



        else:
            QMessageBox.warning(self, 'Sorry Error', "Please Select Existing Company Name to Continue!!!")

        # self.clients.lineEdit_IDNo_new.text()
        # reg_date = stamp
        # reg_no = self.clients.lineEdit_regNo_new.text()

        # address = self.clients.lineEdit_address.text()
        c.close()

    def show_data(self, nid, company_name, kra_pin, fn_rep, mn_rep, ln_rep, tell, email_rep):

        self.clients.lineEdit_IDNo_old.setText(nid)
        self.clients.lineEdit_kra_pin_old.setText(kra_pin)
        self.clients.lineEdit_org_name_old.setText(company_name)
        self.clients.lineEdit_fn_repold.setText(fn_rep)
        self.clients.lineEdit_mn_repold.setText(mn_rep)
        self.clients.lineEdit_ln_repold.setText(ln_rep)
        self.clients.lineEdit_tell_repold.setText(tell)
        self.clients.lineEdit_email_repold.setText(email_rep)

    def show_employee_view(self):
        self.db1 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db1.setDatabaseName('database_hrm.db')
        self.model1 = QtSql.QSqlTableModel()
        self.model1.setTable('view_worker_for_client')
        self.model1.select()
        # self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Worker_hrm_code")
        self.model1.setHeaderData(0, QtCore.Qt.Horizontal, "National ID No")
        self.model1.setHeaderData(1, QtCore.Qt.Horizontal, "KRA PIN No")
        self.model1.setHeaderData(2, QtCore.Qt.Horizontal, "First_Name")
        self.model1.setHeaderData(3, QtCore.Qt.Horizontal, "Middle_Name")
        self.model1.setHeaderData(4, QtCore.Qt.Horizontal, "Last_Name")
        self.model1.setHeaderData(5, QtCore.Qt.Horizontal, "Gender")
        self.model1.setHeaderData(6, QtCore.Qt.Horizontal, "Phone")
        self.model1.setHeaderData(7, QtCore.Qt.Horizontal, "Email")
        self.model1.setHeaderData(8, QtCore.Qt.Horizontal, "Address")
        self.model1.setHeaderData(9, QtCore.Qt.Horizontal, "Experience_level")
        self.model1.setHeaderData(10, QtCore.Qt.Horizontal, "Skills")
        self.model1.setHeaderData(11, QtCore.Qt.Horizontal, "Availability")

        self.model1.select()
        self.clients.tableView_workers.setModel(self.model1)
        self.clients.tableView_workers_old.setModel(self.model1)
        self.db1.close()

    def show_client_view(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database_hrm.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('view_clients')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "National ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Registration Date")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Registration No")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Invoice No")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Company Name")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "KRA PIN")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "First Name")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Middle Name")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Last Name")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Phone")
        self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Email")
        self.model.setHeaderData(11, QtCore.Qt.Horizontal, "Workforce")
        self.model.setHeaderData(12, QtCore.Qt.Horizontal, "Skills")
        self.model.setHeaderData(13, QtCore.Qt.Horizontal, "Pay Rate")
        self.model.select()
        self.clients.tableWidget_records.setModel(self.model)
        # print(self.clients.tableWidget_records.currentIndex().row())
        self.i = self.model.rowCount()
        self.clients.lcdNumber_user_id.display(self.i)
        # print(self.i)
        self.show()

    def showMessageBox(self, title, message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def create_table(self):

        try:

            self.enter_data()


        except:
            conn = sqlite3.connect('database_hrm.db')
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS user_clients(User_id  INTEGER PRIMARY KEY AUTOINCREMENT,"
                      "National_ID VARCHAR (20),"
                      "Registration_Date   VARCHAR,"
                      "Registration_Number VARCHAR (20),"
                      "Client_invoice_Number VARCHAR (20),"
                      "Company_Name VARCHAR (50),"
                      "KRA_PIN VARCHAR (20),"
                      "First_Name          VARCHAR (20),"
                      "Middle_Name         VARCHAR (20),"
                      "Last_Name           VARCHAR (20),"
                      "Phone               VARCHAR (16),"
                      "Email               VARCHAR (50),"
                      "Address             VARCHAR (50),"
                      "Workforce           INTEGER(5),"
                      "Skills          VARCHAR (20),"
                      "Payment_Rate        VARCHAR (20),"
                      "User_role          VARCHAR (20))")
            print('Operational:', "Table Created Successfully")

            QMessageBox.information(self, 'User', "Table Data created  Successfully", QMessageBox.Ok)
            conn.commit()
            self.enter_data()
            QMessageBox.information(self, 'Success', "Info Added Successfully !!!", QMessageBox.Ok)
            c.close()
            conn.close()

    def enter_data(self):
        a = self.random_string_generator()
        # print (a)
        self.date = QDate.currentDate()
        self.time = QTime.currentTime()
        dstamp = self.date.toString(Qt.ISODate)
        tstamp = self.time.toString(Qt.DefaultLocaleLongDate)
        self.clients.lineEdit_regNo_old.setText(dstamp + a + tstamp)
        self.clients.lineEdit_regNo_new.setText(dstamp + a + tstamp)

        stamp = (dstamp + ' ' + tstamp)
        nid = self.clients.lineEdit_IDNo_new.text()
        reg_date = stamp
        reg_no = self.clients.lineEdit_regNo_new.text()
        hrm_code = self.clients.lineEdit_invoice_new.text()
        kra = self.clients.lineEdit_kra_pin_new.text()
        org_name = self.clients.lineEdit_org_name_new.text()
        fn = self.clients.lineEdit_fn_repnew.text()
        mn = self.clients.lineEdit_mn_repnew.text()
        ln = self.clients.lineEdit_ln_repnew.text()
        phone = self.clients.lineEdit_tell_repnew.text()
        email = self.clients.lineEdit_email_repnew.text()
        force = self.clients.spinBox_workforce.text()
        # address = self.clients.lineEdit_address.text()
        pay_rate = self.clients.comboBox_payrate_new.currentText()
        skill = self.clients.comboBox_skill_new.currentText()
        urole = 'Client'

        # print(nid, reg_date, kra, hrm_code, org_name, fn, mn, ln, phone, email, urole, pay_rate, skill, force)

        try:
            conn = sqlite3.connect('database_hrm.db')
            c = conn.cursor()

            c.execute(
                "INSERT INTO user_clients(National_ID,"
                " Registration_Date,"
                " Registration_Number,"
                " Client_invoice_Number,"
                " Company_Name,"
                "KRA_PIN,"
                " First_Name,"
                " Middle_Name,"
                " Last_Name,"
                " Phone,"
                " Email,"
                " User_role,"
                " Payment_Rate,"
                " Skills,"
                " Workforce)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (nid, reg_date, reg_no, hrm_code, org_name, kra, fn, mn, ln, phone, email, urole, pay_rate, skill,
                 force))

            conn.commit()

            self.show_reg_code()

            QMessageBox.information(self, 'Success', "Info Added Successfully !!!", QMessageBox.Ok)
            c.close()
            conn.close()
        except ValueError:
            QMessageBox.information(self, 'Error', "Data Not Successfully Inserted ", QMessageBox.Ok)
            print(ValueError)

    # TODO

    # TODO know how to set data to list from a sqlite table

    def view_data(self):
        print("TODO")

    @staticmethod
    def random_string_generator(size=12, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def set_data(self):

        try:
            self.create_table()

        except ValueError:
            QMessageBox.information(self, "User Error", "Sorry, An Error Occurred!!", QMessageBox.Ok)

    def delrow(self):

        if self.clients.tableWidget_records.currentIndex().row() > -1:

            buttonReply = QMessageBox.question(self, 'Confirm Record Delete',
                                               "Do you really want to delete this record??",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.model.removeRow(self.clients.tableWidget_records.currentIndex().row())
                self.i -= 1
                self.clients.lcdNumber_user_id.display(self.i)
                self.show_client_view()
            else:
                self.show_client_view()
        else:

            QMessageBox.question(self, 'Message', "Please select a row would you like to delete", QMessageBox.Ok)
            self.show()

    def show_pay(self):
        p = PaymentsDialog()
        p.show()

    def back_home(self):
        self.close()

    # def connection(self):
    #    try:
    #        mdb = hrmDB.connect('localhost', 'root', '', 'HRMSDB')
    #        QMessageBox.about(self, 'Connection', 'Successfully Connected to DB')

    #    except hrmDB.Error as e:
    #        QMessageBox.about(self, 'Connection', 'Not Connected Successfully Connected to DB')
    #        sys.exit()


# =====================================================ClientForm Ends======================================================================

# =====================================================EmployeeSearch Begin======================================================================

class EmployeeSearch(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.search = Ui_empSearchDialog()
        self.search.setupUi(self)
        self.exec_()

    def cancel(self):
        self.close()


# =====================================================EmployeeSearch Ends======================================================================

# =====================================================Payments Begin======================================================================

class PaymentsDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.pay = Ui_ReceiptDialog()
        self.pay.setupUi(self)
        self.init_window()

    def init_window(self):
        self.pay.pushButton_cancel.clicked.connect(lambda: self.cancel())

    def cancel(self):
        self.close()


# =====================================================Payments Ends======================================================================

# =====================================================EmployeeForm Begin======================================================================

class EmployeeForm(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.employee = Ui_HRM_Employee_view()
        self.employee.setupUi(self)
        self.init_window()

    def init_window(self):

        self.employee.pushButton_reg.clicked.connect(lambda: self.create_table())
        # self.employee.pushButton_update.clicked.connect(self.updaterow)
        self.employee.pushButton_back.clicked.connect(lambda: self.back_home())

        self.show_employee_view()
        self.show_hrmcode()
        self.show_time()
        self.show_status_bar()
        self.show_menu()

    def show_time(self):
        self.datetime = QDateTime.currentDateTime()
        self.stamp = self.datetime.toString(Qt.DefaultLocaleLongDate)
        self.employee.label_timestamp.setText(self.stamp)

        a = self.random_string_generator()
        # print (a)
        self.date = QDate.currentDate()
        self.time = QTime.currentTime()
        dstamp = self.date.toString(Qt.ISODate)
        tstamp = self.time.toString(Qt.DefaultLocaleLongDate)
        self.employee.lineEdit_regNo.setText(dstamp + a + tstamp)

    def show_status_bar(self):
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def show_menu(self):
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

    def show_hrmcode(self):
        a = self.random_string_generator()
        # print (a)
        self.employee.lineEdit_hrm_code.setText("HRM" + a)
        self.employee.lineEdit_regNo.setText("HRM" + a)

    def show_employee_view(self):

        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database_hrm.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('view_employee')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "National_ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Registration_Date")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Registration_Number")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Employee_hrm_code")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "KRA_PIN")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "First_Name")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Middle_Name")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Last_Name")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Gender")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Phone")
        self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Email")
        self.model.setHeaderData(11, QtCore.Qt.Horizontal, "Address")
        self.model.setHeaderData(12, QtCore.Qt.Horizontal, "Experience_level")
        self.model.setHeaderData(13, QtCore.Qt.Horizontal, "Skills")
        self.model.setHeaderData(14, QtCore.Qt.Horizontal, "Availability")
        self.model.setHeaderData(15, QtCore.Qt.Horizontal, "Payment_Mode")
        self.employee.tableWidget_records.setModel(self.model)
        self.i = self.model.rowCount()
        self.employee.lcdNumber_user_id.display(self.i)
        self.show()

    def create_table(self):

        try:

            self.enter_data()

        except:
            conn = sqlite3.connect('database_hrm.db')
            c = conn.cursor()
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
            print('Operational:', "Table Created Successfully")

            QMessageBox.information(self, 'User', "Table Data created  Successfully", QMessageBox.Ok)
            conn.commit()
            self.enter_data()
            QMessageBox.information(self, 'Success', "Info Added Successfully !!!", QMessageBox.Ok)
            c.close()
            conn.close()

    def enter_data(self):

        nid = self.employee.lineEdit_IDNo.text()
        reg_date = self.datetime.toString(Qt.DefaultLocaleLongDate)
        reg_no = self.employee.lineEdit_regNo.text()
        hrm_code = self.employee.lineEdit_hrm_code.text()
        kra = self.employee.lineEdit_kra_pin.text()
        fn = self.employee.lineEdit_fn.text()
        mn = self.employee.lineEdit_mn.text()
        ln = self.employee.lineEdit_ln.text()
        phone = self.employee.lineEdit_tell.text()
        email = self.employee.lineEdit_email.text()
        # address = self.employee.textEdit_address
        address = '20100 NAKURU'
        exp = self.employee.spinBox_experience.text()
        dob = self.employee.dateEdit_dob.text()
        skill = self.employee.comboBox_skill.currentText()
        urole = 'Employee'
        gender = None
        available = None
        payby = None

        self.date = QDate.currentDate()
        self.time = QTime.currentTime()
        dstamp = self.date.toString(Qt.DefaultLocaleShortDate)
        tstamp = self.time.toString(Qt.DefaultLocaleLongDate)

        stamp = (dstamp + ' ' + tstamp)

        # print(nid, reg_date, hrm_code, kra, fn, mn, ln, gender, payby, available, phone, email, address, dob, stamp,urole,exp, skill)

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

        try:
            conn = sqlite3.connect('database_hrm.db')
            c = conn.cursor()

            c.execute(
                "INSERT INTO user_employees(National_ID, "
                "Registration_Date,"
                "Registration_Number,"
                "Employee_hrm_code, "
                "KRA_PIN, "
                "First_Name, "
                "Middle_Name, "
                "Last_Name, "
                "Gender,"
                "Availability,"
                "Payment_Mode, "
                "Phone, "
                "Email,"
                "Address, "
                "DOB, "
                "User_role,"
                "Experience_level,"
                "Skills)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (nid, stamp, reg_no, hrm_code, kra, fn, mn, ln, gender, available, payby, phone, email, address, dob,
                 urole, exp, skill))

            conn.commit()
            self.show_employee_view()
            self.show_hrmcode()
            self.show_time()
            QMessageBox.information(self, 'Success', "Info Added Successfully !!!", QMessageBox.Ok)
            c.close()
            conn.close()
        except ValueError:
            QMessageBox.information(self, 'Error', "Data Not Successfully Inserted ", QMessageBox.Ok)
            print(ValueError)

    def random_string_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def delrow(self):

        if self.employee.tableWidget_records.currentIndex().row() > -1:

            buttonReply = QMessageBox.question(self, 'Confirm Record Delete',
                                               "Do you really want to delete this record??",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.model.removeRow(self.employee.tableWidget_records.currentIndex().row())
                self.i -= 1
                self.employee.lcdNumber_user_id.display(self.i)
                self.show_employee_view()
            else:
                self.show_employee_view()
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
        self.close()


# =====================================================EmployeeForm Ends======================================================================

# =====================================================RegForm starts======================================================================


class RegForm(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.signup = Ui_HRM_Signup_view()
        self.signup.setupUi(self)
        self.init_window()

    def init_window(self):
        self.signup.pushButton_signup.clicked.connect(lambda: self.create_account())
        self.signup.pushButton_back.clicked.connect(lambda: self.back_home())
        self.signup.pushButton_login.clicked.connect(lambda: self.view_login())

    def create_table(self):

        self.conn = sqlite3.connect('database_hrm.db')
        self.c = conn.cursor()

        try:

            self.c.execute("CREATE TABLE IF NOT EXISTS superusers(User_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                           "First_Name VARCHAR(20),"
                           "Middle_Name VARCHAR,"
                           "Last_Name VARCHAR,"
                           "User_Name VARCHAR,"
                           "Phone INTEGER,"
                           "Email VARCHAR,"
                           "Password VARCHAR,"
                           "DOB VARCHAR,"
                           "User_role VARCHAR,"
                           "Gender VARCHAR)")

            QMessageBox.information(self, 'User', "Table Data created  Successfully", QMessageBox.Ok)
            conn.commit()
            self.c.close()
            self.conn.close()
            self.enter_data()
        except:
            self.enter_data()
            QMessageBox.information(self, 'Success', "Info Added Successfully !!!", QMessageBox.Ok)
            self.c.close()
            self.conn.close()

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

            c.execute("INSERT INTO superusers(First_Name,"
                      " Middle_Name,"
                      " Last_Name,"
                      " User_Name,"
                      " Phone, Email,"
                      " Password,"
                      " DOB,"
                      " User_role,"
                      " Gender)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (fn, mn, ln, un, phone, email, password, dob, urole, gender))

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
        self.close()
        r = LoginDialog()
        r.show()

    def view_login(self):
        self.close()
        r = LoginDialog()
        r.show()


# =====================================================RegForm Ends======================================================================


# =====================================================PayForm Begins======================================================================


class PayrollDialog(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.payroll = Ui_payrolDialog()
        self.payroll.setupUi(self)
        self.grosspay = 0
        self.gross_pay = 0
        self.deduc = 0
        self.deductions = 0
        self.bsalary = 0
        self.med_allowance = 0
        self.hse_allowance = 0
        self.oth_allowance = 0
        self.paye = 0
        self.nhif = 0
        self.nssf = 0
        self.insuarance_pp = 0
        self.pension = 0
        self.pension_volun = 0
        self.loans = 0
        self.net = 0

        self.payroll.label_paye.setText(str(self.deduc))

        self.payroll.checkBox_bsalary.toggled.connect(self.checkbox_toggled_allowances)
        self.payroll.label_bsalary.setText(str(0))

        self.payroll.checkBox_hse_allowance.toggled.connect(self.checkbox_toggled_allowances)
        self.payroll.label_hse_allowance.setText(str(0))

        self.payroll.checkBox_med_allowance.toggled.connect(self.checkbox_toggled_allowances)
        self.payroll.label_med_allowance.setText(str(0))

        self.payroll.checkBox_oth_allowance.toggled.connect(self.checkbox_toggled_allowances)
        self.payroll.label_oth_allowance.setText(str(0))

        self.payroll.label_gross_salary.setText(str(self.gross_pay))
        self.payroll.label_total_deductions.setText(str(self.deductions))

        self.payroll.label_total_deductions.setText(str(self.deductions))

        self.payroll.checkBox_paye.toggled.connect(self.checkbox_toggled_deduction)
        self.payroll.label_paye.setText(str(0))

        self.payroll.checkBox_nhif.toggled.connect(self.checkbox_toggled_deduction)
        self.payroll.label_nhif.setText(str(0))

        self.payroll.checkBox_nssf.toggled.connect(self.checkbox_toggled_deduction)
        self.payroll.label_nssf.setText(str(0))

        self.payroll.checkBox_insuarance_premium.toggled.connect(self.checkbox_toggled_deduction)
        self.payroll.label_insuarance_premium.setText(str(0))

        self.payroll.checkBox_provident_pension.toggled.connect(self.checkbox_toggled_deduction)
        self.payroll.label_provident_pension.setText(str(0))

        self.payroll.checkBox_voluntary_pension.toggled.connect(self.checkbox_toggled_deduction)
        self.payroll.label_voluntary_pension.setText(str(0))

        self.payroll.checkBox_loans.toggled.connect(self.checkbox_toggled_deduction)
        self.payroll.label_loan.setText(str(0))

        self.payroll.label_net_pay.setText(str(self.net))

        self.show()

    def net_pay(self, a, b):
        self.net = a - b
        return self.net

    def p_a_ye(self, x):

        if 0 < x <= 147580:
            self.deduc = x * 0.1
            self.paye = self.deduc
        elif 147581 <= x <= 286623:
            self.deduc = x * 0.15
            self.paye = self.deduc
        elif 286624 <= x <= 425660:
            self.deduc = x * 0.2
            self.paye = self.deduc
        elif 425667 <= x <= 564709:
            self.deduc = x * 0.25
            self.paye = self.deduc
        elif x <= 5647010:
            self.deduc = x * 0.3
            self.paye = self.deduc
        return self.paye

    def checkbox_toggled_allowances(self):

        if self.payroll.checkBox_bsalary.isChecked():
            self.bsalary = 50000
            self.payroll.label_bsalary.setText(str(self.bsalary))
            self.gross_pay = self.bsalary + self.med_allowance + self.hse_allowance + self.oth_allowance
            self.payroll.label_gross_salary.setText(str(self.gross_pay))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        else:
            self.gross_pay = self.gross_pay - self.bsalary
            self.payroll.label_bsalary.setText(str(0))
            self.payroll.label_gross_salary.setText(str(self.gross_pay))
            self.bsalary = 0
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        if self.payroll.checkBox_med_allowance.isChecked():
            self.med_allowance = 1000
            self.payroll.label_med_allowance.setText(str(self.med_allowance))

            self.gross_pay = self.bsalary + self.med_allowance + self.hse_allowance + self.oth_allowance
            self.payroll.label_gross_salary.setText(str(self.gross_pay))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))


        else:
            self.gross_pay = self.gross_pay - self.med_allowance
            self.payroll.label_med_allowance.setText(str(0))
            self.payroll.label_gross_salary.setText(str(self.gross_pay))
            self.med_allowance = 0
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        if self.payroll.checkBox_hse_allowance.isChecked():
            self.hse_allowance = 6500
            self.payroll.label_hse_allowance.setText(str(self.hse_allowance))

            self.gross_pay = self.bsalary + self.med_allowance + self.hse_allowance + self.oth_allowance
            self.payroll.label_gross_salary.setText(str(self.gross_pay))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))


        else:
            self.gross_pay = self.gross_pay - self.hse_allowance
            self.payroll.label_hse_allowance.setText(str(0))
            self.payroll.label_gross_salary.setText(str(self.gross_pay))
            self.hse_allowance = 0
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        if self.payroll.checkBox_oth_allowance.isChecked():
            self.oth_allowance = 4000
            self.payroll.label_oth_allowance.setText(str(self.oth_allowance))

            self.gross_pay = self.bsalary + self.med_allowance + self.hse_allowance + self.oth_allowance
            self.payroll.label_gross_salary.setText(str(self.gross_pay))
            self.net_pay(self.gross_pay, self.deductions)

        else:
            self.gross_pay = self.gross_pay - self.oth_allowance
            self.payroll.label_oth_allowance.setText(str(0))
            self.payroll.label_gross_salary.setText(str(self.gross_pay))
            self.oth_allowance = 0
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

    def checkbox_toggled_deduction(self):
        print(self.gross_pay)

        if self.payroll.checkBox_paye.isChecked():
            self.paye = self.p_a_ye(self.gross_pay)
            self.deductions = self.nhif + self.nssf + self.insuarance_pp + self.pension + self.pension_volun + self.loans + self.paye
            self.payroll.label_paye.setText(str(self.paye))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        else:
            self.deductions = self.deductions - self.paye
            self.paye = 0

            self.payroll.label_paye.setText(str(self.paye))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        if self.payroll.checkBox_nhif.isChecked():
            self.nhif = 1000
            self.deductions = self.nhif + self.nssf + self.insuarance_pp + self.pension + self.pension_volun + self.loans + self.paye
            self.payroll.label_nhif.setText(str(self.nhif))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        else:
            self.deductions = self.deductions - self.nhif
            self.nhif = 0

            self.payroll.label_nhif.setText(str(self.nhif))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        if self.payroll.checkBox_nssf.isChecked():
            self.nssf = 200
            self.deductions = self.nhif + self.nssf + self.insuarance_pp + self.pension + self.pension_volun + self.loans + self.paye
            self.payroll.label_nssf.setText(str(self.nssf))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        else:

            self.deductions = self.deductions - self.nssf

            self.nssf = 0
            self.payroll.label_nssf.setText(str(self.nssf))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        if self.payroll.checkBox_insuarance_premium.isChecked():
            self.insuarance_pp = 2500
            self.deductions = self.nhif + self.nssf + self.insuarance_pp + self.pension + self.pension_volun + self.loans + self.paye
            self.payroll.label_insuarance_premium.setText(str(self.insuarance_pp))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        else:
            self.deductions = self.deductions - self.insuarance_pp
            self.insuarance_pp = 0

            self.payroll.label_insuarance_premium.setText(str(self.insuarance_pp))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        if self.payroll.checkBox_provident_pension.isChecked():
            self.pension = 3450
            self.deductions = self.nhif + self.nssf + self.insuarance_pp + self.pension + self.pension_volun + self.loans + self.paye
            self.payroll.label_provident_pension.setText(str(self.pension))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        else:
            self.deductions = self.deductions - self.pension
            self.pension = 0

            self.payroll.label_provident_pension.setText(str(self.pension))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        if self.payroll.checkBox_voluntary_pension.isChecked():
            self.pension_volun = 1235
            self.deductions = self.nhif + self.nssf + self.insuarance_pp + self.pension + self.pension_volun + self.loans + self.paye
            self.payroll.label_voluntary_pension.setText(str(self.pension_volun))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        else:
            self.deductions = self.deductions - self.pension_volun
            self.pension_volun = 0

            self.payroll.label_voluntary_pension.setText(str(self.pension_volun))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        if self.payroll.checkBox_loans.isChecked():
            self.loans = 150
            self.deductions = self.nhif + self.nssf + self.insuarance_pp + self.pension + self.pension_volun + self.loans + self.paye
            self.payroll.label_loan.setText(str(self.loans))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

        else:
            self.deductions = self.deductions - self.loans
            self.loans = 0

            self.payroll.label_loan.setText(str(self.loans))
            self.payroll.label_total_deductions.setText(str(self.deductions))
            self.net = self.net_pay(self.gross_pay, self.deductions)
            self.payroll.label_net_pay.setText(str(self.net))

    def cancel(self):
        self.close()


# =====================================================PayForm Ends======================================================================


# =====================================================HRMForm start======================================================================


class HRMForm(QMainWindow):

    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.dashboard = Ui_HRM_Dashboard_view()
        self.login = LoginDialog()

        self.dashboard.setupUi(self)

        # self.createProgressBar()

        self.dashboard.actionNewEmployee.triggered.connect(lambda: self.new_employee())
        self.dashboard.actionNewWorker.triggered.connect(lambda: self.new_worker())
        self.dashboard.actionNewClient.triggered.connect(lambda: self.new_client())
        self.dashboard.actionQiut_Application.triggered.connect(lambda: self.close())
        self.dashboard.pushButton_user_login.clicked.connect(lambda: self.login_user())
        self.dashboard.pushButton_user_reg.clicked.connect(lambda: self.new_user())
        self.dashboard.pushButton_exit_app.clicked.connect(QtWidgets.qApp.quit)

        self.dashboard.toolButton_print.clicked.connect(self.createPrintDialog)

        self.uname = self.dashboard.label_welcome_username.text()
        print (self.uname)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

    def dashboardWindowShow(self):
        pass

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
        e = EmployeeForm()
        e.showMaximized()

    def new_user(self):
        self.close()
        r = RegForm()
        r.show()

    def login_user(self):
        log = LoginDialog()
        log.show()

    def new_client(self):
        c = ClientForm()
        c.showMaximized()

    def new_worker(self):
        wo = WorkerForm()
        wo.showMaximized()

    def new_employer(self):
        pass

    def register_staff(self):
        pass

    def show_it(self, the_username):
        self.dashboard.label_welcome_username.setText(the_username)

    def createPrintDialog(self):
        mylist = []

        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.dashboard.label_welcome_username.print_(printer)


# =====================================================HRMForm start======================================================================

# =====================================================LoginDialog start======================================================================


class LoginDialog(QDialog):
    got_username = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        QDialog.__init__(self, *args, **kwargs)
        self.login = Ui_HRM_Login_view()
        self.login.setupUi(self)
        self.un = self.login.lineEdit_un.text()

        self.login.pushButton_login.clicked.connect(lambda: self.login_check())
        self.login.pushButton_signup.clicked.connect(lambda: self.register())

    def login_check(self):
        with sqlite3.connect('database_hrm.db') as db:
            c = db.cursor()

        self.un = self.login.lineEdit_un.text()
        password = self.login.lineEdit_pass.text()
        c.execute('SELECT * FROM superusers WHERE User_Name = ? and Password = ?', (self.un, password))
        data = c.fetchone()
        db.commit()
        if data != None:
            QMessageBox.information(self, 'Message', "Logged Successfully !!!", QMessageBox.Ok)
            self.accept()
            # print (self.comfirm())
        else:
            QMessageBox.information(self, 'Error',
                                    "No Account With That Username And Password\nPlease check your Credatials",
                                    QMessageBox.Ok)

    def comfirm(self):

        self.value = self.login.lineEdit_un.text()
        self.got_username.emit(self.value)
        return self.value

    def register(self):
        self.close()
        r = RegForm()
        r.show()


# =====================================================LoginDialog Ends======================================================================


###########################################################################################################################################
##############################################Project end##################################################################################


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginDialog()
    w = HRMForm()
    w.hide()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        uname = login.comfirm()
        w.dashboard.label_welcome_username.setText(uname)

        w.showMaximized()

    else:
        w.close()

    sys.exit(app.exec_())

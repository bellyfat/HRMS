import sys
from clients import *
from admin_raw import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView, QMenuBar, QStatusBar
from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QDateTime, QDate, QTime, Qt
import sqlite3
import random
import string
#import MySQLdb as hrmDB





class ClientForm(QMainWindow):



    def __init__(self, master=None):
        QMainWindow.__init__(self, master)
        self.clients = Ui_HRM_Clients_view()
        self.clients.setupUi(self)
        


        menubar = QtWidgets.QMenuBar(self)
        menubar.setGeometry(QtCore.QRect(0, 0, 1516, 21))
        menubar.setObjectName("menubar")

        filemenu = menubar.addMenu("File")

        open = filemenu.addMenu("Open")

        open.addAction('New')
        open.addAction('Save')
        open.addAction('Save As')
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

        self.datetime = QDateTime.currentDateTime()
        stamp = self.datetime.toString(Qt.DefaultLocaleLongDate)
        self.clients.dateTimeEdit_stampNew.setText(stamp)
        self.clients.dateTimeEdit_stampOld.setText(stamp)
        print(stamp)





        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database_hrm.db')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('user_clients')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "National ID")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Registration Date")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Registration No")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Invoice No")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Company Name")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "KRA PIN")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "First Name")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Middle Name")
        self.model.setHeaderData(9, QtCore.Qt.Horizontal, "Last Name")
        self.model.setHeaderData(10, QtCore.Qt.Horizontal, "Phone")
        self.model.setHeaderData(11, QtCore.Qt.Horizontal, "Email")
        self.model.setHeaderData(13, QtCore.Qt.Horizontal, "Workforce")
        self.model.setHeaderData(14, QtCore.Qt.Horizontal, "Skills")
        self.model.setHeaderData(15, QtCore.Qt.Horizontal, "Pay Rate")
        self.clients.tableWidget_records.setModel(self.model)
        print(self.clients.tableWidget_records.currentIndex().row())
        self.i = self.model.rowCount()
        self.clients.lcdNumber_user_id.display(self.i)
        self.show()
        self.clients.comboBox_clients_list.addItem('No User Yet')

        conn = sqlite3.connect('database_hrm.db')
        c = conn.cursor()
        c.execute('SELECT Company_Name from user_clients')
        rows = c.fetchall()
        print(rows)
        if rows!=None:

            for row in rows:
                print(row)
                self.clients.comboBox_clients_list.addItems(row)



        a = self.random_string_generator()
        print(a)
        self.clients.lineEdit_invoice_new.setText("2018-" + a)



        self.db1 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db1.setDatabaseName('database_hrm.db')
        self.model1 = QtSql.QSqlTableModel()
        self.model1.setTable('user_employees')
        self.model1.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model1.select()
       # self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Worker_hrm_code")
        self.model1.setHeaderData(1, QtCore.Qt.Horizontal, "First_Name")
        self.model1.setHeaderData(2, QtCore.Qt.Horizontal, "Middle_Name")
        self.model1.setHeaderData(3, QtCore.Qt.Horizontal, "Last_Name")
        self.model1.setHeaderData(4, QtCore.Qt.Horizontal, "Gender")
        self.model1.setHeaderData(5, QtCore.Qt.Horizontal, "Phone")
        self.model1.setHeaderData(6, QtCore.Qt.Horizontal, "Email")
        self.model1.setHeaderData(7, QtCore.Qt.Horizontal, "Address")
        self.model1.setHeaderData(8, QtCore.Qt.Horizontal, "Experience_level")
        self.model1.setHeaderData(9, QtCore.Qt.Horizontal, "Skills")
        self.clients.tableView_workers.setModel(self.model1)
        self.db1.close()

        self.show()

        self.db2 = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db2.setDatabaseName('database_hrm.db')
        self.model2 = QtSql.QSqlTableModel()
        self.model2.setTable('user_employees')
        self.model2.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model2.select()
        self.model2.setHeaderData(0, QtCore.Qt.Horizontal, "Worker_hrm_code")
        self.model2.setHeaderData(1, QtCore.Qt.Horizontal, "First_Name")
        self.model2.setHeaderData(2, QtCore.Qt.Horizontal, "Middle_Name")
        self.model2.setHeaderData(3, QtCore.Qt.Horizontal, "Last_Name")
        self.model2.setHeaderData(4, QtCore.Qt.Horizontal, "Gender")
        self.model2.setHeaderData(5, QtCore.Qt.Horizontal, "Phone")
        self.model2.setHeaderData(6, QtCore.Qt.Horizontal, "Email")
        self.model2.setHeaderData(7, QtCore.Qt.Horizontal, "Address")
        self.model2.setHeaderData(8, QtCore.Qt.Horizontal, "Experience_level")
        self.model2.setHeaderData(9, QtCore.Qt.Horizontal, "Skills")
        self.clients.tableView_workers_old.setModel(self.model2)
        self.db2.close()

        self.show()


        self.clients.pushButton_reg.clicked.connect(self.set_data)
        # self.clients.pushButton_update.clicked.connect(self.updaterow)
        self.clients.pushButton_back.clicked.connect(self.delrow)
        self.clients.pushButton_delete.clicked.connect(self.delrow)
        #self.clients.pushButton_login.clicked.connect(self.connection)


        print(self.clients.tableWidget_records.currentIndex().row())
        print(self.clients.tableView_workers_old.currentIndex().row())
        print(self.clients.tableView_workers.currentIndex().row())



    def showMessageBox(self, title, message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def create_table(self):

        try:
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
              "Phone               INTEGER (10),"
              "Email               VARCHAR (50),"
              "Address             VARCHAR (50),"
              "Workforce           INTEGER(5),"
              "Skills          VARCHAR (20),"
              "Payment_Rate        VARCHAR (20),"
              "User_role          VARCHAR (20))")
            print('Operational:', "Table Created Successfully")

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

    def enter_data(self):

        print(self.i)
        self.datetime = QDateTime.currentDateTime()

        stamp = self.datetime.toString(Qt.DefaultLocaleLongDate)
        print(stamp)

        nid = self.clients.lineEdit_IDNo_new.text()
        reg_date = stamp
        # reg_no = self.clients.lineEdit_regNo_new.text()
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

        print(nid, reg_date, kra, hrm_code, org_name, fn, mn, ln, phone, email, urole, pay_rate, skill, force)

        try:
            conn = sqlite3.connect('database_hrm.db')
            c = conn.cursor()

            c.execute(
            "INSERT INTO user_clients(National_ID,"
            " Registration_Date,"
            " Client_invoice_Number,"
            " Company_Name, KRA_PIN,"
            " First_Name, Middle_Name,"
            " Last_Name,"
            " Phone,"
            " Email,"
            " User_role,"
            " Payment_Rate,"
            " Skills,"
            " Workforce)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (nid, reg_date, hrm_code, org_name, kra, fn, mn, ln, phone, email, urole, pay_rate, skill, force))

            conn.commit()
            c.close()
            conn.close()
        except ValueError:
            QMessageBox.information(self, 'Error', "Data Inserted  Not Success", QMessageBox.Ok)

    # TODO

    # TODO know how to set data to list from a sqlite table

    def view_data(self):
        print("TODO")

    def random_string_generator(self, size=12, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def set_data(self):

        try:
            self.create_table()

        except ValueError:
            QMessageBox.information(self, "User Error", "Sorry, An Error Occurred!!", QMessageBox.Ok)




    def addToDb(self):
        print(self.i)
        self.datetime = QDateTime.currentDateTime()

        stamp = self.datetime.toString(Qt.DefaultLocaleLongDate)
        print(stamp)

        nid = self.clients.lineEdit_IDNo_new.text()
        reg_date = stamp
        # reg_no = self.clients.lineEdit_regNo_new.text()
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

        print(nid, reg_date, kra, hrm_code, org_name, fn, mn, ln, phone, email, urole, pay_rate, skill, force)

        with sqlite3.connect('database_hrm.db') as dbconn:
            c = dbconn.cursor()
        c.execute(
            "INSERT INTO user_clients(National_ID, Registration_Date, Client_invoice_Number, Company_Name, KRA_PIN, First_Name, Middle_Name, Last_Name,Phone, Email,User_role,Payment_Rate,Skills,Workforce)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (nid, reg_date, hrm_code, org_name, kra, fn, mn, ln, phone, email, urole, pay_rate, skill, force))
        QMessageBox.information(self, 'Success', "Info Added Successfully !!!", QMessageBox.Ok)
        print('Info Added Successfully')

        self.i += 1

        self.clients.lcdNumber_user_id.display(self.i)


        # self.clear1()
        dbconn.commit()
        c.close()
        dbconn.close()

        

    def delrow(self):

        if self.clients.tableWidget_records.currentIndex().row() > -1:
            self.model.removeRow(self.clients.tableWidget_records.currentIndex().row())
            self.i -= 1
            self.clients.lcdNumber_user_id.display(self.i)
        else:
            QMessageBox.question(self,'Message', "Please select a row would you like to delete", QMessageBox.Ok)
            

    def back_home(self):
        ClientForm.hide(self)
        self.window = HRMForm()
        self.window.showMaximized()


    #def connection(self):
    #    try:
    #        mdb = hrmDB.connect('localhost', 'root', '', 'HRMSDB')
    #        QMessageBox.about(self, 'Connection', 'Successfully Connected to DB')

    #    except hrmDB.Error as e:
    #        QMessageBox.about(self, 'Connection', 'Not Connected Successfully Connected to DB')
    #        sys.exit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    frm = ClientForm()
    frm.showMaximized()
    sys.exit(app.exec_())

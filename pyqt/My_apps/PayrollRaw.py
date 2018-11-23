import sys
from payroll import *
from admin_raw import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView, QStatusBar, QMenuBar, QStatusBar
from PyQt5 import QtSql
from PyQt5 import QtCore, QtGui
import sqlite3
from PyQt5.QtSql import QSqlQuery


class PayForm(QMainWindow):

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
            self.bsalary = 34000
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
            self.hse_allowance = 3500
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
            self.nhif = 850
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
















if __name__ == '__main__':
    app = QApplication(sys.argv)
    frm = PayForm()
    frm.showMaximized()
    sys.exit(app.exec_())

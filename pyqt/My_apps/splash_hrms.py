# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash_hrms.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_splashHRMS(object):
    def setupUi(self, splashHRMS):
        splashHRMS.setObjectName("splashHRMS")
        splashHRMS.setWindowModality(QtCore.Qt.ApplicationModal)
        splashHRMS.resize(473, 345)
        splashHRMS.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        splashHRMS.setWindowIcon(icon)
        splashHRMS.setStyleSheet("color:rgb(85, 255, 255);background-color:rgb(0, 85, 127)")
        self.progressBar_logo = QtWidgets.QProgressBar(splashHRMS)
        self.progressBar_logo.setGeometry(QtCore.QRect(0, 320, 471, 20))
        self.progressBar_logo.setProperty("value", 70)
        self.progressBar_logo.setObjectName("progressBar_logo")
        self.label = QtWidgets.QLabel(splashHRMS)
        self.label.setGeometry(QtCore.QRect(30, 30, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(splashHRMS)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 211, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../images/icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.progressBar_logo.raise_()
        self.label.raise_()

        self.retranslateUi(splashHRMS)
        QtCore.QMetaObject.connectSlotsByName(splashHRMS)

    def retranslateUi(self, splashHRMS):
        _translate = QtCore.QCoreApplication.translate
        splashHRMS.setWindowTitle(_translate("splashHRMS", "Dialog"))
        self.label.setText(_translate("splashHRMS", "HUMAN RESOURCE MANAGEMENT SYSTEM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    splashHRMS = QtWidgets.QDialog()
    ui = Ui_splashHRMS()
    ui.setupUi(splashHRMS)
    splashHRMS.show()
    sys.exit(app.exec_())


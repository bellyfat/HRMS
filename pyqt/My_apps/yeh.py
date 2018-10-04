print(self.i)

        nid = self.clients.lineEdit_IDNo_new.text()
        reg_date = self.clients.dateTimeEdit_stamp_new.text()
        reg_no = self.clients.lineEdit_regNo_new.text()
        hrm_code = self.clients.lineEdit_invoice_new.text()
        kra = self.clients.lineEdit_kra_pin_new.text()
        org_name= lineEdit_org_name_new.text()
        fn = self.clients.lineEdit_fn_repnew.text()
        mn = self.clients.lineEdit_mn_repnew.text()
        ln = self.clients.lineEdit_ln_repnew.text()
        phone = self.clients.lineEdit_tell_repnew.text()
        email = self.clients.lineEdit_email_repnew.text()
        force = self.clients.lineEdit_workforce_new.text()
        # address = self.clients.lineEdit_address.text()
        pay_rate = self.clients.comboBox_payrate_new.currentText()
        skill = self.clients.comboBox_skill_new.currentText()
        urole = 'Client'
        
        print(nid, reg_date, kra, fn, mn, ln, phone, email,  urole, pay_rate, skill,force)

        with sqlite3.connect('database_hrm.db') as dbconn:
            c = dbconn.cursor()
        c.execute(
            "INSERT INTO user_clients(National_ID, Registration_Date, KRA_PIN, Company_Name, First_Name, Middle_Name, Last_Name,Phone, Email,User_role,Payment_Rate,Skills,Workforce)VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (nid, reg_date, kra, org_name, fn, mn, ln, phone, email, urole, pay_rate, skill,force))
        QMessageBox.information(self, 'Success', "Info Added Successfully !!!", QMessageBox.Ok)
        print('Info Added Successfully')
        self.i += 1
        self.clients.lcdNumber_user_id.display(self.i)


        # self.clear1()
        dbconn.commit()
        c.close()
        dbconn.close()
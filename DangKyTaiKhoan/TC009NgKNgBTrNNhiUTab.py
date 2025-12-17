# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TC009NgKNgBTrNNhiUTab(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c009_ng_k_ng_b_tr_n_nhi_u_tab(self):
        driver = self.driver
        driver.get("http://hauiproj.somee.com/Default.aspx")
        driver.find_element_by_id("LinkDK").click()
        driver.get("http://hauiproj.somee.com/Dangky.aspx")
        driver.find_element_by_id("ContentPlaceHolder1_txtTaiKhoan").click()
        driver.find_element_by_id("ContentPlaceHolder1_txtTaiKhoan").clear()
        driver.find_element_by_id("ContentPlaceHolder1_txtTaiKhoan").send_keys("athwabdabn")
        driver.find_element_by_id("ContentPlaceHolder1_txtMatKhau").clear()
        driver.find_element_by_id("ContentPlaceHolder1_txtMatKhau").send_keys("adwhaj")
        driver.find_element_by_id("ContentPlaceHolder1_txtHoTen").clear()
        driver.find_element_by_id("ContentPlaceHolder1_txtHoTen").send_keys("thinh")
        driver.find_element_by_id("ContentPlaceHolder1_txtNamSinh").click()
        driver.find_element_by_id("ContentPlaceHolder1_txtNamSinh").clear()
        driver.find_element_by_id("ContentPlaceHolder1_txtNamSinh").send_keys("2025-12-18")
        driver.find_element_by_id("ContentPlaceHolder1_txtEmail").click()
        driver.find_element_by_id("ContentPlaceHolder1_txtEmail").clear()
        driver.find_element_by_id("ContentPlaceHolder1_txtEmail").send_keys("akwjdk")
        driver.find_element_by_id("ContentPlaceHolder1_txtSdt").click()
        driver.find_element_by_id("ContentPlaceHolder1_txtSdt").clear()
        driver.find_element_by_id("ContentPlaceHolder1_txtSdt").send_keys(u"ădadwva")
        driver.find_element_by_id("ContentPlaceHolder1_txtDiaChi").click()
        driver.find_element_by_id("ContentPlaceHolder1_txtDiaChi").clear()
        driver.find_element_by_id("ContentPlaceHolder1_txtDiaChi").send_keys(u"ădagwaw")
        driver.find_element_by_id("ContentPlaceHolder1_btDangky").click()
        driver.get("http://hauiproj.somee.com/Default.aspx")
        driver.get("http://hauiproj.somee.com/Default.aspx")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

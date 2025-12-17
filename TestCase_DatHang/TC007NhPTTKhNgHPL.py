# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TC007NhPTTKhNgHPL(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c007_nh_p_t_t_kh_ng_h_p_l(self):
        driver = self.driver
        driver.get("http://hauiproj.somee.com/Default.aspx")
        driver.find_element_by_xpath("//a[@id='HyperLink1']/li").click()
        driver.find_element_by_xpath("//a[@id='HyperLink2']/li").click()
        driver.get("http://hauiproj.somee.com/Kinhmat.aspx")
        driver.find_element_by_id("ContentPlaceHolder1_DataList1_Image1_1").click()
        driver.get("http://hauiproj.somee.com/ChiTietSanPham.aspx?ID=61")
        driver.find_element_by_id("ContentPlaceHolder1_Datalist1_txtSoLuong_0").click()
        driver.find_element_by_id("ContentPlaceHolder1_Datalist1_txtSoLuong_0").clear()
        driver.find_element_by_id("ContentPlaceHolder1_Datalist1_txtSoLuong_0").send_keys("20")
        driver.find_element_by_id("ContentPlaceHolder1_Datalist1_btnThemVaoGio_0").click()
        driver.get("http://hauiproj.somee.com/Giohang.aspx")
        driver.find_element_by_id("ContentPlaceHolder1_btnThanhToan").click()
        driver.get("http://hauiproj.somee.com/Dathang.aspx")
        driver.find_element_by_id("ContentPlaceHolder1_dtlThongTinUser_txtEmail_0").click()
        driver.find_element_by_id("ContentPlaceHolder1_dtlThongTinUser_txtEmail_0").clear()
        driver.find_element_by_id("ContentPlaceHolder1_dtlThongTinUser_txtEmail_0").send_keys("ihdbAAKEW2ISC")
        driver.find_element_by_id("ContentPlaceHolder1_dtlThongTinUser_txtDiaChi_0").click()
        driver.find_element_by_id("ContentPlaceHolder1_dtlThongTinUser_txtDiaChi_0").clear()
        driver.find_element_by_id("ContentPlaceHolder1_dtlThongTinUser_txtDiaChi_0").send_keys("NSVC")
        driver.find_element_by_id("ContentPlaceHolder1_dtlThongTinUser_txtGhiChu_0").click()
        driver.find_element_by_id("ContentPlaceHolder1_dtlThongTinUser_txtGhiChu_0").clear()
        driver.find_element_by_id("ContentPlaceHolder1_dtlThongTinUser_txtGhiChu_0").send_keys(u"thông tin email không hợp lệ!")
        driver.find_element_by_id("ContentPlaceHolder1_dtlThongTinUser_btnThanhToan_0").click()
        driver.find_element_by_id("ContentPlaceHolder1_LinkTrangChu").click()
        driver.get("http://hauiproj.somee.com/Default.aspx")
        driver.find_element_by_xpath("//a[@id='HyperLink1']/li").click()
    
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

from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import os, sys, time, unittest
from random import randint as rnd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.Login import LoginPage


class RegisterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.login_page = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get("https://demo.opencart.com/en-gb?route=account/login")
        time.sleep(1)


    def test_TC_LOG_01(self):
        input()
        self.login_page.set_password("test1234")
        self.login_page.click_login_button()
        time.sleep(1)
        error = self.login_page.get_error_email()
        self.assertIn("Email Address does not appear to be valid!" , error)
        time.sleep(0.5)

    def test_TC_LOG_02(self):
        self.login_page.set_email("test@email.com")
        self.login_page.click_login_button()
        time.sleep(1)
        error = self.login_page.get_error_password()
        self.assertIn("Password must be between 4 and 20 characters!" , error)
        time.sleep(0.5)

    def test_TC_LOG_03(self):
        self.login_page.set_email("emial.com")
        self.login_page.set_password("test1234")
        self.login_page.click_login_button()
        time.sleep(1)
        error  = self.login_page.get_error_email()
        self.assertIn("Email Address does not appear to be valid!" , error)
        time.sleep(0.5)

    def test_TC_LOG_04(self):
        self.login_page.set_email("test@email.com")
        self.login_page.set_password("test123")
        self.login_page.click_login_button()
        time.sleep(1)
        alert = self.login_page.get_alert()
        self.assertIn("Warning: No match for E-Mail Address and/or Password." , alert)
        time.sleep(0.5)


    def test_TC_LOG_05(self):
        self.login_page.set_email("teest@email.com")
        self.login_page.set_password("1234")
        self.login_page.click_login_button()
        time.sleep(1)
        alert = self.login_page.get_alert()
        self.assertIn("Warning: No match for E-Mail Address and/or Password." , alert)

    def test_TC_LOG_06(self):
        self.login_page.set_email("test@email.com")
        self.login_page.set_password("test123")
        for _ in range(6):
            self.login_page.click_login_button()
            time.sleep(0.5)
        alert = self.login_page.get_alert()
        self.assertnotIn("Warning: No match for E-Mail Address and/or Password." , alert)
        time.sleep(0.5)

    def test_TC_LOG_07(self):
        self.login_page.set_email("test@email.com")
        self.login_page.set_password("1234")
        self.login_page.click_login_button()
        time.sleep(1)
        title = self.login_page.get_page_title()
        self.assertIn("My Account" , title)
        time.sleep(0.5)

    def test_TC_LOG_08(self):
        self.login_page.click_register_link()
        time.sleep(1)
        title = self.login_page.get_page_title()
        self.assertIn("Register Account" , title)
        time.sleep(0.5)

    def test_TC_LOG_09(self):
        self.login_page.click_forgotten_password_link()
        time.sleep(1)
        title = self.login_page.get_page_title()
        self.assertIn("Forgotten Password" , title)
        time.sleep(0.5)


    def tearDown(self):
        self.driver.delete_cookie('demo.opencart.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
    




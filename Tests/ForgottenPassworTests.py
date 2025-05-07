from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import os, sys, time, unittest
from random import randint as rnd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.ForgottenPassword import ForgottenPasswordPage


class RegisterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.forgottenPassword_page = ForgottenPasswordPage(cls.driver)

    def setUp(self):
        self.driver.get("https://demo.opencart.com/en-gb?route=account/forgotten")
        time.sleep(1)

    def test_TC_FOR_01(self):
        self.forgottenPassword_page.click_continue_button()
        time.sleep(1)
        error = self.forgottenPassword_page.get_error_email()
        self.assertIn("E-Mail Address does not appear to be valid!" , error)
        time.sleep(0.5)

    def test_TC_FOR_02(self):
        self.forgottenPassword_page.set_email("test.com")
        self.forgottenPassword_page.click_continue_button()
        time.sleep(1)
        error = self.forgottenPassword_page.get_error_email()
        self.assertIn("E-Mail Address does not appear to be valid!" , error)
        time.sleep(0.5)

    def test_TC_FOR_03(self):
        self.forgottenPassword_page.set_email("teest@email.com")
        self.forgottenPassword_page.click_continue_button()
        time.sleep(1)
        alert = self.forgottenPassword_page.get_alert()
        self.assertIn("The E-Mail Address was not found in our records!" , alert)
        time.sleep(0.5)

    def test_TC_FOR_04(self):
        self.forgottenPassword_page.set_email("test@email.com")
        self.forgottenPassword_page.click_continue_button()
        time.sleep(1)
        title = self.forgottenPassword_page.get_title()
        self.assertIn("login" , title)
        time.sleep(0.5)

    def test_TC_FOR_05(self):
        self.forgottenPassword_page.set_email("t.e.s.t@email.com")
        self.forgottenPassword_page.click_continue_button()
        time.sleep(1)
        title = self.forgottenPassword_page.get_title()
        self.assertIn("login" , title)
        time.sleep(0.5)

    def test_TC_FOR_06(self):
        self.forgottenPassword_page.click_back_to_login_button()
        time.sleep(1)
        title = self.forgottenPassword_page.get_title()
        self.assertIn("login" , title)
        time.sleep(0.5)


    def tearDown(self):
        self.driver.delete_cookie('demo.opencart.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()

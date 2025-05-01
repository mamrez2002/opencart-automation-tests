from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import os, sys, time, unittest
from random import randint as rnd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.Register import RegisterPage


class RegisterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.register_page = RegisterPage(cls.driver)
        # cls.driver.get("https://demo.opencart.com/en-gb?route=account/register")
        # input()


    def setUp(self):
        self.driver.get("https://demo.opencart.com/en-gb?route=account/register")
        time.sleep(1)



    def test_TC_REG_01(self):

        input()

        self.register_page.click_continue_button()
        time.sleep(1)
        alert = self.register_page.get_alert()
        self.assertIn("Warning: You must agree to the Privacy Policy!", alert)
        time.sleep(0.5)

    def test_TC_REG_02(self):
        self.register_page.set_last_name("test")
        self.register_page.set_email("test@testemail.com")
        self.register_page.set_password("test1234")
        self.register_page.click_privacy_policy()
        self.register_page.click_continue_button()
        time.sleep(1)
        error = self.register_page.get_error_first_name()
        self.assertIn("First Name must be between 1 and 32 characters!", error)
        time.sleep(0.5)

    def test_TC_REG_03(self):
        self.register_page.set_first_name("test")
        self.register_page.set_email("test@testemail.com")
        self.register_page.set_password('test1234')
        self.register_page.click_privacy_policy()
        self.register_page.click_continue_button()
        time.sleep(1)
        error = self.register_page.get_error_last_name()
        self.assertIn('Last Name must be between 1 and 32 characters!' , error)
        time.sleep(0.5)

    def test_TC_REG_04(self):
        self.register_page.set_first_name("test")
        self.register_page.set_last_name('test')
        self.register_page.set_password('test1234')
        self.register_page.click_privacy_policy()
        self.register_page.click_continue_button()
        time.sleep(1)
        error = self.register_page.get_error_email()
        self.assertIn('E-Mail Address does not appear to be valid!' , error)
        time.sleep(0.5)


    def test_TC_REG_05(self):
        self.register_page.set_first_name("test")
        self.register_page.set_last_name('test')
        self.register_page.set_email("test@testemail.com")
        self.register_page.click_privacy_policy()
        self.register_page.click_continue_button()
        time.sleep(1)
        error = self.register_page.get_error_password()
        self.assertIn('Password must be between 4 and 20 characters!' , error)
        time.sleep(0.5)

    def test_TC_REG_06(self):
        self.register_page.set_first_name("TestNameTestNameTestNameTestNameTestName")
        self.register_page.set_last_name("test")
        self.register_page.set_email("test@testemail.com")
        self.register_page.set_password("test1234")
        self.register_page.click_privacy_policy()
        self.register_page.click_continue_button()
        time.sleep(1)
        error = self.register_page.get_error_first_name()
        self.assertIn("First Name must be between 1 and 32 characters!", error)
        time.sleep(0.5)

    def test_TC_REG_07(self):
        self.register_page.set_first_name("test")
        self.register_page.set_last_name("TestLastNameTestLastNameTestLastName")
        self.register_page.set_email("test@testemail.com")
        self.register_page.set_password('test1234')
        self.register_page.click_privacy_policy()
        self.register_page.click_continue_button()
        time.sleep(1)
        error = self.register_page.get_error_last_name()
        self.assertIn('Last Name must be between 1 and 32 characters!' , error)
        time.sleep(0.5)


    def test_TC_REG_08(self):
        pass

    def test_TC_REG_09(self):
        self.register_page.set_first_name("test")
        self.register_page.set_last_name("test")
        self.register_page.set_email("test@email.com")
        self.register_page.set_password("test1234")
        self.register_page.click_privacy_policy()
        self.register_page.click_continue_button()
        # time.sleep()
        alert = self.register_page.get_alert()
        self.assertIn(' Warning: E-Mail Address is already registered!', alert)
        time.sleep(0.5)

    def test_TC_REG_10(self):
        email = f"k{'.'* rnd(0,1)}a{'.'* rnd(0,2)}r{'.'* rnd(0,2)}y{'.'* rnd(0,2)}a{'.'* rnd(0,2)}a{'.'* rnd(0,2)}r@email.com"
        self.register_page.set_first_name("test")
        self.register_page.set_last_name("test")
        self.register_page.set_email(email)
        self.register_page.set_password("test1234")
        self.register_page.click_privacy_policy()
        self.register_page.click_continue_button()
        # time.sleep(12)
        alert = self.register_page.get_alert()
        self.assertIn(' Warning: E-Mail Address is already registered!', alert)
        time.sleep(0.5)


    def test_TC_REG_11(self):
        self.register_page.set_first_name("test")
        self.register_page.set_last_name("test")
        self.register_page.set_email('KARYAAR@email.com')
        self.register_page.set_password("test1234")
        self.register_page.click_privacy_policy()
        self.register_page.click_continue_button()
        # time.sleep(1)
        alert = self.register_page.get_alert()
        self.assertIn(' Warning: E-Mail Address is already registered!', alert)
        time.sleep(0.5)

    def test_TC_REG_12(self):
        self.register_page.set_first_name("test")
        self.register_page.set_last_name("test")
        self.register_page.set_email("test@email.com")
        self.register_page.set_password("12")
        self.register_page.click_privacy_policy()
        self.register_page.click_continue_button()
        time.sleep(1)
        error = self.register_page.get_error_password()
        self.assertIn('Password must be between 4 and 20 characters!' , error)
        time.sleep(0.5)

    def test_TC_REG_13(self):
        email = ""
        for i in range(8):
            email += chr(rnd(97, 122))
        email += "@email.com"
        self.register_page.set_first_name("test")
        self.register_page.set_last_name("test")
        self.register_page.set_email(email)
        self.register_page.set_password("test1234")
        self.register_page.click_privacy_policy()
        self.register_page.click_continue_button()
        time.sleep(1)
        title = self.register_page.get_page_title()
        self.assertIn('Your Account Has Been Created!', title)
        time.sleep(0.5)


    def test_TC_REG_14(self):
        self.register_page.click_login_link()
        time.sleep(1)
        title = self.register_page.get_page_title()
        self.assertIn('Account Login', title)

    def tearDown(self):
        self.driver.delete_cookie('demo.opencart.com')
        



if __name__ == "__main__":
    unittest.main()
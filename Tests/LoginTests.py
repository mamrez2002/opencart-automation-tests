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
        cls.register_page = LoginPage(cls.driver)


    def setUp(self):
        self.driver.get("https://demo.opencart.com/en-gb?route=account/login")
        time.sleep(1)





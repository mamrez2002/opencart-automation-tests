# Account Login
# https://demo.opencart.com/en-gb?route=account/login

import time
from selenium import webdriver


class LoginPage:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.email = '//*[(@id = "input-email")]'
        self.password = '//*[(@id = "input-password")]'
        self.login_button = '//*[(@id = "form-login")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]'
        self.forgotten_password_link = '//*[(@id = "form-login")]//a'
        self.register_link = '//a[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]'

        self.error_email = '//*[(@id = "error-email")]'
        self.error_password = '//*[(@id = "error-password")]'
        self.alert = '//*[(@id = "alert")]'

    def set_email(self, email):
        self.driver.find_element('xpath', self.email).send_keys(email)

    def set_password(self, password):
        self.driver.find_element('xpath', self.password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element('xpath', self.login_button).click()

    def click_forgotten_password_link(self):
        self.driver.find_element('xpath', self.forgotten_password_link).click()

    def click_register_link(self):
        self.driver.find_element('xpath', self.register_link).click()

    def get_error_email(self):
        return self.driver.find_element('xpath', self.error_email).text

    def get_error_password(self):
        return self.driver.find_element('xpath', self.error_password).text

    def get_alert(self):
        return self.driver.find_element('xpath', self.alert).text

    def get_page_title(self):
        return self.driver.title

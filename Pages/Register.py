# Register Account
# https://demo.opencart.com/en-gb?route=account/register

import time

class RegisterPage:
    def __init__(self , driver):
        self.driver = driver
        self.first_name = '//*[(@id = "input-firstname")]'
        self.last_name = '//*[(@id = "input-lastname")]'
        self.email = '//*[(@id = "input-email")]'
        self.password = '//*[(@id = "input-email")]'
        self.privacy_policy = '//*[contains(concat( " ", @class, " " ), concat( " ", "form-check-inline", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "form-check-input", " " ))]'
        self.continue_button = '//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]'
        self.login_link = '//*[(@id = "content")]//p//a'

        self.error_first_name = '//*[(@id = "error-firstname")]'
        self.error_last_name = '//*[(@id = "error-lastname")]'
        self.error_email = '//*[(@id = "error-email")]'
        self.error_password = '//*[(@id = "error-password")]'
        self.alert = '//*[(@id = "alert")]'


    def set_first_name(self, first_name):
        self.driver.find_element('xpath', self.first_name).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element('xpath', self.last_name).send_keys(last_name)

    def set_email(self, email):
        self.driver.find_element('xpath', self.email).send_keys(email)

    def set_password(self, password):
        self.driver.find_element('xpath', self.password).send_keys(password)

    def click_privacy_policy(self):
        self.driver.find_element('xpath', self.privacy_policy).click()

    def click_continue_button(self):
        self.driver.find_element('xpath', self.continue_button).click()

    def click_login_link(self):
        self.driver.find_element('xpath', self.login_link).click()

    def get_error_first_name(self):
        return self.driver.find_element('xpath', self.error_first_name).text

    def get_error_last_name(self):
        return self.driver.find_element('xpath', self.error_last_name).text

    def get_error_email(self):
        return self.driver.find_element('xpath', self.error_email).text

    def get_error_password(self):
        return self.driver.find_element('xpath', self.error_password).text

    def get_alert(self):
        return self.driver.find_element('xpath', self.alert).text

    def get_page_title(self):
        return self.driver.title
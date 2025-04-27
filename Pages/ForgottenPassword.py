# Forgot Your Password?
# https://demo.opencart.com/en-gb?route=account/forgotten


import time

class ForgottenPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.email = '//*[(@id = "input-email")]'
        self.continue_button = '//*[contains(concat( " ", @class, " " ), concat( " ", "btn-primary", " " ))]'
        self.back_to_login_button = '//*[(@id = "form-forgotten")]//*[contains(concat( " ", @class, " " ), concat( " ", "btn-light", " " ))]'

        self.error_email = '//*[(@id = "error-email")]'
        self.alert = '//*[(@id = "alert")]'

    def set_email(self, email):
        self.driver.find_element('xpath', self.email).send_keys(email)

    def click_continue_button(self):
        self.driver.find_element('xpath', self.continue_button).click()

    def click_back_to_login_button(self):
        self.driver.find_element('xpath', self.back_to_login_button).click()

    def get_error_email(self):
        return self.driver.find_element('xpath', self.error_email).text

    def get_alert(self):
        return self.driver.find_element('xpath', self.alert).text

    def get_page_title(self):
        return self.driver.title

    

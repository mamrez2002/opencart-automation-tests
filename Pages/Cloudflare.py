# cloudflare captcha bypass

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Cloudflare:
    def __init__(self, driver: uc.Chrome):
        self.driver = driver
        self.captcha_box = '//*[@id="qOTkU1"]/div/div'
        self.action = ActionChains(self.driver)

    def bypass_captcha(self):
        el = self.driver.find_elements(By.XPATH, self.captcha_box)
        location = el[0].location
        size = el[0].size


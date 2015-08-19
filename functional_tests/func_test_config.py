from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import os

__author__ = 'Aaron Olson <aaron.olson@agosto.com>'

class BaseTest(unittest.TestCase):

    def setUp(self):
        if os.path.exists('/usr/bin/phantomjs'):
            self.driver = webdriver.PhantomJS('/usr/bin/phantomjs')
        else:
            chromedriver = 'chromedriver'
            for root, dirs, files in os.walk(r'/Users'):
                if chromedriver in files:
                    local_driver_location = os.path.abspath(os.path.join(root, chromedriver))

            self.driver = webdriver.Chrome(local_driver_location)
        self.driver.implicitly_wait(1)
        self.base_url = "http://0.0.0.0:8080/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()
        if os.path.exists('/vagrant/functional_tests/.screenshots/'):
            self.screenshot_dir = "/vagrant/functional_tests/.screenshots/"
        else:
            self.screenshot_dir = "~/Pictures"
        self.driver.get(self.base_url + "")

        self.driver.find_element_by_id("submit-login").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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

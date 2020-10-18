import unittest
import time
from selenium import webdriver
import logging
import requests
from TestWebsitelogin.Pages.login_page import LoginPage
from config_login import ke
class TestAutomationPracticeLoginInvalid(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_login_invalid(self):
        logging.basicConfig(
            format='%(levelname)s: %(asctime)s: %(message)s',
            filename='/Users/siriqa/PycharmProjects/pythonProject/TestWebsitelogin/Reports/loggingfile.py',
            level=logging.DEBUG)
        driver = self.driver
        driver.get(ke['url_login'])
        # self.driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
        logging.info('Started LogIn')
        login = LoginPage(driver)
        login.enter_username(ke['invalid_email'])
        login.enter_password(ke['invalid_passwd'])
        login.click_submit()

        # after login failed
        try:
            actual_message_failed = driver.find_element_by_xpath('//*[@id="center_column"]/div[1]/p').text
            expected_message_failed = actual_message_failed[
                                  :actual_message_failed.find("There is 1 error") + len("There is 1 error")]
        except NoSuchElementException:
            actual_message_failed = ''
        assert (actual_message_failed == expected_message_failed), 'Login unsuccessful for another reason'
        print('{} user login is unsuccessful'.format(ke['email']))
        logging.info('Logging - Login is unsuccessful')
        driver.close()

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
    unittest.main()
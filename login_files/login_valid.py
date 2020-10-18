import unittest
import time
from selenium import webdriver
import logging
import requests
from TestWebsitelogin.Pages.login_page import LoginPage
from config_login import ke
#import XLUtils

class TestAutomationPracticeLoginValid(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    def test_login_valid(self):
        logging.basicConfig(
            format = '%(levelname)s: %(asctime)s: %(message)s',filename='/Users/siriqa/PycharmProjects/pythonProject/TestWebsitelogin/Reports/loggingfile.py',
            level=logging.DEBUG)

        driver = self.driver

        #code for DDT
        '''
        path = "/Users/siriqa/Documents/login_credentials.xlsx"
        rows = XLUtils.getRowCount(path,'Sheet1')

        for r in range(3,rows+1):
            email = XLUtils.readData(path,"Sheet1",r,1)
            passwd = XLUtils.readData(path,"Sheet1",r,2)
        
        try:
            driver.get("http://automationpractice.com/index.php?controller=authentication")
            #self.driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
            logging.info('Started LogIn')
            login = LoginPage(driver)
            login.enter_username(email)
            login.enter_password(passwd)
            login.click_submit()
        
        '''
        try:
            driver.get(ke['url_login'])
            #self.driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
            logging.info('Started LogIn')
            login = LoginPage(driver)
            login.enter_username(ke['email'])
            login.enter_password(ke['passwd'])
            login.click_submit()

            # after login
            time.sleep(3)
            try:
                actual_message = driver.find_element_by_xpath('//*[@id="center_column"]/p').text
                expected_message = "Welcome to your account. Here you can manage all of your personal information and orders."
            except NoSuchElementException:
                actual_message = ''

            #self.assertEqual(actual_message, expected_message)
            assert(actual_message == expected_message),'Login failed with Invalid Credentials'
            print('{} user login is successful'.format(ke['email']))
            logging.info('Logging - Login is successful')

        except requests.HTTPError as exception:
            print(exception)
        self.driver.close()

if __name__ == '__main__':

    driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner(output = '/Users/siriqa/PycharmProjects/pythonProject/TestWebsitelogin/Reports'))
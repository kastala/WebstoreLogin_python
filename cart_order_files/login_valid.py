import unittest
import time
from selenium import webdriver
import logging
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import TimeoutException
from config_login import ke

class TestAutomationPracticeLoginValid(unittest.TestCase):

    '''
    def setUp(self):
        driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
        driver.get(ke['url_login'])

    def tearDown(self):
        driver.quit()
    '''
    def test_login_valid(self):
        logging.basicConfig(
            filename='/Users/siriqa/PycharmProjects/pythonProject/TestWebsitelogin/Reports/loggingfile.py',
            level=logging.DEBUG)
        driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
        driver.get(ke['url_login'])
        driver.find_element_by_id('email').send_keys(ke['email'])
        driver.find_element_by_id('passwd').send_keys(ke['passwd'])
        driver.find_element_by_id('SubmitLogin').click()

        # after login
        time.sleep(3)
        driver.get(ke['url_afterlogin'])
        actual_message = driver.find_element_by_xpath('//*[@id="center_column"]/p').text
        expected_message = "Welcome to your account. Here you can manage all of your personal information and orders."
        # print(actual_message)

        #self.assertEqual(actual_message, expected_message)
        if (actual_message == expected_message):
            print('Login is Successful')
        else:
            print('Login failed, Inavid Credentials')
        # self.assertNotEqual(actual_message,expected_message,"Login is NOT Successful")



if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
    unittest.main()
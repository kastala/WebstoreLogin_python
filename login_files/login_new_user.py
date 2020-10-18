import unittest
import time
from selenium import webdriver
import logging
from config_login import ke

class TestAutomationPracticeLoginNewUser(unittest.TestCase):
    ''' def setUp(self):
        driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
        driver.get(ke['url_login'])

    def tearDown(self):
        driver.quit()
    '''
    def test_new_user(self):
        logging.basicConfig(
            format='%(levelname)s: %(asctime)s: %(message)s',
            filename='/Users/siriqa/PycharmProjects/pythonProject/TestWebsitelogin/Reports/loggingfile.py',
            level=logging.DEBUG)
        driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
        driver.maximize_window()
        driver.get(ke['url_login'])
        driver.find_element_by_id('email_create').send_keys(ke['email_create'])
        driver.find_element_by_id('SubmitCreate').click()
        #after clicking "Create an Account"
        #driver.get(ke['url_new_user'])
        driver.implicitly_wait(5)
        driver.find_element_by_id('id_gender2').click()
        driver.find_element_by_id('customer_firstname').send_keys(ke['first_name'])
        driver.find_element_by_id('customer_lastname').send_keys(ke['last_name'])
        driver.find_element_by_id('passwd').send_keys(ke['password'])
        pass_length = len(ke['password'])
        assert (pass_length >= 5), 'Min. of 5 characters for password is required'
        print("password restrictions matched")


        #DOB
        driver.find_element_by_xpath('//*[@id="days"]/option[{}]'.format(ke['dob_day'])).click()
        driver.find_element_by_xpath('//*[@id="months"]/option[{}]'.format(ke['dob_month'])).click()
        driver.find_element_by_xpath('//*[@id="years"]/option[{}]'.format(ke['dob_year'])).click()
        #driver.find_element_by_xpath('//*[@id="months"]/option[2]').click()
        #driver.find_element_by_xpath('//*[@id="years"]/option[15]').click()


        #Address
        driver.find_element_by_id('firstname').send_keys(ke['address_first_name'])
        driver.find_element_by_id('lastname').send_keys(ke['address_last_name'])
        driver.find_element_by_id('company').send_keys(ke['address_companyname'])
        driver.find_element_by_id('address1').send_keys(ke['address_address1'])
        driver.find_element_by_id('address2').send_keys(ke['address_address2'])
        driver.find_element_by_id('city').send_keys(ke['address_city'])
        #driver.find_element_by_id('id_state/option[{}]'.format(ke['address_state'])).click()
        driver.find_element_by_xpath('//*[@id="id_state"]/option[6]').click()
        driver.find_element_by_id('postcode').send_keys(ke['address_zip'])
        #driver.find_element_by_id('id_country/option[{}]'.format(ke['address_country'])).click()
        #driver.find_element_by_xpath('//*[@id="id_country"]/option[2]').click()
        driver.find_element_by_xpath('//*[@id="other"]').send_keys(ke['address_additional_info'])
        driver.find_element_by_xpath('//*[@id="phone"]').send_keys(ke['address_home_phone'])
        driver.find_element_by_xpath('//*[@id="phone_mobile"]').send_keys(ke['address_mobile_phone'])
        driver.find_element_by_xpath('//*[@id="alias"]').send_keys(ke['address_alias'])
        driver.find_element_by_xpath('//*[@id="submitAccount"]/span').click()
        time.sleep(6)
        driver.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
    unittest.main()
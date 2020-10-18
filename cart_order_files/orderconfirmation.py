import unittest
import time
from selenium import webdriver
import logging
from TestWebsitelogin.Pages.login_page import LoginPage
from TestWebsitelogin.Pages.myaccount_page import MyAccountPage
from TestWebsitelogin.Pages.add_items_to_cart_from_search_page import AddItemsToCartPage
from TestWebsitelogin.Pages.cart_page import MyCartPage
from TestWebsitelogin.Pages.checkout_page import CheckoutPage
from TestWebsitelogin.Pages.checkout_addresspage import CheckoutAddress
from TestWebsitelogin.Pages.checkout_shippingpage import CheckoutShipping
from TestWebsitelogin.Pages.checkout_paymentpage import CheckoutPayment
from TestWebsitelogin.Pages.checkout_confirmpage import CheckoutConfirm
from config_login import ke

class TestAutomationPracticeOrderConmpletion(unittest.TestCase):

        @classmethod
        def setUp(cls):
            cls.driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(5)

        @classmethod
        def tearDown(cls):
            cls.driver.quit()

        def test_order(self):
            logging.basicConfig(
                format='%(levelname)s: %(asctime)s: %(message)s',
                filename='/Users/siriqa/PycharmProjects/pythonProject/TestWebsitelogin/Reports/loggingfile.py',
                level=logging.DEBUG)
            driver = self.driver
            driver.get(ke['url_afterlogin'])
            # logging in
            login = LoginPage(driver)
            login.enter_username(ke['email'])
            login.enter_password(ke['passwd'])
            login.click_submit()
            time.sleep(6)

            # searching item 1

            myaccount = MyAccountPage(driver)
            myaccount.search_item(ke['search1_top'])
            myaccount.search_submit()

            # Add to cart
            addtocart = AddItemsToCartPage(driver)
            addtocart.item_selection()
            time.sleep(5)
            addtocart.item_add_to_cart()
            logging.info('{} Item added to cart successfully'.format(ke['search1_top']))
            time.sleep(5)
            addtocart.continue_shopping()
            time.sleep(5)

            # searching item 2
            # myaccount = MyAccountPage(driver)
            driver.find_element_by_xpath('//*[@id="search_query_top"]').clear()
            myaccount.search_item(ke['search2_top'])
            myaccount.search_submit()
            logging.info('search successful')

            # Add to cart
            # addtocart = AddItemsToCartPage(driver)
            addtocart.item_selection()
            time.sleep(5)
            addtocart.item_add_to_cart()
            time.sleep(5)
            addtocart.continue_shopping()
            time.sleep(10)
            count_addcart = driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[1]').text
            # print(count_addcart)
            logging.info('{} Item added to cart successfully'.format(ke['search2_top']))

            # cartpage Summary quantity validation
            mycartsummary = MyCartPage(driver)
            mycartsummary.cart_click()
            time.sleep(5)
            '''count_cartpage = driver.find_element_by_id('summary_products_quantity').text
            count_cartpagesummary = count_cartpage.split()[0]
            # print(count_cartpagesummary)
            if (count_addcart == count_cartpagesummary):
                print("No. of items added to cart are same in Cart Summary page")
                logging.info('Logging: Items quantity added is not same in Cart Summary page')
            else:
                print("No. of items added to cart are not same in Cart Summary page")
                logging.error('Logging: Items quantity added is not same in Cart Summary page')
            '''

            #Initial checkout page
            time.sleep(3)
            mycheckout = CheckoutPage(driver)
            mycheckout.click_proceed_to_checkout()

            #Address checkout page
            time.sleep(3)
            myaddresscheckout = CheckoutAddress(driver)
            #myaddresscheckout.enter_comment_info("Please give a phone call")
            driver.find_element_by_xpath('//*[@id="ordermsg"]/textarea').send_keys("please call")
            myaddresscheckout.click_proceed_address()
            time.sleep(7)

            #Shipping Checkout page
            myshippingcheckout = CheckoutShipping(driver)
            myshippingcheckout.accept_terms_conditions()
            myshippingcheckout.click_proceed_shipping()

            #Payment Checkout Page
            mycheckoutpayment = CheckoutPayment(driver)
            #print(ke['payment_type'])
            if(ke['payment_type'] == "Pay by bank wire"):
                mycheckoutpayment.click_pay_wire()
            else:
                mycheckoutpayment.click_pay_check()
            time.sleep(5)
            #checkout confirm order
            mycheckoutconfirm = CheckoutConfirm(driver)
            mycheckoutconfirm.confirm_order_final()

            #validating order reference in Order History Page

            your_order = driver.find_element_by_xpath('//*[@id="center_column"]/div').text
            reference_key = "reference"
            reference_id_sentence = your_order[your_order.find(reference_key) + len(reference_key):]
            reference_id = reference_id_sentence.split()[0]
            driver.find_element_by_xpath('//*[@id="footer"]/div/section[5]/h4/a').click()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/ul/li[1]/a/span').click()
            time.sleep(5)
            your_order_history_text = driver.find_element_by_xpath('//*[@id="center_column"]').text
            your_order_history_id = your_order_history_text[
                                    :your_order_history_text.find(reference_id) + len(reference_id)]
            your_order_history_id_reference = your_order_history_id.split()[-1]
            if (your_order_history_id_reference == reference_id):
                print("Order is saved in Order History Page")
            else:
                print("Order is not present in Order History Page")
        

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
    unittest.main()
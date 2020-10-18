import unittest
import time
from selenium import webdriver
import logging
from TestWebsitelogin.Pages.login_page import LoginPage
from TestWebsitelogin.Pages.myaccount_page import MyAccountPage
from TestWebsitelogin.Pages.add_items_to_cart_from_search_page import AddItemsToCartPage
from TestWebsitelogin.Pages.cart_page import MyCartPage
from config_login import ke

class TestAutomationPracticeSearchAddtocart(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="/Applications/chromedriver")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


    def test_search_addtocart(self):

        logging.basicConfig(
            format='%(levelname)s: %(asctime)s: %(message)s',
            filename='/Users/siriqa/PycharmProjects/pythonProject/TestWebsitelogin/Reports/loggingfile.py',
            level=logging.DEBUG)
        time.sleep(5)
        driver = self.driver
        driver.get(ke['url_login'])
        logging.info('Started LogIn')

        #logging in
        login = LoginPage(driver)
        login.enter_username(ke['email'])
        login.enter_password(ke['passwd'])
        login.click_submit()
        time.sleep(6)

        #searching item 1

        myaccount = MyAccountPage(driver)
        myaccount.search_item(ke['search1_top'])
        myaccount.search_submit()

        #Add to cart
        addtocart = AddItemsToCartPage(driver)
        addtocart.item_selection()
        #price_each_item = driver.find_element_by_id('our_price_display').text
        #quantity_each_item = driver.find_element_by_id(quantity_wanted).text
        time.sleep(5)

        addtocart.item_add_to_cart()
        logging.info('{} Item added to cart successfully'.format(ke['search1_top']))
        time.sleep(5)
        addtocart.continue_shopping()
        time.sleep(5)

        # searching item 2
        #myaccount = MyAccountPage(driver)
        driver.find_element_by_xpath('//*[@id="search_query_top"]').clear()
        myaccount.search_item(ke['search2_top'])
        myaccount.search_submit()
        logging.info('search successful')

        # Add to cart
        #addtocart = AddItemsToCartPage(driver)
        addtocart.item_selection()
        time.sleep(5)
        addtocart.item_add_to_cart()
        time.sleep(5)
        total_price_afteradding_items = driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[1]/span').text
        time.sleep(5)

        addtocart.continue_shopping()
        time.sleep(10)
        count_addcart = driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a/span[1]').text
        #print(count_addcart)
        time.sleep(5)
        logging.info('{} Item added to cart successfully'.format(ke['search2_top']))

        #cartpage Summary quantity,prices validation
        mycartsummary = MyCartPage(driver)
        mycartsummary.cart_click()
        time.sleep(5)
        price_total = driver.find_element_by_id('total_product').text
        count_cartpage = driver.find_element_by_id('summary_products_quantity').text
        count_cartpagesummary = count_cartpage.split()[0]


        #Assertions
        assert(count_addcart == count_cartpagesummary),'No. of items added to cart are not same in Cart Summary page'
        print("No. of items added to cart{0} are same in Cart Summary page{1}".format(count_addcart,count_cartpagesummary))
        logging.info('Logging: Items quantity added is  same in Cart Summary page')

        assert(total_price_afteradding_items == price_total),'Total item prices added are not same in Cart Summary page'
        print("Total price of items {0} is same as Total products price{1} in Cart summary page".format(total_price_afteradding_items, price_total))
        logging.info('Logging: Items total prices is  same as Total products prices in Cart Summary page')

        driver.close()



if __name__ == '__main__':
    unittest.main()
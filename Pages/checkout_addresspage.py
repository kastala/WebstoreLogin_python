class CheckoutAddress():
    def __init__(self, driver):
        self.driver = driver

        #self.comment_info_textbox_xpath = '//*[@id="ordermsg"]/textarea'
        self.proceed_address_button_xpath = '//*[@id="center_column"]/form/p/button/span'

    #def enter_comment_info(self,'//*[@id="ordermsg"]/textarea'):
        #self.driver.find_element_by_xpath(self.comment_info_textbox_xpath).clear()
        #self.driver.find_element_by_xpath(self.comment_info_textbox_xpath).send_keys('//*[@id="ordermsg"]/textarea')

    def click_proceed_address(self):
        self.driver.find_element_by_xpath(self.proceed_address_button_xpath).click()


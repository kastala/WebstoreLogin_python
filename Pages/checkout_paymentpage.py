class CheckoutPayment():
    def __init__(self, driver):
        self.driver = driver

        self.pay_bank_wire_button_xpath = '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a'
        self.pay_check_button_xpath = '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a'

    def click_pay_wire(self):
        self.driver.find_element_by_xpath(self.pay_bank_wire_button_xpath).click()

    def click_pay_check(self):
        self.driver.find_element_by_xpath(self.pay_check_button_xpath).click()


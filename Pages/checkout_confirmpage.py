class CheckoutConfirm():
    def __init__(self, driver):
        self.driver = driver

        self.confirm_order_button_xpath = '//*[@id="cart_navigation"]/button/span'

    def confirm_order_final(self):
        self.driver.find_element_by_xpath(self.confirm_order_button_xpath).click()
class CheckoutShipping():
    def __init__(self, driver):
        self.driver = driver

        self.accept_tc_checkbox_id = 'cgv'
        self.proceed_shipping_button_xpath = '//*[@id="form"]/p/button/span'

    def accept_terms_conditions(self):
        self.driver.find_element_by_id(self.accept_tc_checkbox_id).click()

    def click_proceed_shipping(self):
        self.driver.find_element_by_xpath(self.proceed_shipping_button_xpath).click()


class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver

        self.proceed_button_xpath = '//*[@id="center_column"]/p[2]/a[1]/span'



    def click_proceed_to_checkout(self):
        self.driver.find_element_by_xpath(self.proceed_button_xpath).click()


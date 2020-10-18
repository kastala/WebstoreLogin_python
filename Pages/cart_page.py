class MyCartPage():
    def __init__(self, driver):
        self.driver = driver

        self.cart_icon_click = '//*[@id="header"]/div[3]/div/div/div[3]/div/a/b'

    def cart_click(self):
        self.driver.find_element_by_xpath(self.cart_icon_click).click()
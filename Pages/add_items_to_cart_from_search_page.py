class AddItemsToCartPage():
    ac = 0
    def __init__(self, driver):
        self.driver = driver

        self.image_xpath_item_click = '//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img'
        self.add_to_cart_id_click = "add_to_cart"
        self.continue_shopping_click = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span'


    def item_selection(self):
        self.driver.find_element_by_xpath(self.image_xpath_item_click).click()



    def item_add_to_cart(self):

        self.driver.find_element_by_id(self.add_to_cart_id_click).click()



    def continue_shopping(self):
        self.driver.find_element_by_xpath(self.continue_shopping_click).click()
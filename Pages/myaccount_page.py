class MyAccountPage():
    def __init__(self, driver):
        self.driver = driver

        self.seachitems_textbox_id = 'search_query_top'
        self.search_xpath_click = '//*[@id="searchbox"]/button'

    def search_item(self, search_query_top):
        self.driver.find_element_by_id(self.seachitems_textbox_id).clear()
        self.driver.find_element_by_id(self.seachitems_textbox_id).send_keys(search_query_top)



    def search_submit(self):
        self.driver.find_element_by_xpath(self.search_xpath_click).click()
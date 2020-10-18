class LoginPage():
    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_id = "email"
        self.password_textbox_id = "passwd"
        self.submit_button_id = "SubmitLogin"

    def enter_username(self,email):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(email)

    def enter_password(self,passwd):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(passwd)

    def click_submit(self):
        self.driver.find_element_by_id(self.submit_button_id).click()
    

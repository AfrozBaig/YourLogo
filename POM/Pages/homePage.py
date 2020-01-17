class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.sign_out_linkText = "Sign out"

    def click_sign_out(self):
        self.driver.find_element_by_link_text(self.sign_out_linkText).click()

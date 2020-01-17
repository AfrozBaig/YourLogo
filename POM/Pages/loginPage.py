class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.sign_in_button_linkText = "Sign in"
        self.email_textbox_id = "email"
        self.password_textbox_id = "passwd"
        self.login_button_id = "SubmitLogin"

    def click_sign_in_link(self):
        self.driver.find_element_by_link_text(self.sign_in_button_linkText).click()

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id ).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element_by_id(self.login_button_id).click()

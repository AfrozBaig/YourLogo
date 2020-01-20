from selenium import webdriver
import time
import unittest
from POM.Pages.loginPage import LoginPage
from POM.Pages.homePage import HomePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Karan Singh Bais/Downloads/chromedriver_win32"
                                                      "/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("http://automationpractice.com/")

        login = LoginPage(driver)
        login.click_sign_in_link()
        login.enter_email("test@123z.com")
        login.enter_password("12345")
        login.click_sign_in()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        home = HomePage(cls.driver)
        home.click_sign_out()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:/Users/Karan Singh Bais/PycharmProjects/YourLogo/Reports/ExecutionReport.html'))

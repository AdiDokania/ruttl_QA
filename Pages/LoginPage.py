from selenium.webdriver.common.by import By
from Configuration.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    Email = (By.NAME, 'email')
    Password = (By.NAME, 'password')
    Sign_in = (By.XPATH, "//button[text()='Sign in']")

    def __init__(self, driver):
        super().__init__(driver)

    def setEmailAddress(self):
        self.do_send_keys(self.Email, TestData.EmailAddress)
        self.do_send_keys(self.Password, TestData.Password)
        self.do_click(self.Sign_in)

    def verifyPageTitle(self):
        return self.get_title()

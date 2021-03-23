import time

from selenium.webdriver.common.by import By
from Configuration.config import TestData
from Pages.BasePage import BasePage

class ForgetPasswordPage(BasePage):

    forgetPasswordBtn = (By.LINK_TEXT, "Forgot password?")
    emailAddress = (By.ID, 'email')
    forgetText = (By.XPATH, "//h3[text() ='Forgot your password?']")
    resetBtn = (By.XPATH, "//button[text()='Reset Password']")
    emailMessage = (By.XPATH, "//p[contains(text(),'password')]")

    def __init__(self, driver):
        super().__init__(driver)

    def verifyPageTitle(self):
            return self.get_title()

    def clickForgetPasswordBtn(self):
        self.do_click(self.forgetPasswordBtn)

    def enterEmailAddress(self):
        self.do_send_keys(self.emailAddress, TestData.EmailAddress)
        self.do_click(self.resetBtn)

    def verifyPage(self):
        return self.get_element_text(self.forgetText)

    def verifyEmailSent(self):
        return self.get_element_text(self.emailMessage)
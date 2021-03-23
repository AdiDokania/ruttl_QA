import time
from behave import *
from selenium import webdriver
from Pages.ForgetPasswordPage import ForgetPasswordPage
from Utilities.CustomLogger import LogGen
from Configuration.config import TestData

global fppage
global fppage1
mylogger = LogGen.logger()


@given('Launch browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    mylogger.info("**** Driver Initialized ****")
    time.sleep(10)
    context.driver.maximize_window()
    context.driver.get(TestData.BASEURL)
    time.sleep(10)
    mylogger.info("** URL Launched **")


@when('Verify page title')
def verify_Page_Title(context):
    fppage = ForgetPasswordPage(context.driver)
    title = fppage.verifyPageTitle()
    if title == TestData.ExpectedTitle:
        assert True
        context.driver.save_screenshot(".\\Screenshots\\LoginPageTitle1.png")
        mylogger.info("** Title Verified **")
    else:
        context.driver.save_screenshot(".\\Screenshots\\LoginPageTitle1.png")
        mylogger.info("** Title Not Verified **")
        assert False


@then('Go to forget password page')
def navigate_ForgtePassword_Page(context):
    fppage = ForgetPasswordPage(context.driver)
    fppage.clickForgetPasswordBtn()
    time.sleep(2)
    PageText = fppage.verifyPage()
    if PageText == TestData.ForgetPasswordPageText:
        assert True
        context.driver.save_screenshot(".\\Screenshots\\ForgetPasswordPageText.png")
        mylogger.info("** Page Verified **")
    else:
        mylogger.info("** Page Not Verified **")
        context.driver.save_screenshot(".\\Screenshots\\ForgetPasswordPageText.png")
        assert False


@then('Verify Forget Password')
def verify_ForgetPasword_Functionality(context):
    fppage = ForgetPasswordPage(context.driver)
    fppage.enterEmailAddress()
    time.sleep(10)
    EmailSentText = fppage.verifyEmailSent()
    if EmailSentText == TestData.EmailMessage:
        assert True
        context.driver.save_screenshot(".\\Screenshots\\EmailMessageText.png")
        mylogger.info("** Email Text Verified **")
    else:
        context.driver.save_screenshot(".\\Screenshots\\EmailMessageText.png")
        mylogger.info("** Email Text Not Verified **")
        assert False

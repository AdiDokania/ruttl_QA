import time
from behave import *
from selenium import webdriver


from Utilities.CustomLogger import LogGen
from Configuration.config import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage

global lpage
global hpage
mylogger = LogGen.logger()


@given('Launch the browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    mylogger.info("**** Driver Initialized ****")
    time.sleep(10)
    context.driver.maximize_window()
    context.driver.get(TestData.BASEURL)
    time.sleep(10)
    mylogger.info("** URL Launched **")


@when('Verify the page title')
def verify_Page_Title(context):
    lpage = LoginPage(context.driver)
    title = lpage.verifyPageTitle()
    if title == TestData.ExpectedTitle:
        assert True
        context.driver.save_screenshot(".\\Screenshots\\LoginPageTitle.png")
        mylogger.info("** Title Verified **")
    else:
        mylogger.info("** Title Not Verified **")
        assert False
        context.driver.save_screenshot(".\\Screenshots\\LoginPageTitle.png")
        time.sleep(1)


@then('Login to the Application')
def set_Email_Address(context):
    mylogger.info("** Passing Credentials **")
    lpage = LoginPage(context.driver)
    lpage.setEmailAddress()


@then('Verify Login Credentials')
def verify_Login_Credentials(context):
    hpage = HomePage(context.driver)
    hpage.verifyHomePageCredentials()
    displayName = hpage.getDisplayName()
    if displayName == TestData.UserName:
        assert True
        context.driver.save_screenshot(".\\Screenshots\\LoginDisplayName.png")
        mylogger.info("** Person Verified **")
    else:
        mylogger.info("** Person Not Verified **")
        assert False
        context.driver.save_screenshot(".\\Screenshots\\LoginDisplayName.png")


@then('Click on Projects')
def click_Project(context):
    time.sleep(2)
    global hpage
    hpage = HomePage(context.driver)
    hpage.clickProjects()


@then('Create new Project')
def create_Project(context):
    time.sleep(2)
    global hpage
    hpage = HomePage(context.driver)
    hpage.createNewProject()

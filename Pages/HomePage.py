import time

from selenium.webdriver.common.by import By
from Configuration.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):

    Avatar = (By.XPATH, "//div[@class ='add-project-button-container']/following::div[1]/button")
    AccountSettings = (By.LINK_TEXT, "Account Settings")
    DisplayName = (By.ID, "displayName")
    Projects = (By.XPATH, "//div[@id='main']/nav/div/div/a[@href='/projects']")
    CreateProjects = (By.XPATH, "//button[text()='+ Create Project']")
    ProjectName = (By.ID, "title")
    CreateButton = (By.XPATH, "//button[text()='Create Project'][@type ='submit']")
    EnterWebURL = (By.XPATH, "//input[@placeholder='Enter web URL']")
    AddPage = (By.XPATH, "//input[@placeholder='Enter web URL']/following::button[text()='Add Page']")
    ViewPage = (By.XPATH, "//input[@name ='pTitle']/preceding::a[text()='View page']")
    LaterBtn =(By.XPATH, "//button[text()='Later']")
    NoThanksBtn =(By.XPATH, "//button[text()='No Thanks']")
    CardClick = (By.XPATH, "//input[@name ='pTitle']")

    def __init__(self, driver):
        super().__init__(driver)

    def verifyHomePageCredentials(self):
        self.do_click(self.Avatar)
        self.do_click(self.AccountSettings)

    def getDisplayName(self):
        return self.get_element_value(self.DisplayName)

    def clickProjects(self):
        self.do_click(self.Projects)
        time.sleep(10)
        self.do_click(self.LaterBtn)

    def createNewProject(self):
        self.do_click(self.CreateProjects)
        self.do_send_keys(self.ProjectName, TestData.ProjectName)
        self.do_click(self.CreateButton)
        self.do_send_keys(self.EnterWebURL, TestData.WebsiteURL)
        self.do_click(self.AddPage)
        time.sleep(10)
        self.do_click(self.NoThanksBtn)
        time.sleep(2)
        self.mouse_hover(self.CardClick)
        self.mouse_hover(self.ViewPage)
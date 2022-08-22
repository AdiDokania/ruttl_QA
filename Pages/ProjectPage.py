from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class ProjectPage(BasePage):

    PreviewMode = (By.XPATH, '//*[@id="web-views-menu"]/li[2]/button')
    EditMode = (By.XPATH, '//*[@id="web-views-menu"]/li[3]/button')
    MobileView = (By.XPATH, "//*[@class ='c-info__share']/preceding::li[1]/button")
    WebsiteView = (By.XPATH, "//*[@class ='c-info__share']/preceding::li[2]/button")
    AllProjectLink = (By.XPATH, "//button[text()= 'Version 1']/preceding::a")
    Version1 = (By.XPATH, "//button[text()= 'Version 1']")
    AllProjectLink = (By.XPATH, "//button[text()= 'Version 1']/preceding::a")

    def __init__(self, driver):
        super().__init__(driver)
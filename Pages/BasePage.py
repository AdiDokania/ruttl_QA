import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

"""This class is the Parent of all Pages"""
"""It contains all generic method"""


class BasePage:

    def __init__(context, driver):
        context.driver = driver

    def do_click(context, by_locator):
        WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(context, by_locator, text):
        WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(context, by_locator):
        element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_element_value(context, by_locator):
        element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute("value")

    def is_visible(context, by_locator):
        element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def dropdown(context, by_locator, text):
        element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(by_locator))
        time.sleep(5)
        sel = Select(element)
        time.sleep(5)
        sel.select_by_visible_text(text)

    def get_title(context):
        return context.driver.title

    def tab_handle(context):
        allTabs = context.driver.window_handles
        for tabs in allTabs:
            context.driver.switch_to.window(tabs)
            print(context.driver.current_url)
            if (context.driver.current_url == ""):
                time.sleep(10)
                get_title = context.driver.title
                print(get_title)

    def handle_alert(context):
        alert = context.driver.switch_to.alert()
        print(alert.text)
        time.sleep(10)
        alert.send_keys("B" + Keys.TAB + "G")
        alert.accept()

    def mouse_hover(context, by_locator):
        element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action = ActionChains(context.driver)
        action.move_to_element(element).click()
        action.perform()
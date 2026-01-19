from selenium.webdriver.common.by import By

from Pytest_demo1.shope import ShopePage
from Pytest_demo1.util.browserUtil import BrowserUtils


class LoginPage(BrowserUtils):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.signin_button = (By.ID, "signInBtn")

    def login(self, username, password):
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")

        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.signin_button).click()
        shopePage = ShopePage(self.driver)
        return shopePage



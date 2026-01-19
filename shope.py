from selenium.webdriver.common.by import By

from Pytest_demo1.checkout_conformation import CheckoutConformation
from Pytest_demo1.util.browserUtil import BrowserUtils


class ShopePage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shope_link = (By.CSS_SELECTOR, 'a[href*="shop"]')
        self.add_cart = (By.XPATH, '//div[@class="card h-100"]')
        self.checkbox = (By.CSS_SELECTOR, "a[class*=primary]")



    def shop_page(self,product):

        self.driver.find_element(*self.shope_link).click()

        products = self.driver.find_elements(* self.add_cart)

        for item in products:
            productName = item.find_element(By.XPATH, 'div/h4/a').text
            if productName == "Blackberry":
                item.find_element(By.XPATH, 'div/button').click()

    def gotocart(self):
        self.driver.find_element(*self.checkbox).click()
        checkout_conformation = CheckoutConformation(self.driver)
        return checkout_conformation



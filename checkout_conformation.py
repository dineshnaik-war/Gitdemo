from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pytest_demo1.util.browserUtil import BrowserUtils


class CheckoutConformation(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, 'button[class*="success"]')
        self.country_input = (By.CSS_SELECTOR, "#country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.XPATH, '//div[@class="checkbox checkbox-primary"]')
        self.submit = (By.CSS_SELECTOR, '[type="submit"]')
        self.success_message = (By.CLASS_NAME, "alert-success")



    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()



    def enter_deliveryaddress(self,countryName):
        wait = WebDriverWait(self.driver, 10)

        self.driver.find_element(*self.country_input).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit).click()


    def validate_order(self):

        successText = self.driver.find_element(self.success_message).text
        assert 'Success! Thank you!' in successText



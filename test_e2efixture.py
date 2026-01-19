import json
import os

import sys

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pytest_demo1.login import LoginPage
from Pytest_demo1.shope import ShopePage


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
test_data_file = os.path.join(BASE_DIR, "..", "data", "test_e2efixture.json")
with open(test_data_file) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_items",test_list)
def test_e2e(browserInstance,test_list_items):
    driver = browserInstance
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    shopePage = loginPage.login(test_list_items["userEmail"],test_list_items["userPassword"])
    shopePage.shop_page(test_list_items["productName"])
    checkout_conformation = shopePage.gotocart()
    checkout_conformation.checkout()
    checkout_conformation.enter_deliveryaddress('Ind')
    checkout_conformation.validate_order()


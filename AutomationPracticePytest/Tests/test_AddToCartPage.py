import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
import pytest
import allure 
from allure_commons.types import AttachmentType
from Locators.Locators import Locators
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.AddToCartPage import AddToCartPage

class Test_AddTOCartPage(BaseTest):
    
    @pytest.mark.order()
    def test_verify_cart_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage = HomePage(self.driver)
        homePage.do_shopping()
        homePage.do_click(Locators.CART_ICON)
        addToCart = AddToCartPage(self.driver)
        cart_title = addToCart.get_header_name_of_cart_page()
        assert cart_title == TestData.CART_PAGE_TITLE
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.order()
    def test_verify_item_1_in_cart(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        homePage = HomePage(self.driver)
        homePage.do_shopping()
        homePage.do_click(Locators.CART_ICON)
        addToCart = AddToCartPage(self.driver)
        addToCart.do_items_exist_in_cart()
        addToCart.do_click_checkout_button()
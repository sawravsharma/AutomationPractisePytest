import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
import allure 
from Pages.AddToCartPage import AddToCartPage
from Pages.BillingDetailsPage import BillingDetailsPage
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage


class Test_BillingDetailsPage(BaseTest):

    @pytest.mark.order(1)
    def test_verify_enter_info_in_cart(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login()
        self.homePage = HomePage(self.driver)
        homePage.do_shopping()
        homePage.is_cart_icon_clickable()
        self.addToCart = AddToCartPage(self.driver)
        self.addToCart.do_click_checkout_button()
        self.checkInfo = BillingDetailsPage(self.driver)
        self.checkInfo.do_enter_your_info()  
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)

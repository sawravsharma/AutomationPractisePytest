# import sys, os
# from xml.sax.xmlreader import Locator

# from Pages.CheckoutOverviewPage import CheckoutOverviewPage
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')

# import pytest
# import allure 
# from Pages.AddToCartPage import AddToCartPage
# from Pages.BillingDetailsPage import BillingDetailsPage
# from allure_commons.types import AttachmentType
# from Tests.test_Base import BaseTest
# from Pages.HomePage import HomePage
# from Pages.LoginPage import LoginPage
# from Locators.Locators import Locators


# class Test_CheckoutOverviewPage(BaseTest):

#     # @pytest.mark.order(10)
#     # def test_verify_click_on_finish_button(self):
#     #     self.loginPage = LoginPage(self.driver)
#     #     homePage = self.loginPage.do_login()
#     #     self.homePage = HomePage(self.driver)
#     #     homePage.do_shopping()
#     #     homePage.is_cart_icon_clickable()
#     #     self.addToCart = AddToCartPage(self.driver)
#     #     self.addToCart.do_click_checkout_button()
#     #     self.checkInfo = BillingDetailsPage(self.driver)
#     #     self.checkInfo.do_enter_your_info()  
#     #     self.checkInfo.do_click(Locators.CONTINUE_BUTTON)
#     #     self.checkoutOverview = CheckoutOverviewPage
#     #     self.checkoutOverview.do_click_on_finish_button
#     #     allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)
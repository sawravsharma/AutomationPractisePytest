import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Pages.AddToCartPage import AddToCartPage
from Pages.BasePage import BasePage
from Locators.Locators import Locators
from EnumsPackage.Enums import Products

import logging
log = logging.getLogger(__name__)

class HomePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_cart_icon_exist(self):
        return self.is_visible(Locators.CART_ICON)

    # def is_cart_icon_clickable(self):
    #     self.do_click(Locators.CART_ICON)
    #     return AddToCartPage(self.driver)

    def get_header_value(self):
        return self.get_element_text(Locators.HEADER)

    def do_shopping(self):
        for product in Products:
            product = self.driver.find_element_by_xpath(
                "(//a[@rel='nofollow'])[%s]" % str(product.value))
            product.click()
        self.do_click(Locators.CART_ICON)
        return AddToCartPage(self.driver)

    def do_logout(self):
        self.do_click(Locators.MY_ACCOUNT_TAB)
        self.do_click(Locators.LOGOUT_BUTTON)


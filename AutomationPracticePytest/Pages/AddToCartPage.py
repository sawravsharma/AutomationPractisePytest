import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Locators.Locators import Locators
from Pages.BasePage import BasePage
from Pages.BillingDetailsPage import BillingDetailsPage
from EnumsPackage.Enums import Products
import logging
log = logging.getLogger(__name__)

class AddToCartPage(BasePage):

        def __init__(self, driver):
            super().__init__(driver)

        def get_header_name_of_cart_page(self):
            return self.get_element_text(Locators.CART_PAGE_TITLE)

        def do_items_exist_in_cart(self):
            for getValue in Products:
                searchProductPresence  = self.driver.find_element_by_xpath(
                     "(//*[@class='cart_item'])[%s]" % str(getValue.value))
            assert searchProductPresence.text == getValue.value
            print(searchProductPresence.text)

        def do_click_checkout_button(self):
            self.do_click(Locators.CHECKOUT_BUTTON)
            return BillingDetailsPage(self.driver)


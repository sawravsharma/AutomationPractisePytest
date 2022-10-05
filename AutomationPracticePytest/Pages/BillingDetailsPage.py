
import sys, os
from EnumsPackage.Enums import States
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Locators.Locators import Locators
from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.support.ui import Select
import logging
import time

log = logging.getLogger(__name__)

class BillingDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def do_enter_your_info(self):
        self.do_send_keys(Locators.FIRST_NAME, TestData.FIRST_NAME)
        self.do_send_keys(Locators.LAST_NAME, TestData.LAST_NAME)
        self.do_send_keys(Locators.COMPANY_NAME, TestData.COMPANY_NAME)
        self.do_send_keys(Locators.PHONE, TestData.PHONE)
        self.do_send_keys(Locators.ADDRESS, TestData.ADDRESS)
        time.sleep(1)
        self.do_send_keys(Locators.TOWN_CITY, TestData.TOWN_CITY)
        time.sleep(1)
        self.do_click(Locators.STATE_COUNTY)
        states = self.driver.find_element_by_xpath(
            "(//div[@class='select2-result-label'])[%s]" % str(States.HIMACHAL_PRADESH.value))
        states.click()
        time.sleep(1)
        self.do_send_keys(Locators.POSTAL_ZIP_CODE, TestData.POSTAL_ZIP_CODE)
        time.sleep(1)
        self.do_click(Locators.PAYPAL_EXPRESS_CHECKOUT)
        time.sleep(1)
        self.do_click(Locators.PLACE_ORDER_BUTTON)
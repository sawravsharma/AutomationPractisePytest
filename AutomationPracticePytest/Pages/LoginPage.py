from lib2to3.pgen2 import driver
import sys, os
import time
from pytest import yield_fixture

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Locators.Locators import Locators
from Config.config import TestData
from Pages.HomePage import HomePage
from Pages.BasePage import BasePage

import logging
log = logging.getLogger(__name__)

class LoginPage(BasePage):

    '''constructor of the page class'''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    '''Page Actions for login page'''
    '''this method is use to get the page title'''
    def get_login_page_title(self, title):
        return self.get_title(title)

    '''this is use to login to application'''
    def do_login(self):
            self.do_send_keys(Locators.EMAIL, TestData.EMAIL)
            self.do_send_keys(Locators.PASSWORD, TestData.PASSWORD)
            self.do_click(Locators.LOGIN_BUTTON)
            self.do_click(Locators.SHOP_TAB)
            return HomePage(self.driver)

    '''this is use to login into application with incorrect credentials'''
    def do_login_with_incorrect_credentials(self):
            self.do_send_keys(Locators.EMAIL, TestData.EMAIL)
            time.sleep(3)
            self.do_send_keys(Locators.PASSWORD, TestData.ERR_PASSWORD)
            time.sleep(3)
            self.do_click(Locators.LOGIN_BUTTON)
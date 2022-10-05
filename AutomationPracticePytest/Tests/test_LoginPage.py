import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import allure
import pytest
from Locators.Locators import Locators
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage 

class Test_Login(BaseTest):

    @pytest.mark.order()
    def test_verify_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    '''login with correct credentials'''
    @pytest.mark.order()
    def test_verify_login_into_app(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

        # self.loginPage.do_click()

    '''login with incorrect credentials'''
    @pytest.mark.order()
    def test_verify_login_into_app_with_incorrect_credentials(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login_with_incorrect_credentials()
        error_msg = self.loginPage.get_element_text(Locators.ERROR_MESSAGE)
        assert error_msg == TestData.LOGIN_WITH_INCORRECT_CREDENTIALS_MESSAGE
        print(error_msg)
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)


import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from Locators.Locators import Locators
from Pages.BasePage import BasePage
import logging
log = logging.getLogger(__name__)

class CheckoutOverviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def do_click_on_finish_button(self):
        time.sleep(5)
        self.do_click(Locators.FINISH_BUTTON)
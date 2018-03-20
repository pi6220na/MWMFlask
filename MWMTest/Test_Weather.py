import selenium
from selenium import webdriver

import unittest
import urllib3

from flask_testing import LiveServerTestCase

class TitleTest(LiveServerTestCase):
    port = 8081

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_shown_on_home_page(self):
        self.browser.get(self.live_server_url)
        assert 'Firday' in self.browser.title


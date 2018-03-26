# copied and modeled from Scott example in:
#  https://github.com/jorricarter/PythonProject4/blob/master/tests/front_end_test.py

# terminal/command line: python -m unittest test_Weather.py -v
# assumes running from MWMTest subdirectory
# assumes browser driver.exe in MWMTest subdirectory (chromedriver.exe)


from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


# an interesting discussion on unittesting and test case ordering:
# https://stackoverflow.com/questions/5387299/python-unittest-testcase-execution-order


class MyTestCase(TestCase):

    def setUp(self):
        '''setUp test'''
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://127.0.0.1:5000')
        self.driver.implicitly_wait(10)

        self.addCleanup(self.driver.quit)

    # tests if page loads and the title is "FirdayNight"
    def test_apage_title(self):
        '''test page title'''
        self.assertIn('FirdayNight', self.driver.title)    # your title here
        self.driver.implicitly_wait(4)

    # tests links on right side of page for clicks
    def test_links(self):
        '''test links'''
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://127.0.0.1:5000')
        self.driver.implicitly_wait(10)

        # first test of help button dropdown
        test = self.driver.find_element_by_id('myHelpButton')
        test.click()


        # second test clicking HELP dropdown
        test = self.driver.find_element_by_id('myHelpLink')
        test.click()
        time.sleep(2)

        # https://www.youtube.com/watch?v=p_X99_PwFWo great vid shows how to copy element selector or xpath
        # close the modal window
        self.driver.find_element_by_css_selector('#MWM_help > div > div.modal-menu-bar > svg > path').click()


        # click on weather icon to display 3 choice dropdown
        test = self.driver.find_element_by_xpath('//*[@id="weather-menu"]/div/button')
        test.click()
        time.sleep(2)
        # open weather current conditions modal window
        test = self.driver.find_element_by_xpath('//*[@id="weather-menu"]/div/div/a[1]')
        test.click()
        time.sleep(2)
        # # close weather current conditions modal window
        test = self.driver.find_element_by_css_selector('#w_current > div > div.modal-menu-bar > svg > path')
        test.click()


if __name__ == '__main__':
    main(verbosity=2)
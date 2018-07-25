from selenium.webdriver.common.keys import Keys
from resources.model.elements.web_element import WebElement
from time import sleep


class Input(WebElement):

    def __init__(self, xpath, driver, tag):
        WebElement.__init__(self, xpath, driver)
        self.tag_xpath = '//a[@href="/explore/tags/' + tag + '/"]'

    def send_keys(self, string):
        self._return_visible_element_(self.xpath).send_keys(string)
        sleep(1)
        self._return_visible_element_(self.tag_xpath).click()

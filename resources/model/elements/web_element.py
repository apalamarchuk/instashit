from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class WebElement(object):

    def __init__(self, xpath, driver):
        self.xpath = xpath
        self.driver = driver

    def click(self):
        sleep(1)
        self._return_visible_element_(self.xpath).click()

    def comment(self, comment):
        self._return_visible_element_(self.xpath).click()
        self._return_visible_element_(self.xpath).send_keys(comment)
        self._return_visible_element_(self.xpath).send_keys(Keys.ENTER)
        sleep(3)

    def _is_visible_(self):
        sleep(1)
        return WebDriverWait(self.driver, 15) \
            .until(EC.visibility_of_element_located((By.XPATH, self.xpath)))

    @staticmethod
    def return_visible_element(driver, xpath):
        sleep(1)
        return WebDriverWait(driver, 15) \
            .until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def _return_visible_element_(self, xpath):
        sleep(1)
        return WebDriverWait(self.driver, 15) \
            .until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def _return_visible_elements_(self, xpath):
        sleep(1)
        return WebDriverWait(self.driver, 15) \
            .until(EC.visibility_of_any_elements_located((By.XPATH, xpath)))

    def _return_element_(self, xpath):
        sleep(1)
        return self.driver.find_element_by_xpath(xpath)

    def _return_elements_(self, xpath):
        sleep(1)
        return self.driver.find_elements_by_xpath(xpath)

    def _return_elements_len_(self):
        sleep(1)
        return len(self.driver.find_elements_by_xpath(self.xpath))

    def return_len(self):
        sleep(1)
        return len(WebDriverWait(self.driver, 15).until(EC.visibility_of_any_elements_located((By.XPATH, self.xpath))))

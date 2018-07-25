from selenium.webdriver.common.keys import Keys
from time import sleep

from resources.model.pages.base_page import BasePage
from resources.model.pages.profile_page_obj_rep import ProfilePageObjRep


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, ProfilePageObjRep(driver))

    def get_following_number(self):
        return self.object_rep.following_number.get_text()

    def get_followers_number(self):
        return self.object_rep.followers_number.get_text()

    def open_following_list(self):
        self.object_rep.following_link.click()

    def open_followers_list(self):
        self.object_rep.followers_link.click()

    def scroll_dialog(self):
        self.object_rep.first_li.click()
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight")

    def get_following_list(self, mysql_helper):
        default_list = set()
        foll_num = int(self.get_following_number())
        self.open_following_list()
        self.object_rep.following_first_li.click()
        while self.object_rep.following_li_list.return_len() < foll_num:
            self.driver.switch_to.active_element.send_keys(Keys.PAGE_DOWN)

        mysql_helper.delete_default_list()
        mysql_helper.reset_autoincrement_default_list()

        for i in range(1, foll_num + 1):
            name = str(self.driver.find_element_by_xpath(self.object_rep.following_li_list_xpath + "[" + str(
                i) + "]//a").get_attribute("href"))
            mysql_helper.add_to_default_list(name)
            default_list.add(name)

        return default_list

    def get_followers_list(self, mysql_helper):
        followers_list = set()
        foll_num = int(self.get_followers_number())
        self.open_followers_list()
        self.object_rep.followers_first_li.click()
        while self.object_rep.followers_li_list.return_len() < foll_num:
            self.driver.switch_to.active_element.send_keys(Keys.PAGE_DOWN)

        mysql_helper.delete_followers_list()
        mysql_helper.reset_autoincrement_followers_list()

        for i in range(1, foll_num + 1):
            name = str(self.driver.find_element_by_xpath(self.object_rep.followers_li_list_xpath + "[" + str(
                i) + "]//a").get_attribute("href"))
            mysql_helper.add_to_followers_list(name)
            followers_list.add(name)

        return followers_list

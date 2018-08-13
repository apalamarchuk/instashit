from selenium.webdriver.common.keys import Keys

from resources.model.pages.base_page import BasePage
from resources.model.pages.search_result_obj_rep import SearchResultObjRep
from time import sleep


class SearchResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, SearchResultObjRep(driver))

    def following(self, mysql_helper, comment):
        self.object_rep.photo_link.click()
        if self.object_rep.like_button._return_elements_len_() > 0:
            self.object_rep.like_button.click()
        self.object_rep.comment_area.comment(comment)
        self.object_rep.likes_link.click()
        self.object_rep.first_user_li.click()
        shit_list = self.driver.find_elements_by_xpath(self.object_rep.follow_button_xpath)
        shit_name_list = self.driver.find_elements_by_xpath(
            self.object_rep.follow_button_xpath + self.object_rep.follow_user_xpath)
        for i in range(1, 50):
            sleep(2)
            shit_list[i].click()
            name = shit_name_list[i].get_attribute("href")
            mysql_helper.add_to_following_list(name)
            if i % 6 == 0:
                self.driver.switch_to.active_element.send_keys(Keys.PAGE_DOWN)
                sleep(5)

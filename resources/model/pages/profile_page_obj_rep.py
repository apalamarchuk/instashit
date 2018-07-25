from resources.model.pages.object_rep import ObjectRepository
from resources.model.elements.button import Button
from resources.model.elements.link import Link
from resources.model.elements.field import Field
from resources.model.elements.web_element import WebElement
from resources.model.elements.select_field import SelectField


class ProfilePageObjRep(ObjectRepository):
    following_link_xpath = '//a[@href="/arthur_super/following/"]'
    followers_link_xpath = '//a[@href="/arthur_super/followers/"]'
    following_number_xpath = '//a[@href="/arthur_super/following/"]/span'
    followers_number_xpath = '//a[@href="/arthur_super/followers/"]/span'

    following_dialog_xpath = '//div[text()="Following"]/following-sibling::div'
    following_li_list_xpath = '//div[text()="Following"]/following-sibling::div//li'
    following_first_li_xpath = '//div[text()="Following"]/following-sibling::div//li[1]'

    followers_dialog_xpath = '//div[text()="Followers"]/following-sibling::div'
    followers_li_list_xpath = '//div[text()="Followers"]/following-sibling::div//li'
    followers_first_li_xpath = '//div[text()="Followers"]/following-sibling::div//li[1]'

    def __init__(self, driver):
        super().__init__(driver)
        self.following_link = Link(self.following_link_xpath, driver)
        self.following_number = Field(self.following_number_xpath, driver)
        self.following_dialog = WebElement(self.following_dialog_xpath, driver)
        self.following_first_li = WebElement(self.following_first_li_xpath, driver)
        self.following_li_list = WebElement(self.following_li_list_xpath, driver)

        self.followers_link = Link(self.followers_link_xpath, driver)
        self.followers_number = Field(self.followers_number_xpath, driver)
        self.followers_dialog = WebElement(self.followers_dialog_xpath, driver)
        self.followers_first_li = WebElement(self.followers_first_li_xpath, driver)
        self.followers_li_list = WebElement(self.followers_li_list_xpath, driver)

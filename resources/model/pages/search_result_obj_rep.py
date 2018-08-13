
from resources.model.elements.link import Link
from resources.model.elements.web_element import WebElement
from resources.model.elements.button import Button
from resources.model.pages.object_rep import ObjectRepository


class SearchResultObjRep(ObjectRepository):
    photo_link_xpath = '//h2[div]/following-sibling::div//a'
    likes_link_xpath = '//a[text() = " likes"]'
    post_owner_follow_button = '//button[text()="Follow"]'
    first_user_li_xpath = '//div[div[text() = "Likes"]]//li[1]'
    follow_button_xpath = '//div[div[text() = "Likes"]]//button[text() = "Follow"]'
    follow_user_xpath = '/../../div/a'
    like_button_xpath = '//span[@aria-label="Like"]'
    comment_area_xpath = '//textarea[@aria-label="Add a comment…"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.photo_link = Link(self.photo_link_xpath + "[1]", driver)
        self.likes_link = Link(self.likes_link_xpath, driver)
        self.first_user_li = WebElement(self.first_user_li_xpath, driver)
        self.follow_button = Button(self.follow_button_xpath, driver)
        self.like_button = Button(self.like_button_xpath, driver)
        self.comment_area = WebElement(self.comment_area_xpath, driver)

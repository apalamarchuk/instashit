from resources.model.pages.object_rep import ObjectRepository
from resources.model.elements.button import Button
from resources.model.elements.link import Link
from resources.model.elements.input import Input
from resources.model.elements.select_field import SelectField


class FeedPageObjRep(ObjectRepository):
    profile_link_xpath = '//*[@href="/arthur_super/"]'
    search_input_xpath = '//input[ @ placeholder = "Search"]'

    def __init__(self, driver, tag):
        super().__init__(driver)
        self.profile_link = Link(self.profile_link_xpath, driver)
        if tag is not None:
            self.search_input = Input(self.search_input_xpath, driver, tag)
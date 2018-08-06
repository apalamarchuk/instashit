from resources.model.pages.base_page import BasePage
from resources.model.pages.feed_page_obj_rep import FeedPageObjRep


class FeedPage(BasePage):

    def __init__(self, driver, tag=None):
        super().__init__(driver, FeedPageObjRep(driver, tag))
        self.tag = tag

    def goto_profile_page(self):
        self.object_rep.profile_link.click()

    def goto_search_result_page(self):
        self.object_rep.search_input.send_keys(self.tag)

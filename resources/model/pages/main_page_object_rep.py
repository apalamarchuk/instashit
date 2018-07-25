from resources.model.pages.object_rep import ObjectRepository
from resources.model.elements.button import Button
from resources.model.elements.link import Link
from resources.model.elements.field import Field
from resources.model.elements.select_field import SelectField


class MainPageObjectRepository(ObjectRepository):
    calculate_link_xpath = '//a[@href="#calculation"]'

    login_link_xpath = '//a[@href="/accounts/login/"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.login_link = Link(self.login_link_xpath, driver)
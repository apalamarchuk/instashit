from resources.model.pages.object_rep import ObjectRepository
from resources.model.elements.button import Button
from resources.model.elements.link import Link
from resources.model.elements.field import Field
from resources.model.elements.select_field import SelectField


class LoginPageObjRep(ObjectRepository):
    username_input_xpath = '//input[@name="username"]'
    password_input_xpath = '//input[@name="password"]'
    login_button_xpath = '//button[contains(text(), "Log in")]'

    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = Field(self.username_input_xpath, driver)
        self.password_input = Field(self.password_input_xpath, driver)
        self.login_button = Button(self.login_button_xpath, driver)
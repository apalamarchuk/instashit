from resources.model.pages.base_page import BasePage
from resources.model.pages.login_page_object_rep import LoginPageObjRep


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, LoginPageObjRep(driver))

    def login(self, username, password):
        self.object_rep.username_input.set_value(username)
        self.object_rep.password_input.set_value(password)
        self.object_rep.login_button.click()
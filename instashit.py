from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from control.mysql_helper import MySqlHelper

from resources.model.pages.feed_page import FeedPage
from resources.model.pages.login_page import LoginPage
from resources.model.pages.main_page import MainPage
from resources.model.pages.main_page_object_rep import MainPageObjectRepository
from resources.model.pages.profile_page import ProfilePage
from resources.model.pages.search_result_page import SearchResultPage

mysql_helper = MySqlHelper()
chrome_options = Options()
chrome_options.add_argument("user-agent=Chrome/67.0.3396.99")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--blink-settings=imagesEnabled=false')  # change to false
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.maximize_window()

start_page_obj_rep = MainPageObjectRepository(driver)
start_page = MainPage(driver, start_page_obj_rep)
start_page.open_main_page()
start_page.object_rep.login_link.click()

login_page = LoginPage(driver).login("arthur_super", "tararam123")
#feed_page = FeedPage(driver).goto_profile_page()

#profile_page = ProfilePage(driver)
#following_number = profile_page.get_following_number()

#default_list = profile_page.get_following_list(mysql_helper)
#driver.refresh()
#followers_list = profile_page.get_followers_list(mysql_helper)

FeedPage(driver, "follow4follow").goto_search_result_page()
result_page = SearchResultPage(driver)
result_page.following(mysql_helper, "F4F??!")

sleep(3)
# driver.quit()

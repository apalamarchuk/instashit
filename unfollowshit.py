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
#chrome_options.add_argument('--headless')
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
feed_page = FeedPage(driver).goto_profile_page()

profile_page = ProfilePage(driver)
following_number = profile_page.get_following_number()
print(following_number)
following_list = profile_page.get_following_list(mysql_helper, 200)
print(len(following_list))
print(following_list)

if len(following_list) > 200:
    for link in following_list:
        driver.get(link)
        driver.find_element_by_xpath('//button[text()="Following"]').click()
        sleep(2)
        driver.find_element_by_xpath('//button[text()="Unfollow"]').click()
        sleep(2)
        driver.refresh()
        sleep(5)
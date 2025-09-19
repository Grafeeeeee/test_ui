from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from locators import search_page as loc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SearchPage(BasePage):

    page_url = '/website/search?search=&order=name+asc'

    def __init__(self, driver, wait):
        super().__init__(driver)

    def enter_word_to_search_field(self, check_word):
        search_field = self.find(loc.search_field_loc)
        search_field.send_keys(check_word)
        search_field.send_keys(Keys.ENTER)

    def check_all_found_words(self, check_word):
        all_elements = self.finds(loc.all_elements_loc)
        assert all(check_word in element.text for element in all_elements)

    def choose_filter_by_category(self, wait):
        nav_menu = self.find(loc.nav_menu_loc)
        ActionChains(self.driver).move_to_element(nav_menu).perform()
        desks_category = wait.until(EC.element_to_be_clickable(loc.desks_category_loc))
        desks_category.click()

    def sign_in(self):
        sign_in_btn = self.find(loc.sign_in_btn_loc)
        sign_in_btn.click()

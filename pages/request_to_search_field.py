from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from locators import search_field_locators as loc


class SearchField(BasePage):

    page_url = '/website/search?search=&order=name+asc'

    def enter_word_to_search_field(self, check_word):
        search_field = self.find(loc.search_field_loc)
        search_field.send_keys(check_word)
        search_field.send_keys(Keys.ENTER)

    def check_all_found_words(self, check_word):
        all_elements = self.finds(loc.all_elements_loc)
        assert all(check_word in element.text for element in all_elements)

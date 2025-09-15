from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators import sorting_by_price_range as loc


class SortPriceRange(BasePage):

    page_url = '/shop/category/desks-1'

    def get_min_value(self, wait, test_value):
        min_value_for_enter = wait.until(EC.presence_of_element_located(loc.min_value_for_enter_loc))
        min_value = wait.until(EC.element_to_be_clickable(loc.min_value_loc))
        min_value.click()
        min_value_for_enter.send_keys(test_value, Keys.ENTER)

    def check_price_of_received_items(self, test_value):
        elements = self.finds(loc.elements_loc)
        elements_price = [float(el.text.replace(',', '')) for el in elements]
        assert [i > test_value for i in elements_price]

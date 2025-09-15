from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators import sorting_by_price as loc


class SortingByPrice(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.list_prices_before_filtered = None
        self.list_prices_after_filtered = None

    page_url = '/shop/category/desks-1'

    def get_prices_before(self):
        get_price_for_each_card = self.finds(loc.get_price_for_each_card_loc)
        self.list_prices_before_filtered = [float(i.text.replace(',', '')) for i in get_price_for_each_card]

    def click_price_filter(self, wait):
        filter_price = self.find(loc.filter_price_loc)
        filter_price.click()
        filter_low_to_high = wait.until(EC.element_to_be_clickable(loc.filter_low_to_high_loc))
        filter_low_to_high.click()

    def get_prices_after(self):
        get_price_after_filtered = self.finds(loc.get_price_after_filtered_loc)
        self.list_prices_after_filtered = [float(i.text.replace(',', '')) for i in get_price_after_filtered]

    def compare_received_values(self):
        assert self.list_prices_after_filtered == sorted(self.list_prices_before_filtered)
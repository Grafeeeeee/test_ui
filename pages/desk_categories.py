from pages.base_page import BasePage
from locators import desk_categories as loc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class DeskCategories(BasePage):

    page_url = '/shop/category/desks-1'

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.list_prices_before_filtered = None
        self.list_prices_after_filtered = None

    def get_item_by_filter_category_desk(self):
        get_list_elements = self.finds(loc.get_list_elements_loc)
        for item in get_list_elements:
            text = item.text.lower()
            assert any(word in text for word in ('desk', 'table')), f'{item.text} does not include "desk" or "table"'

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

    def get_min_value(self, wait, test_value):
        min_value_for_enter = wait.until(EC.presence_of_element_located(loc.min_value_for_enter_loc))
        min_value = wait.until(EC.element_to_be_clickable(loc.min_value_loc))
        min_value.click()
        min_value_for_enter.send_keys(test_value, Keys.ENTER)

    def check_price_of_received_items(self, test_value):
        elements = self.finds(loc.elements_loc)
        elements_price = [float(el.text.replace(',', '')) for el in elements]
        assert [i > test_value for i in elements_price]

    def go_to_search_result(self, wait):
        all_cards = len(self.finds(loc.all_cards_loc))
        search_field = self.find(loc.search_field_loc)
        search_field.send_keys('table', Keys.ENTER)
        wait.until(lambda x: (len(x.find_elements(
            By.XPATH, '//div[@class="oe_product_image position-relative h-100 flex-grow-0 overflow-hidden"]')))
                             != all_cards)

    def switch_to_new_tab_and_get_text(self, wait):
        inner_info = wait.until(EC.element_to_be_clickable(loc.inner_info_loc))
        ActionChains(self.driver).key_down(Keys.CONTROL).click(inner_info).key_up(Keys.CONTROL).perform()
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        self.text = self.find(loc.text_loc).text
        self.driver.close()
        self.driver.switch_to.window(tabs[0])

    def get_text_to_check(self):
        return self.text

    def add_item_to_cart(self, wait):
        element = self.find(loc.element_loc)
        ActionChains(self.driver).move_to_element(element).click(element).perform()
        btn_go_to_cart = wait.until(EC.element_to_be_clickable(loc.btn_go_to_cart_loc))
        btn_go_to_cart.click()

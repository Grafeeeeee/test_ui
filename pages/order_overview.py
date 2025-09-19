from pages.base_page import BasePage
from locators import order_overview as loc


class OrderOverview(BasePage):

    page_url = '/shop/cart'

    def __init__(self, driver, expected_values):
        super().__init__(driver)

    def check_get_added_element(self, expected_values):
        adding_element_after = self.find(loc.adding_element_after_loc)
        assert adding_element_after.text == expected_values

    def check_title_added_element(self, text):
        order_text = self.find(loc.order_text_loc).text
        assert order_text == text

    def check_quantity_added_element(self, expected_values):
        order_total_quantity = self.find(loc.order_total_quantity_loc)
        assert order_total_quantity.get_attribute('value') == expected_values

    def check_item_text(self, text):
        assert self.find(loc.check_text_loc).text == text

    def click_button_checkout(self):
        checkout = self.find(loc.checkout_loc)
        checkout.click()

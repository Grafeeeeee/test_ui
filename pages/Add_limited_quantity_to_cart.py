from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators import limited_addition_product_to_cart_locators as loc


class AddToCart(BasePage):

    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.initial_quan_value = None

    def add_limit_quantity(self):
        add_quantity = self.find(loc.add_quantity_loc)
        for _ in range(5):
            add_quantity.click()

    def get_quantity(self, wait):
        quantity = wait.until(EC.element_to_be_clickable(loc.quantity_loc))
        self.initial_quan_value = quantity.get_attribute('value')

    def add_cart(self):
        btn_add_cart = self.find(loc.btn_add_cart_loc)
        btn_add_cart.click()

    def go_to_cart(self, wait):
        cart = wait.until(EC.element_to_be_clickable(loc.cart_loc))
        cart.click()

    def check_text_added_element(self, text):
        order_text = self.find(loc.order_text_loc).text
        order_total_quantity = self.find(loc.order_total_quantity_loc)
        assert order_text == text
        assert order_total_quantity.get_attribute('value') == self.initial_quan_value

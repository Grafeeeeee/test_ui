from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import office_design_software as loc


class OfficeDesignSoftware(BasePage):

    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def __init__(self, driver, wait):
        super().__init__(driver)
        self.adding_element_before = None
        self.initial_quan_value = None

    def button_adding_element(self):
        btn_add_cart = self.find(loc.btn_add_cart_loc)
        btn_add_cart.click()

    def add_limit_quantity(self, clicks, wait):
        for _ in range(clicks):
            add_quantity = wait.until(EC.element_to_be_clickable(loc.add_quantity_loc))
            add_quantity.click()

    def get_quantity(self, wait):
        quantity = wait.until(EC.element_to_be_clickable(loc.quantity_loc))
        self.initial_quan_value = quantity.get_attribute('value')
        return self.initial_quan_value

    def get_element_text_before(self):
        self.adding_element_before = self.find(loc.adding_element_before_loc)
        return self.adding_element_before.text

    def click_btn_view_to_cart(self, wait):
        btn_view_cart = wait.until(EC.element_to_be_clickable(loc.btn_view_cart_loc))
        btn_view_cart.click()

    def add_cart(self):
        btn_add_cart = self.find(loc.btn_add_cart_loc)
        btn_add_cart.click()

    def go_to_cart(self, wait):
        cart = wait.until(EC.element_to_be_clickable(loc.cart_loc))
        cart.click()

    def check_indicator_addition_to_cart(self, wait):
        cart_indicator = self.find(loc.cart_indicator_loc)
        cart_indicator_text = cart_indicator.text
        wait.until(lambda x: x.find_element(
            By.CSS_SELECTOR,
            ".my_cart_quantity.badge.text-bg-primary.position-absolute.top-0.end-0.mt-n1.me-n1.rounded-pill")
                   .text != cart_indicator_text)
        cart_indicator.click()

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators import btn_to_cart_locators as loc


class ToCartWithBtn(BasePage):

    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.adding_element_before = None

    def adding_element(self):
        self.adding_element_before = self.find(loc.adding_element_before_loc).text
        btn_add_cart = self.find(loc.btn_add_cart_loc)
        btn_add_cart.click()

    def click_btn_to_cart(self, wait):
        btn_view_cart = wait.until(EC.element_to_be_clickable(loc.btn_view_cart_loc))
        btn_view_cart.click()

    def check_get_added_element(self):
        adding_element_after = self.find(loc.adding_element_after_loc)
        assert adding_element_after.text == self.adding_element_before


from pages.base_page import BasePage
from locators import add_item_by_search as loc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class AddItem(BasePage):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.text = None

    page_url = '/shop/category/desks-1'

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

    def add_item_to_cart(self, wait):
        element = self.find(loc.element_loc)
        ActionChains(self.driver).move_to_element(element).click(element).perform()
        btn_go_to_cart = wait.until(EC.element_to_be_clickable(loc.btn_go_to_cart_loc))
        btn_go_to_cart.click()

    def check_item_text(self):
        assert self.find(loc.check_text_loc).text == self.text

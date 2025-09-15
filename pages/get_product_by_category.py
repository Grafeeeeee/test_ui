from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import sorting_by_category as loc


class SortByCategory(BasePage):

    page_url = '/website/search?search=&order=name+asc'

    def choose_filter_by_category(self, wait):
        nav_menu = self.find(loc.nav_menu_loc)
        ActionChains(self.driver).move_to_element(nav_menu).perform()
        desks_category = wait.until(EC.element_to_be_clickable(loc.desks_category_loc))
        desks_category.click()

    def get_element_for_checking(self):
        first_element = self.find(loc.first_element_loc)
        assert "Desk" in first_element.text
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from locators import validation_login_form as loc


class ValidationLogin(BasePage):

    page_url = '/website/search?search=&order=name+asc'

    def sign_in(self):
        sign_in_btn = self.find(loc.sign_in_btn_loc)
        sign_in_btn.click()

    def login_form(self, faker):
        email_field = self.find(loc.email_field_loc)
        email_field.send_keys(faker.email())
        email_field.send_keys(Keys.ENTER)
        pass_field = self.find(loc.pass_field_loc)
        validation_text = pass_field.get_attribute("validationMessage")
        assert "Please fill out this field" in validation_text
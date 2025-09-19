from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from locators import login_form as loc


class LoginPage(BasePage):

    def validate_login_form_with_empty_pass_field(self, faker):
        email_field = self.find(loc.email_field_loc)
        email_field.send_keys(faker.email())
        email_field.send_keys(Keys.ENTER)
        pass_field = self.find(loc.pass_field_loc)
        validation_text = pass_field.get_attribute("validationMessage")
        assert "Please fill out this field" in validation_text
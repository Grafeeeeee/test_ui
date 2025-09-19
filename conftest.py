import random
from selenium.webdriver.chrome.options import Options
import string
from faker import Faker
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from pages.desk_categories import DeskCategories
from pages.fill_address_form import FillAddressForm
from pages.login_page import LoginPage
from pages.office_design_software import OfficeDesignSoftware
from pages.order_overview import OrderOverview
from pages.search_page import SearchPage


@pytest.fixture()
def generate_random_pass(length: int):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture()
def faker():
    return Faker('en_US')


@pytest.fixture()
def office_design_software(driver, wait):
    return OfficeDesignSoftware(driver, wait)


@pytest.fixture()
def order_overview(driver, wait):
    return OrderOverview(driver, wait)


@pytest.fixture()
def fill_address_form(driver, wait, faker):
    return FillAddressForm(driver, wait, faker)


@pytest.fixture()
def search_page(driver, wait):
    return SearchPage(driver, wait)


@pytest.fixture()
def page_login_form(driver):
    return LoginPage(driver)


@pytest.fixture()
def category_desk(driver, wait):
    return DeskCategories(driver, wait)

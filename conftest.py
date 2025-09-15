import random
from selenium.webdriver.chrome.options import Options
import string
from faker import Faker
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


@pytest.fixture()
def generate_random_pass(length: int):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


@pytest.fixture
def driver():
    options = Options()
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def wait(driver):
    return WebDriverWait(driver, 10)


@pytest.fixture()
def faker():
    return Faker('en_US')

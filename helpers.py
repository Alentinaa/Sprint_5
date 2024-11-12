import random
import string

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from data import REGISTRATION_URL, data_email, data_user_password
from locators import TestLocators

def generate_login():
    """Генерация уникального логина для регистрации"""
    name = "Valentina_Pahatinskayaкуегкт"
    cohort_number = "15"
    random_digits = ''.join(random.choices(string.digits, k=3))
    domain = "ya.ru"
    return f"{name}_{cohort_number}_{random_digits}@{domain}"

def generate_password():
    """Генерация случайного пароля длиной 6 символов"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def generate_username():
    """Генерация имени пользователя для регистрации"""
    return "Valentina_Pahatinskaya"

def register_user(driver):
    """Регистрация нового пользователя с уникальными логином и паролем"""
    email = generate_login()
    username = "Valentina_Pahatinskaya"
    password = generate_password()

    driver.get(REGISTRATION_URL)
    driver.find_element(*TestLocators.INPUT_REGISTRATION_EMAIL).send_keys(email)
    driver.find_element(*TestLocators.INPUT_REGISTRATION_USER_NAME).send_keys(username)
    driver.find_element(*TestLocators.INPUT_REGISTRATION_USER_PASSWORD).send_keys(password)
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.FORM_LOGIN_AFTER_REGISTRATION)
    )

def account_authorization(driver):
    """Авторизация пользователя с логином и паролем из data.py"""
    driver.find_element(*TestLocators.INPUT_EMAIL_ON_LOGIN_PAGE).send_keys(data_email)
    driver.find_element(*TestLocators.INPUT_PASSWORD_ON_LOGIN_PAGE).send_keys(data_user_password)
    driver.find_element(*TestLocators.BUTTON_LOG_IN_ON_LOGIN_PAGE).click()


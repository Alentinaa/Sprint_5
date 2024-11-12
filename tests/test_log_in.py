from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import MAIN_PAGE_URL, LOGIN_URL, REGISTRATION_URL, FORGOT_PASSWORD_URL
from locators import TestLocators
from helpers import account_authorization


class TestLogin:

    def test_button_login_to_account(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.BUTTON_LOGIN_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(TestLocators.FORM_LOGIN_AFTER_REGISTRATION)
        )
        driver.get(LOGIN_URL)
        account_authorization(driver)

        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER_ON_MAIN_PAGE)
        )
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER_ON_MAIN_PAGE).is_displayed()

    def test_button_personal_account(self,driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT_ON_MAIN_PAGE).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(LOGIN_URL)
        )
        driver.get(LOGIN_URL)
        account_authorization(driver)
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER_ON_MAIN_PAGE)
        )
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER_ON_MAIN_PAGE).is_displayed()

    def test_button_login_on_registration_page(self,driver):
        driver.get(REGISTRATION_URL)
        element = driver.find_element(*TestLocators.BUTTON_LOG_IN_ON_REGISTRATION_PAGE)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(LOGIN_URL)
        )

        driver.get(LOGIN_URL)
        account_authorization(driver)
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER_ON_MAIN_PAGE)
        )
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER_ON_MAIN_PAGE).is_displayed()

    def test_button_login_on_forgot_password_page(self, driver):
        driver.get(FORGOT_PASSWORD_URL)
        driver.find_element(*TestLocators.BUTTON_LOG_IN_ON_FORGOT_PASSWORD_PAGE).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(LOGIN_URL)
        )
        driver.get(LOGIN_URL)
        account_authorization(driver)
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER_ON_MAIN_PAGE)
            )
        assert driver.find_element(*TestLocators.BUTTON_MAKE_ORDER_ON_MAIN_PAGE).is_displayed()


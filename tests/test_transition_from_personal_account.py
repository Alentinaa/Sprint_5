from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from data import MAIN_PAGE_URL, LOGIN_URL, PROFILE_URL
from helpers import account_authorization
from locators import TestLocators


class TestTransitionFromPersonalAccount:

    def test_transition_from_personal_account_to_constructor(self, driver):
        driver.get(LOGIN_URL)
        account_authorization(driver)

        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER_ON_MAIN_PAGE)
        )

        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(PROFILE_URL)
        )

        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR_FROM_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(MAIN_PAGE_URL)
        )

        current_url = driver.current_url
        assert current_url == MAIN_PAGE_URL

    def test_transition_from_personal_account_click_to_logo(self, driver):
        driver.get(LOGIN_URL)
        account_authorization(driver)

        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER_ON_MAIN_PAGE)
        )

        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(PROFILE_URL)
        )

        driver.find_element(*TestLocators.STELLAR_BURGERS_LOGO).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(MAIN_PAGE_URL)
        )

        current_url = driver.current_url
        assert current_url == MAIN_PAGE_URL


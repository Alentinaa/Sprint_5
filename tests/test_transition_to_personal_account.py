from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import MAIN_PAGE_URL, LOGIN_URL, PROFILE_URL
from helpers import account_authorization
from locators import TestLocators


class TestTransitionToPersonalAccount:

    def test_transition_to_personal_account (self, driver):
        driver.get(MAIN_PAGE_URL)

        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT_ON_MAIN_PAGE).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(LOGIN_URL)
        )
        driver.get(LOGIN_URL)
        account_authorization(driver)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER_ON_MAIN_PAGE)
        )

        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT_ON_MAIN_PAGE).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.url_to_be(PROFILE_URL)
        )

        current_url = driver.current_url
        assert current_url == PROFILE_URL


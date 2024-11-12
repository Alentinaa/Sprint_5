from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from data import MAIN_PAGE_URL, LOGIN_URL
from helpers import account_authorization
from locators import TestLocators


class TestLogOutFromPersonalAccount:

    def test_log_out_from_personal_account(self, driver):
        driver.get(LOGIN_URL)
        account_authorization(driver)

        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_MAKE_ORDER_ON_MAIN_PAGE)
        )

        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT_ON_MAIN_PAGE).click()

        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable(TestLocators.BUTTON_LOG_OUT)
        )

        driver.find_element(*TestLocators.BUTTON_LOG_OUT).click()

        WebDriverWait(driver, 20).until(
            expected_conditions.url_to_be(LOGIN_URL)
        )

        current_url = driver.current_url
        assert current_url == LOGIN_URL


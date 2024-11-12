from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import REGISTRATION_URL, LOGIN_URL, data_username, data_email
from helpers import register_user
from locators import TestLocators


class TestRegistration:

    def test_successful_registration(self, driver):
        register_user(driver)

        WebDriverWait(driver, 20).until(expected_conditions.url_to_be(LOGIN_URL))

        login_form = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(TestLocators.FORM_LOGIN_AFTER_REGISTRATION)
        )
        assert login_form.is_displayed()

    def test_incorrect_password(self, driver):
        driver.get(REGISTRATION_URL)

        incorrect_password = "zf1u2"

        driver.find_element(*TestLocators.INPUT_REGISTRATION_USER_NAME).send_keys(data_username)
        driver.find_element(*TestLocators.INPUT_REGISTRATION_EMAIL).send_keys(data_email)
        driver.find_element(*TestLocators.INPUT_REGISTRATION_USER_PASSWORD).send_keys(incorrect_password)

        driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()

        error_message = WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(TestLocators.INCORRECT_PASSWORD)
        )
        assert error_message.is_displayed()


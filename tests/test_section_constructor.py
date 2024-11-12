from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from data import MAIN_PAGE_URL
from locators import TestLocators


class TestSectionConstructor:
    def test_transition_to_sauces_section_is_available(self,driver):
        driver.get(MAIN_PAGE_URL)

        driver.find_element(*TestLocators.SECTION_SAUСES).click()

        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(TestLocators.SAUCES_HEADER)
        )

        assert driver.find_element(*TestLocators.SAUCES_HEADER).is_displayed()

    def test_transition_to_buns_section_is_available(self,driver):
        driver.get(MAIN_PAGE_URL)

        driver.find_element(*TestLocators.SECTION_SAUСES).click()
        driver.find_element(*TestLocators.SECTION_BULKI)

        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUNS_HEADER)
        )

        assert driver.find_element(*TestLocators.BUNS_HEADER).is_displayed()

    def test_transition_to_fillings_section_is_available(self, driver):
        driver.get(MAIN_PAGE_URL)

        driver.find_element(*TestLocators.SECTION_FILLINGS).click()

        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located(TestLocators.FILLINGS_HEADER)
        )

        assert driver.find_element(*TestLocators.FILLINGS_HEADER).is_displayed()


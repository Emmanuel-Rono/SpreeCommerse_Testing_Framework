from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from Locators.locators import ProductsPageLocators
from Core.waits import wait_for_clickable, wait_for_visible
from Services.basepage import BasePage


class OpenProductsPage(BasePage):
    def OpenProductPage(self):
        self.open("/us/en/products")

    def open_products_page(self):
        self.open("/us/en/products")

    def get_page_title(self):
        return self.get_title()

    def get_product_list(self, timeout=10):
        try:
            return self._wait_for_any_product(timeout=timeout)
        except TimeoutException:
            return []

    def _wait_for_any_product(self, timeout=10):
        def _has_products(driver):
            elements = driver.find_elements(*ProductsPageLocators.PRODUCT_ITEMS)
            return elements if elements else False

        return WebDriverWait(self.driver, timeout).until(_has_products)

    def wait_for_products_loaded(self, timeout=10):
        return self._wait_for_any_product(timeout=timeout)

    def click_first_product(self):
        product_links = self._wait_for_any_product()
        if product_links:
            product_name = product_links[0].text
            product_links[0].click()
            return product_name
        return None

    def search_products(self, product_name):
        search_trigger = wait_for_clickable(self.driver, ProductsPageLocators.SEARCH_TRIGGER)
        search_trigger.click()
        for _ in range(3):
            try:
                search_box = wait_for_visible(self.driver, ProductsPageLocators.SEARCH_INPUT)
                search_box.clear()
                search_box.send_keys(product_name)
                search_box.send_keys(Keys.ENTER)
                return
            except StaleElementReferenceException:
                continue
        raise AssertionError("Search input became stale before the query could be entered")

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Core.waits import wait_for_clickable
from Services.basepage import BasePage


class ProductDetailsPage(BasePage):


    ADD_TO_CART_CANDIDATES = [
        (
            By.XPATH,
            "//button[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'add to cart') or contains(translate(@aria-label, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'add to cart')]",
        ),
        (By.CSS_SELECTOR, "button[data-hook*='add_to_cart']"),
        (By.CSS_SELECTOR, "button[name='add-to-cart']"),
        (By.CSS_SELECTOR, "form[action*='cart'] button[type='submit']"),
        (By.CSS_SELECTOR, "button[type='submit']"),
    ]

    def _wait_for_add_to_cart(self, timeout=15):
        def _find(driver):
            for locator in self.ADD_TO_CART_CANDIDATES:
                try:
                    el = driver.find_element(*locator)
                    if el.is_displayed() and el.is_enabled():
                        return el
                except Exception:
                    continue
            return False

        return WebDriverWait(self.driver, timeout).until(_find)

    def add_to_cart(self, timeout=15):
        try:
            button = self._wait_for_add_to_cart(timeout=timeout)
            button.click()
        except Exception:
            # Fallback to clickable wait on the first candidate.
            button = wait_for_clickable(self.driver, self.ADD_TO_CART_CANDIDATES[0], timeout=timeout)
            button.click()

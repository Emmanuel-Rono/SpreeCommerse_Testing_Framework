from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from Core.waits import wait_for_clickable
from Services.basepage import BasePage


class CartPage(BasePage):
    TO_CART_BUTTON = (By.XPATH, "/html/body/header/div[1]/div/div/div[3]/button[2]")
    VIEW_CART_BUTTON = (By.XPATH, "//a[@href='/us/en/cart' and normalize-space()='View Cart']")
    CART_HEADING = (By.XPATH, "//main//h1[normalize-space()='Shopping Cart']")
    CART_ITEMS = (
        By.XPATH,
        "//main//div[contains(@class,'bg-white') and contains(@class,'divide-y')]/div[contains(@class,'p-6') and contains(@class,'flex') and contains(@class,'gap-6')]",
    )

    def _click_cart_button(self, timeout=10):
        cart_button = wait_for_clickable(self.driver, self.TO_CART_BUTTON, timeout=timeout)
        cart_button.click()

    def open_cart(self, timeout=10):
        try:
            try:
                view_cart_button = wait_for_clickable(self.driver, self.VIEW_CART_BUTTON, timeout=3)
            except TimeoutException:
                self._click_cart_button(timeout=timeout)
                view_cart_button = wait_for_clickable(self.driver, self.VIEW_CART_BUTTON, timeout=timeout)
            view_cart_button.click()
            return
        except Exception:
            raise AssertionError("Could not open the cart drawer and navigate to the cart page")

    def is_cart_page(self):
        url = self.driver.current_url.lower()
        if "/us/en/cart" in url or url.endswith("/cart"):
            return True
        return bool(self.driver.find_elements(*self.CART_HEADING))

    def get_line_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        if items:
            return len(items)
        return 0

    def wait_for_line_items(self, timeout=10):
        def _has_items(driver):
            items = driver.find_elements(*self.CART_ITEMS)
            if items:
                return items

        return WebDriverWait(self.driver, timeout).until(_has_items)

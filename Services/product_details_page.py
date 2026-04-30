from selenium.webdriver.common.by import By

from Core.waits import wait_for_clickable
from Services.basepage import BasePage


class ProductDetailsPage(BasePage):
    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//button[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'add to cart') or contains(translate(@aria-label, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'add to cart')]",
    )

    def add_to_cart(self, timeout=15):
        button = wait_for_clickable(self.driver, self.ADD_TO_CART_BUTTON, timeout=timeout)
        button.click()

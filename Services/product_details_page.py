from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Core.waits import wait_for_clickable
from Services.basepage import BasePage


class ProductDetailsPage(BasePage):
    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "/html/body/main/div[2]/div/div[2]/div[4]/div/button",
    )
    CART_SLIDER = (
        By.XPATH,
        "//div[@role='dialog' and @data-state='open' and @data-side='right']",
    )
    VIEW_CART_BUTTON = (
        By.XPATH,
        "//div[@role='dialog' and @data-state='open']//a[@href='/us/en/cart' and normalize-space()='View Cart']",
    )

    def add_to_cart(self, timeout=15):
        button = wait_for_clickable(self.driver, self.ADD_TO_CART_BUTTON, timeout=timeout)
        button.click()
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.CART_SLIDER)
        )
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.VIEW_CART_BUTTON)
        )

    def view_cart(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.CART_SLIDER)
        )
        view_cart_button = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.VIEW_CART_BUTTON)
        )
        try:
            view_cart_button.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", view_cart_button)
        WebDriverWait(self.driver, timeout).until(
            lambda driver: "/us/en/cart" in driver.current_url.lower()
        )

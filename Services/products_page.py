from selenium.webdriver.common.by import By

from Configuration.settings import PRODUCTS_PAGE
from Locators import locators
from Locators.locators import ProductsPageLocators
from Services.basepage import BasePage


class OpenProductsPage(BasePage):
    def OpenProductPage(self):
        self.open(PRODUCTS_PAGE)

    def get_page_title(self):
        self.get_title()

    def get_product_list(self):
        products = self.driver.find_elements(*ProductsPageLocators.PRODUCT_ITEMS)

    def click_first_product(self):
        self.open(PRODUCTS_PAGE)
        productlinks=self.driver.find_elements(*ProductsPageLocators.PRODUCT_ITEMS)
        if productlinks:
            productlinks[0].click()


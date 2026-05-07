from selenium.webdriver.common.by import By


class ProductsPageLocators:
    PRODUCT_ITEMS = (
        By.CSS_SELECTOR,
        "div.grid.grid-cols-2.lg\\:grid-cols-3.gap-6 > a.group.block",
    )
    PRODUCT_LINKS = PRODUCT_ITEMS
    PRODUCT_COUNT = (
        By.XPATH,
        "//div[contains(@class,'hidden') and contains(@class,'md:flex')]//span[contains(text(),'products')]",
    )
    SEARCH_TRIGGER = (By.XPATH, "/html/body/header/div[1]/div/div/div[3]/button[1]")
    SEARCH_INPUT = (By.XPATH, "//*[@id='search-overlay']/div/div/div/form/div/input")

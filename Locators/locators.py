from selenium.webdriver.common.by import By


class ProductsPageLocators:
    PRODUCT_ITEMS = (
        By.XPATH,
        "//main//div[contains(@class,'grid-cols-2') and contains(@class,'lg:grid-cols-3')]//a[contains(@href,'/products/')]",
    )
    PRODUCT_LINKS = PRODUCT_ITEMS
    SEARCH_TRIGGER = (By.XPATH, "/html/body/header/div[1]/div/div/div[3]/button[1]")
    SEARCH_INPUT = (By.XPATH, "//*[@id='search-overlay']/div/div/div/form/div/input")

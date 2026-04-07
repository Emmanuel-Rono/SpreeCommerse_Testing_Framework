

from Services.products_page import OpenProductsPage
from Services.signin_to_account import Customer_Account
import pytest

@pytest.mark.ui
@pytest.mark.smoke

def test_open_account_page(driver):
    products_page =OpenProductsPage(driver)
    products_page.open_products_page(driver)
    account = Customer_Account(driver)
    account.open_account_page
    assert account.open_account_page() == True
 
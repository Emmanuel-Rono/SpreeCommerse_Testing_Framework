
from Services.products_page import OpenProductsPage
from Services.signin_to_account import Customer_Account
import pytest

@pytest.mark.ui
@pytest.mark.smoke

def test_open_account_page(driver,settings):
    products_page =OpenProductsPage(driver,settings)
    products_page.open_products_page()
    account = Customer_Account(driver,settings)
    assert account.open_account_page() == True

 
def test_sign_in_with_valid_credentials(driver, settings):
    products_page = OpenProductsPage(driver,settings)
    products_page.open_products_page()
    account = Customer_Account(driver,settings)
    account.open_account_page()
    email = settings.test_user_email
    password = settings.test_user_password
    account.enter_login_credentials(email, password)
    assert account.is_logged_in() == True

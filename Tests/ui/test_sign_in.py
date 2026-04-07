

from Services.signin_to_account import Customer_Account
import pytest

@pytest.mark.ui
@pytest.mark.smoke

def test_open_account_page(driver):
    account = Customer_Account(driver)
    assert account.open_account_page() == True
 
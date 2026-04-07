from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Services.basepage import BasePage

class Customer_Account(BasePage):
    account_button_locator= (By.XPATH, "//*[@id='section-21057']/header/nav/div/div/div[3]/div[2]/button")
    enter_email_field_locator=(By.XPATH, '//*[@id="email"]')
    enter_password_field_locator = (By.XPATH, '//*[@id="password"]')
    sign_in_button_locator=(By.XPATH, '/html/body/main/div[1]/div/div[2]/form/div[4]/button')
    account_button_after_sign_locator = (By.XPATH, '/html/body/header/div[1]/div/div/div[3]/div[2]/a')
    account_signed_in_fields_locator =(By.XPATH, '/html/body/main/div[1]/div/aside/div/nav/ul')
    login_error_locator = (By.XPATH, "//*[contains(@class,'error') or contains(@class,'alert')]")


    def open_account_page(self, timeout=10):
        account_button = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.account_button_locator)
        )
        account_button.click()
        enter_email_field = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.enter_email_field_locator)
        )
        return enter_email_field.is_displayed()

#To enter the login credentials in the fields
    def enter_login_credentials(self, email, password, timeout=10):
        enter_email_field = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.enter_email_field_locator)
        )
        enter_password_field = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.enter_password_field_locator)
        )
        sign_in_button = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.sign_in_button_locator)
        )

        enter_email_field.clear()
        enter_email_field.send_keys(email)
        enter_password_field.clear()
        enter_password_field.send_keys(password)
        sign_in_button.click()
        return True

    def is_logged_in(self, timeout=10):
        account_button_after_signin = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.account_button_after_sign_locator)
        )
        account_button_after_signin.click()
        account_signed_in_fields = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.account_signed_in_fields_locator)
        )
        return account_signed_in_fields.is_displayed()

    def has_login_error(self, timeout=5):
        try:
            error_elem = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.login_error_locator)
            )
            return error_elem.is_displayed()
        except Exception:
            return False
        

    


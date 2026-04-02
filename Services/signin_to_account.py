from selenium.webdriver.common.by import By

from Services.basepage import BasePage

class Customer_Account(BasePage):
    account_button_locator= (By.XPATH, "//*[@id='section-21057']/header/nav/div/div/div[3]/div[2]/button")
    enter_email_field_locator=(By.XPATH, '//*[@id="email"]')
    enter_password_field_locator = (By.XPATH, '//*[@id="password"]')
    sign_in_button_locator=(By.XPATH, '/html/body/main/div[1]/div/div[2]/form/div[4]/button')

    def open_account_page(self):
        
        try:
            account_button = self.find_element(*self.account_button_locator)
            enter_email_field = self.find_element(*self.enter_email_field_locator)           account_button.click()
            assert enter_email_field.is_displayed()
            self.driver.implicit.wait(5)

        except Exception as e:
            print(f"Error:{e}")
            
#To enter the login credentials in the fields
    def enter_login_credentials(self, email,password):

        try:

            enter_email_field = self.find_element(*self.enter_email_field_locator)
            enter_password_field = self.find_element(*self.enter_password_field_locator)
            sign_in_button= self.find_element(*self.sign_in_button_locator)
 
            enter_email_field.send_keys(email)
            enter_password_field.send_keys(password)
            sign_in_button.click()

        except Exception as e:
            print(f"Log: {e}")     
        
    


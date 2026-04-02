from selenium.webdriver.common.by import By

from Services.basepage import BasePage

class Customer_Acccount(BasePage):
    def open_account_page(self):
        account_button= self.driver.find_element(By.XPATH, "//*[@id='section-21057']/header/nav/div/div/div[3]/div[2]/button")
        enter_password_field = self.driver.find_element(By.XPATH, '//*[@id="email']")
        try:
            account_button.click()
            assert enter_password_field.is_displayed()
            self.driver.implicitly_Wait(5)
        except Exception as e:
            print(f"Error:{e}")
    


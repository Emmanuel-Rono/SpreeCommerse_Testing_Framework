from selenium.webdriver.common.by import By

from Services.basepage import BasePage

class Customer_Acccount(BasePage):
    def open_account_page(self):
        account_button= self.driver.find_element(By.XPATH, "//*[@id='section-21057']/header/nav/div/div/div[3]/div[2]/button")
        try:
            account_button.click()
        except Exception as e:
            print(f"Error:{e}")
    
    def specify_size(self):
        pass


    def specify_quantity():
        pass
    
    

#Add to cart
    def add_to_cart():
        pass

    

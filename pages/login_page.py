from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver=driver

    username=(By.ID, "username")
    password=(By.ID,"password")
    login_button=(By.CSS_SELECTOR,"button[type='submit']")
    success_message=(By.ID,"flash")

    def enter_username(self,user):
        self.driver.find_element(*self.username).send_keys(user)

    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
      self.driver.find_element(*self.login_button).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text






























































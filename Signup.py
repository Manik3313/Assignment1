import Base_class
class Test_Sign_up(Base_class):
    def test_signup(self):
        self.driver.find_element_by_link_text("Sign up").click()
        self.driver.find_element_by_xpath("//div/input[@name='firstName']").send_keys("Rajesh")
        self.driver.find_element_by_xpath("//div/input[@name='lastName']").send_keys("Panwar")
        self.driver.find_element_by_xpath("//div/input[@name='email']").send_keys("rajeshpanwar1717@gmail.com")
        self.driver.find_element_by_xpath("//div/input[@type='password']").send_keys("password")
        self.driver.find_element_by_xpath("//span/input[@type='checkbox']").click()
        if self.driver.find_element_by_xpath("//span[@class='MuiButton-label']").is_enabled():
            print("Signup")
            self.driver.find_element_by_xpath("//span[@class='MuiButton-label']").click()




from time import sleep
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://creds.appwrk.com/sign-in")
driver.maximize_window()
sleep(5)

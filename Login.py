import Base_class
class Test_login(Base_class):
    def test_login(self):
        self.driver.find_element_by_xpath("//div/input[@name='email']").send_keys("rajeshpanwar1717@gmail.com")
        self.driver.find_element_by_xpath("//div/input[@name='password']").send_keys("password")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        print("hello")



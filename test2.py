
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

email = "tester@mailinator.com"
name = "Jan"
surname = "Kowalski"
password = "Tester1234@"
birthdate_dmr = ['1', '7', '1987']


class TestRegistration(unittest.TestCase):
    """
    Mój scenariusz/przypadek testowy
    """

    def setUp(self) -> None:
        """
        Warunki wstępne testu
        """
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def testLogin(self):
        signin_btn = self.driver.find_element_by_class_name("login")
        signin_btn.click()
        email_input = self.driver.find_element_by_id("email")
        email_input.send_keys(email)
        passwd_input = self.driver.find_element_by_id("passwd")
        passwd_input.send_keys(password)
        create_btn = self.driver.find_element_by_name("SubmitLogin")
        create_btn.click()

    def tearDown(self) -> None:
        """
        Porządki po teście
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)

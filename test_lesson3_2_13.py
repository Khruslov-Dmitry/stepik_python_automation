from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        first_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        first_name.send_keys("first_name")
        last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        last_name.send_keys("last_name")
        email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        email.send_keys("email")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text = "Congratulations! You have successfully registered!"
        actual_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, actual_text, "Text don't match")

    def test_registration2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        first_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        first_name.send_keys("first_name")
        last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        last_name.send_keys("last_name")
        email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        email.send_keys("email")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text = "Congratulations! You have successfully registered!"
        actual_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, actual_text, "Text don't match")


if __name__ == "__main__":
    unittest.main()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]')
    first_name.send_keys('first_name')
    
    last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]')
    last_name.send_keys('last_name')
    
    email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]')
    email.send_keys('email')
    
    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'example.txt'
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)
    
    # Нажать кнопку "Submit"
    submit_btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_btn.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
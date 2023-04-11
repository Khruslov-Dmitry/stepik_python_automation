from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    y = calc(x)
    
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(y)
        
    # Отмечаем чекбокс и радиокнопку, и кликаем кнопку подтверждения
    checkbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkbox.click()
    
    radiobtn = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiobtn.click()
    
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
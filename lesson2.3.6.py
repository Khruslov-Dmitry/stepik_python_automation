from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    submit_btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_btn.click()
    
    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)
    
    # Пройти капчу для робота и получить число-ответ
    x = int(browser.find_element(By.ID, 'input_value').text)
    
    def func_x(x):
        return math.log(abs(12*math.sin(x)))
        
    y = func_x(x)
    
    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)
    
    submit_btn1 = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(1)
    print(browser.switch_to.alert.text)
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
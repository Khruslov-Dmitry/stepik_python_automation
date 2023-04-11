from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x
    var_x = int(browser.find_element(By.ID, 'input_value').text)
    
    # Посчитать математическую функцию от x
    def func_x(var_x):
        return math.log(abs(12*math.sin(var_x)))
        
    var_y = func_x(var_x)
        
    # Ввести ответ в текстовое поле
    input_field = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
    input_field.send_keys(var_y)
        
    # Выбрать checkbox "I'm the robot"
    im_the_robot = browser.find_element(By.ID, 'robotCheckbox')
    im_the_robot.click()
    
    # Переключить radiobutton "Robots rule!"
    robots_rule = browser.find_element(By.ID, 'robotsRule')
    robots_rule.click()
    
    # Нажать на кнопку "Submit"
    submit_btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_btn.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
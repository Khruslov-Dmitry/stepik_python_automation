from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # посчитать сумму заданных чисел
    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    total_sum = num1 + num2
    str_sum = str(total_sum)
    
    # нахождение суммы в выпадающем списке
    ddlist = Select(browser.find_element(By.ID, 'dropdown'))
    ddlist.select_by_value(str_sum)
        
    # кликаем подтверждение
    submit_btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
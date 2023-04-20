from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск элемента картинки
    treasure_pic = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    valuex = treasure_pic.get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
        
    y = calc(valuex)
    
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(y)
        
    # Отмечаем чекбокс и радиокнопку, и кликаем кнопку подтверждения
    checkbox = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    checkbox.click()
    
    radiobtn = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    radiobtn.click()
    
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    # Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element 
    # из библиотеки expected_conditions        
    # Нажать на кнопку "Book"
    right_moment = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x = int(browser.find_element(By.ID, 'input_value').text)


    def func_x(x):
        return math.log(abs(12 * math.sin(x)))


    y = func_x(x)

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    time.sleep(1)
    print(browser.switch_to.alert.text)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

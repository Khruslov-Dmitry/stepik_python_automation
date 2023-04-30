import math
import time

import pytest
from creds_for_authorization import login, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def answer():
    return str(math.log(int(time.time())))


@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
])
def test_authorization(browser, link):
    browser.implicitly_wait(15)
    link = f'{link}'
    browser.get(link)
    browser.find_element(By.ID, "ember33").click()
    browser.find_element(By.ID, "id_login_email").send_keys(login)
    browser.find_element(By.ID, "id_login_password").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    time.sleep(5)  # add sleep to avoid StaleException
    answer_field = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )
    answer_field.clear()
    answer_field.send_keys(answer())
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    time.sleep(2)
    feedback_element = WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    feedback_text = feedback_element.text
    assert "Correct!" == feedback_text

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    url = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(url)

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

    browser.switch_to.window(browser.window_handles[-1])

    x_element = browser.find_element(By.CSS_SELECTOR, '[id = "input_value"]')
    x = x_element.text

    input1 = browser.find_element(By.CSS_SELECTOR, '[id = "answer"]')
    input1.send_keys(calc(x))

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

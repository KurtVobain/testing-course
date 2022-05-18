from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    # Получаем первый и второй элемент суммы
    x = browser.find_element(By.CSS_SELECTOR, "[id = 'num1']")
    x = int(x.text)

    y = browser.find_element(By.CSS_SELECTOR, "[id = 'num2']")
    y = int(y.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x+y))

    button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
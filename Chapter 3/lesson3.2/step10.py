import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    def test_right(self):
        # Ссылка, по которой проходит тест:
        #  http://suninjuly.github.io/registration1.html
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(service=Service('C:/chromedriver/chromedriver.exe'))
        browser.get(link)

        input1 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your first name']"
        )
        input1.send_keys("Ivan")

        input2 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your last name']"
        )
        input2.send_keys("Petrov")

        input3 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your email']"
        )
        input3.send_keys("Smolensk")

        input4 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your phone:']"
        )
        input4.send_keys("727755")

        input5 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your address:']"
        )
        input5.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        true_welcome_text = "Congratulations! You have successfully registered!"
        self.assertEqual(
            welcome_text,
            true_welcome_text,
            f'Expected {true_welcome_text}, got {welcome_text}'
        )

    def test_wromg(self):
        # Ссылка, по которой проходит тест:
        #  http://suninjuly.github.io/registration1.html
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(service=Service('C:/chromedriver/chromedriver.exe'))
        browser.get(link)

        input1 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your first name']"
        )
        input1.send_keys("Ivan")

        input2 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your last name']"
        )
        input2.send_keys("Petrov")

        input3 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your email']"
        )
        input3.send_keys("Smolensk")

        input4 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your phone:']"
        )
        input4.send_keys("727755")

        input5 = browser.find_element(
            By.XPATH, "//input[@placeholder='Input your address:']"
        )
        input5.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        true_welcome_text = "Congratulations! You have successfully registered!"
        self.assertEqual(
            welcome_text,
            true_welcome_text,
            f'Expected {true_welcome_text}, got {welcome_text}'
        )


if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver
import time


class TestRegister(unittest.TestCase):

    def register_successfully(self, link):
        try:

            # link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            element1 = browser.find_element_by_css_selector('div.first_block input.first')
            element1.send_keys("bla bla1")

            element2 = browser.find_element_by_css_selector('div.first_block input.second')
            element2.send_keys("bla bla2")

            element3 = browser.find_element_by_css_selector('div.first_block input.third')
            element3.send_keys("bla bla3")

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

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            # assert "Congratulations! You have successfully registered!" == welcome_text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'welcome_text should'
                                                                                                 'be "Congratulations!'
                                                                                                 ' You have '
                                                                                                 'successfully '
                                                                                                 'registered!"')

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(10)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_register_successfully_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.register_successfully(link)

    def test_register_successfully_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.register_successfully(link)


#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main()

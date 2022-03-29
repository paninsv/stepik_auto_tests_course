from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num_1_element = browser.find_element_by_id('num1')
    num_2_element = browser.find_element_by_id('num2')

    summ = int(num_1_element.text) + int(num_2_element.text)

    print(f'{summ=}')

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summ))  # ищем элемент с текстом


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn.btn-default')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text
    #


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

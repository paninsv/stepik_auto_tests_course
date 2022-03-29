import math
import os

from selenium import webdriver
import time


def calc(x: str):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    first_name_field = browser.find_element_by_css_selector('[name = "firstname"]')
    last_name_field = browser.find_element_by_css_selector('[name = "lastname"]')
    email_field = browser.find_element_by_css_selector('[name = "email"]')

    first_name_field.send_keys('Уася')
    last_name_field.send_keys('Пупкин')
    email_field.send_keys('yasya@gmail.com')



    # x_element = browser.find_element_by_id('input_value')
    # x_text = x_element.text
    # calc_result = calc(x_text)
    # print(calc_result)
    #
    # answer_element = browser.find_element_by_id('answer')
    #
    # browser.execute_script("return arguments[0].scrollIntoView(true);", answer_element)
    # answer_element.send_keys(calc_result)
    #
    # check_box_label_robot = browser.find_element_by_css_selector("[for = 'robotCheckbox']")
    # check_box_label_robot.click()
    #
    # radio_label_robot = browser.find_element_by_css_selector('[for ="robotsRule"]')
    # radio_label_robot.click()
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file_to_upload.txt')  # добавляем к этому пути имя файла
    browse_button = browser.find_element_by_id('file')

    browse_button.send_keys(file_path)

    button = browser.find_element_by_css_selector('button.btn-primary')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



    #
    # # Отправляем заполненную форму
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()
    #
    # # Проверяем, что смогли зарегистрироваться
    # # ждем загрузки страницы
    # time.sleep(1)
    #
    # # находим элемент, содержащий текст
    # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # # записываем в переменную welcome_text текст из элемента welcome_text_elt
    # welcome_text = welcome_text_elt.text



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



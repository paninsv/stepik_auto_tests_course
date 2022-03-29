import math

from selenium import webdriver
import time


def calc(x: str):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button.trollface.btn.btn-primary')
    button.click()

    time.sleep(0.5)
    browser.switch_to.window(browser.window_handles[1])


    x_element = browser.find_element_by_id('input_value')
    x_text = x_element.text
    calc_result = calc(x_text)
    print(f'{calc_result = }')
    #
    answer_element = browser.find_element_by_id('answer')
    answer_element.send_keys(calc_result)
    #
    submit_button = browser.find_element_by_css_selector('button.btn.btn-primary')
    submit_button.click()
    # #
    # time.sleep(2)
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
    #
    # button = browser.find_element_by_css_selector('button.btn-primary')
    # # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    #


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



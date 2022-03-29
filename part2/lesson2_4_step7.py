import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



def calc(x: str):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    #
    book_button = browser.find_element_by_id('book')
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    book_button.click()


    x_element = browser.find_element_by_id('input_value')
    x_text = x_element.text
    calc_result = calc(x_text)
    print(calc_result)
    #
    answer_element = browser.find_element_by_id('answer')

    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_element)
    answer_element.send_keys(calc_result)
    #

    #
    button = browser.find_element_by_id('solve')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()



finally:
    time.sleep(10)
    browser.quit()

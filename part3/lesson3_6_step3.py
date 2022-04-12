import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

question_numbers = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']
# question_numbers = ['236895']


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestCorrectInResponse:
    message = ''

    @pytest.mark.parametrize('question_number', question_numbers)
    def test_correct_in_response(self, browser, question_number):
        link = f"https://stepik.org/lesson/{question_number}/step/1"

        browser.get(link)
        answer = math.log(int(time.time()))

        # # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        # WebDriverWait(browser, 20).until(
        #     EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        # )

        textarea = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "textarea.ember-text-area.ember-view.textarea.string-quiz__textarea"))
        )

        textarea.send_keys(str(answer))

        submit_button = browser.find_element_by_css_selector('button.submit-submission')

        submit_button.click()

        # time.sleep(600)

        correct_label = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "pre.smart-hints__hint"))
        )
        if correct_label:
            print(f'ну вроде нашли!:{correct_label.text}')
            if "Correct" not in correct_label.text:
                TestCorrectInResponse.message += correct_label.text
            assert "Correct" in correct_label.text, f'Сообщение полностью: {TestCorrectInResponse.message}'


# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# class TestLogin:
#     def test_guest_should_see_login_link(self, browser, language):
#         link = f"http://selenium1py.pythonanywhere.com/{language}/"
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#         # этот тест запустится 2 раза
#
#     def test_guest_should_see_navbar_element(self, browser, language):
#         print(language)
#         assert True

from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///" + path + '/test_alert.html'
        self.driver.get(file_path)
        self.driver.maximize_window()

    def test_alert(self):
        self.driver.find_element_by_id('alert').click()
        alert = self.driver.switch_to.alert
        sleep(3)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element_by_id('confirm').click()
        confirm = self.driver.switch_to.alert
        confirm.accept()
        sleep(3)
        confirm.dismiss()

    def test_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        sleep(5)
        prompt.accept()
        sleep(3)


if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    case.test_prompt()

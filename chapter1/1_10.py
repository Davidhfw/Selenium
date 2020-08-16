from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///" + path + '/test_wait.html'
        self.driver.get(file_path)

    def test(self):
        self.driver.find_element_by_id('btn').click()
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.text_to_be_present_in_element(By.ID, 'id 2'))
        print('OK')


if __name__ == '__main__':
    case = TestCase()
    case.test()
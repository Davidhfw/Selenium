from selenium import webdriver
from time import sleep
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///" + path + '/forms.html'
        print(file_path)
        print(path)
        self.driver.get(file_path)
        self.driver.maximize_window()

    def test_login(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('admin')
        pwd = self.driver.find_element_by_id('pwd')
        pwd.send_keys('123')
        print(username.get_attribute('value'))
        print(pwd.get_attribute('value'))
        sleep(3)
        self.driver.find_element_by_id('submit').click()
        self.driver.switch_to.alert.accept()
        sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_login()
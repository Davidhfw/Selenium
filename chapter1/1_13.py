from selenium import webdriver
from time import sleep, strftime, localtime, time
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')

    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)

        # self.driver.save_screenshot('baidu.png')
        #
        st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        file_name = st + '.png'
        # self.driver.save_screenshot(file_name)
        path = os.path.abspath('screenshots')
        print(path)
        file_path = path + '/' + file_name
        self.driver.get_screenshot_as_file(file_path)
        sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test1()

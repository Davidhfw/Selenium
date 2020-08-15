from selenium import webdriver
from time import sleep
import os

from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///" + path + '/forms3.html'
        print(file_path)
        print(path)
        self.driver.get(file_path)
        self.driver.maximize_window()

    def test_select(self):
        se = self.driver.find_element_by_id('provise')
        select = Select(se)
        # select.select_by_index(2)
        # sleep(2)
        # select.select_by_value('bj')
        # sleep(2)
        # select.select_by_visible_text('TianJin')
        # sleep(2)
        for i in range(3):
            select.select_by_index(i)
            sleep(2)
        sleep(3)

        self.driver.quit()

    # def test_select_all(self):
    #     se = self.driver.find_element_by_id('provise')
    #     select = Select(se)
    #     for i in range(3):
    #         select.select_by_index(i)
    #         sleep(1)
    #     sleep(3)
    #     # select.deselect_all()
    #     self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_select()
    
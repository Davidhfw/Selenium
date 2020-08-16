from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.sahitest.com/demo/clicks.htm')


    def test_mouse(self):
        btn = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn).perform()

        sleep(2)

        btn = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        ActionChains(self.driver).click(btn).perform()

        sleep(2)

        btn = self.driver.find_element_by_xpath('/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn).perform()
        sleep(5)

        self.driver.quit()

    def test_keys(self):
        # 测试粘贴、复制等键盘组合键操作
        self.driver.get("http://www.baidu.com")
        # kw = self.driver.find_element_by_id('kw')
        # kw.send_keys('selenium')
        # kw.send_keys(Keys.CONTROL, 'a')
        # sleep(2)
        # kw.send_keys(Keys.CONTROL, 'x')
        # sleep(2)
        # kw.send_keys(Keys.CONTROL, 'v')
        # sleep(2)
        en = self.driver.find_element_by_link_text('新闻')
        ActionChains(self.driver).move_to_element(en).click().perform()
        sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_keys()
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
        self.driver.get('http://www.baidu.com')


    def test1(self):
        self.driver.execute_script("alert('test')")
        sleep(2)
        self.driver.switch_to.alert.accept()

    def test2(self):
        js = 'return document.title'
        title = self.driver.execute_script(js)
        print(title)

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

    def test3(self):
        js = 'var q = document.findElementById("kw");q.style.border="2px" solid red'
        self.driver.execute_script(js)
        sleep(3)
        self.driver.quit()

    def test4(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        js = 'window.scrollTo(0, document.body.scrollHeight)'
        self.driver.execute_script(js)
        sleep(2)


if __name__ == '__main__':
    case = TestCase()
    case.test4()
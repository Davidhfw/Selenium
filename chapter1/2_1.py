from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://wwww.baidu.com")
        self.driver.maximize_window()

    # 测试通过id来定位页面元素
    def test_id(self):
        element = self.driver.find_element_by_id('kw')
        element.send_keys('selenium')
        print(type(element))
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    # 测试通过name来定位页面元素
    def test_name(self):
        element = self.driver.find_element_by_name('wd')
        element.send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    # 测试通过tag name来定位页面元素
    def test_tag(self):
        element = self.driver.find_element_by_tag_name('input')[0]
        print(element)


    # 测试通过link text定位页面元素
    def test_link_text(self):
        self.test_id()
        self.driver.find_element_by_link_text('百度首页').click()
        sleep(3)

    # 测试通过partial link text定位页面元素
    def test_partial_link_text(self):
        self.test_id()
        self.driver.find_element_by_partial_link_text('首页').click()
        sleep(3)
        self.driver.quit()

    # 测试通过xpath定位元素
    def test_xpath(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('极客时间')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    # 测试通过class定位元素
    def test_class_name(self):
        self.driver.find_element_by_class_name('s_ipt').send_keys('极客时间')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    #测试通过css selector定位元素
    def test_css_selector(self):
        self.driver.find_element_by_css_selector('#kw').send_keys('极客时间')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_all(self):
        self.driver.find_element(By.ID, value='kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_id()
    case.test_class_name()
    case.test_css_selector()
    case.test_link_text()
    case.test_partial_link_text()
    case.test_name()
    case.test_xpath()
    case.test_tag()


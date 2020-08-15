from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        sleep(2)

    def test_sleep(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        sleep(2)
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    def test_implicity(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('kw').send_keys('selenium')
        # sleep(2)
        self.driver.find_element_by_id('su').click()
        # sleep(3)
        self.driver.quit()

    def test_wait(self):
        wait = WebDriverWait(self.driver, 2)
        # self.driver.implicitly_wait(10)
        wait.until(EC.title_is('百度一下，你就知道'))
        self.driver.find_element_by_id('kw').send_keys('selenium')
        # sleep(2)
        self.driver.find_element_by_id('su').click()
        # sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    # case.test_sleep()
    # case.test_implicity()
    case.test_wait()
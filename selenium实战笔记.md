# Selenium实战笔记

[toc]

## 1 前言

本笔记仅适用于本人学习极客时间上《Selenium自动化测试实践》，不用于商业用途。本笔记对于selenium的webdriver的安装、python环境安装及selenium库的安装就不一一介绍了，直接从实战部分讲起。关于这部分内容，简单的介绍下，语言中的selenium包或库提供了一整套指令，而驱动程序则是实际听指令驱动浏览器的。我们通过编写程序，驱使浏览器干活。

## 2 Selenium语法

selenium的学习中，其基本的语法是必须要掌握的，下面我们就从selenium语法讲起。

### 2.1 Selenium元素定位方法

selenium中实现元素定位有以下８种方法，具体方法如下表所示：

| NO   | 方法描述                          | 方法描述                 |
| ---- | --------------------------------- | ------------------------ |
| 1    | find_element_by_id                | 通过id获取元素           |
| 2    | find_element_by_name              | 通过name定位元素         |
| 3    | find_element_by_xpath             | 通过xpath定位元素        |
| 4    | find_element_by_link_text         | 通过链接文本定位元素     |
| 5    | find_element_by_partial_link_text | 通过部分链接文本定位元素 |
| 6    | find_element_by_tag_name          | 通过标签名定位元素       |
| 7    | find_element_by_class_name        | 通过类名称定位元素       |
| 8    | find_element_by_css_selector      | 通过css选择器定位元素    |

### 2.2 find_element_*方法解析

- 有一些定位元素是复数形式，可以返回多个元素，比如`find_elements_by_name`、`find_elements_by_id`等；

- find_element是一个更加通用的方法，具体定义如下：

  ```python
  def find_element(self, by=By.ID, value=None):
      """
      Find an element given a By strategy and locator. Prefer the find_element_by_* methods when
      possible.
  
      :Usage:
          element = driver.find_element(By.ID, 'foo')
  
      :rtype: WebElement
      """
      if self.w3c:
      	if by == By.ID:
      		by = By.CSS_SELECTOR
      		value = '[id="%s"]' % value
      	elif by == By.TAG_NAME:
      		by = By.CSS_SELECTOR
      	elif by == By.CLASS_NAME:
      		by = By.CSS_SELECTOR
      		value = ".%s" % value
      	elif by == By.NAME:
      		by = By.CSS_SELECTOR
      		value = '[name="%s"]' % value
      return self.execute(Command.FIND_ELEMENT, {
      	'using': by,
      	'value': value})['value']
  ```

可以通过第二个参数来指定定位元素的方式。接下来我们通过具体代码实例来展示下Selenium定位元素的方式：

```python
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By


class TestCase(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://wwww.baidu.com")
        self.driver.maximize_window() #最大化窗口

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
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('北京')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    # 测试通过class定位元素
    def test_class_name(self):
        self.driver.find_element_by_class_name('s_ipt').send_keys('北京')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

    #测试通过css selector定位元素
    def test_css_selector(self):
        self.driver.find_element_by_css_selector('#kw').send_keys('北京')
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
```

### 2.3 Selenium WebDriver属性

WebDriver的常用属性如下表所示：

| No   | 属性                         | 属性描述     |
| ---- | ---------------------------- | ------------ |
| 1    | driver.name                  | 浏览器名称   |
| 2    | driver.current_url           | 当前url      |
| 3    | driver.title                 | 当前页面标题 |
| 4    | driver.page_source           | 当前页面源码 |
| 5    | driver.current_window_handle | 窗口句柄     |
| 6    | driver.window_handles        | 窗口所有句柄 |

下面再来看下WebDriver的其他方法的用法，具体如下表所示。

| No   | 方法                            | 方法描述       |
| ---- | ------------------------------- | -------------- |
| 1    | driver.back()                   | 浏览器后退     |
| 2    | driver.forward()                | 浏览器前进     |
| 3    | driver.refresh()                | 浏览器刷新     |
| 4    | driver.close()                  | 关闭当前窗口   |
| 5    | driver.quit()                   | 浏览器退出     |
| 6    | driver.switch_to.frame()        | 切换到frame    |
| 7    | driver.switch_to.alert          | 切换到alert    |
| 8    | driver.switch_to.active_element | 切换到活动元素 |

接下来我们就看看实际的代码示例：

```python
from selenium import webdriver
from time import sleep


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()

    def test_prop(self):
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.window_handles)
        print(self.driver.page_source)
        self.driver.quit()

    def test_method(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(5)
        self.driver.back()
        sleep(3)
        self.driver.refresh()
        sleep(3)
        self.driver.forward()
        self.driver.close() # 关闭当前tab，　quit关闭浏览器

    def test_window(self):
        self.driver.find_element_by_link_text('新闻').click()
        windows = self.driver.window_handles
        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(3)


if __name__ == '__main__':
    case = TestCase()
    # case.test_prop()
    # case.test_method()
    case.test_window()
```

### 2.4 Selenium WebElement属性

当我们使用WebDriver的find方法定位元素后，会返回一个WebElement对象，该对象用来描述Web页面上的元素，接下来，我们看下WebElement对象的常用属性和方法。

WebElement的常用属性和方法如下表所示。

| No   | 属性     | 属性描述   |
| ---- | -------- | ---------- |
| 1    | id       | 标示       |
| 2    | size     | 宽高       |
| 3    | rect     | 宽高和坐标 |
| 4    | tag_name | 标签名称   |
| 5    | text     | 文本内容   |

下面是一些关于WebElement属性的实例方法展示，具体如下：

接下来我们看下WebElement的常用方法，具体如下表所示。

| No   | 方法                    | 方法描述   |
| ---- | ----------------------- | ---------- |
| 1    | send_keys()             | 输入内容   |
| 2    | clear()                 | 清空内容   |
| 3    | click()                 | 单击       |
| 4    | get_attribute()         | 获得属性值 |
| 5    | is_selected()           | 是否被选中 |
| 6    | is_enabled()            | 是否可用   |
| 7    | is_displayed()          | 是否显示   |
| 8    | value_of_css_property() | css属性值  |

接下来我们看看实际中的WebElement的属性和方法使用。

```python
from selenium import webdriver
from time import sleep

from selenium.webdriver.remote.webelement import WebElement


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://sahitest.com/demo/linkTest.htm")

    def test_element(self):
        e = self.driver.find_element_by_id('t1')
        # e1 = WebElement
        # print(type(e1))
        print(e.id)
        print(e.tag_name)
        print(e.size)
        print(e.rect)
        print(e.text)

    def test_web_element_method(self):
        e = self.driver.find_element_by_id('t1')
        e.send_keys('hello world')
        sleep(2)
        print(e.get_attribute('type'))
        print(e.get_attribute('value'))
        print(e.get_attribute('name'))
        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))
        sleep(2)
        e.clear()

    def test_method2(self):
        form_element = self.driver.find_element_by_xpath('/html/body/form[1]')
        form_element.find_element_by_id('t1').send_keys('baba')
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_element()
    case.test_web_element_method()
    case.test_method2()
```

### 2.5 Selenium操作form表单

form表单是我们经常使用的一种Web网页，经常用在用户登录、用户注册等操作中，接下来我们介绍如何测试form表单，具体过程如下：

1. 定位表单元素；
2. 输入测试值；
3. 判断表单元素属性；
4. 获取表单元素属性；
5. 提交表单进行验证；

接下来我们看下具体的操作代码。我们先新建一个包括form表单的页面，具体代码如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="javascript:alert('hello')">
UserName: <input type="text" name="username" id="username"><br>
Password: <input type="password" name="pwd" id="pwd"><br>
<input type="submit" value="submit" id="submit">
</form>
</body>
</html>
```

python测试代码如下：

```python
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
```

记住html表单文件和python测试代码必须位于同一目录下。

### 2.6 Selenium操作checkbox和radiobutton

form表单中经常会用到checkbox和radiobutton，其中，checkbox表示多选框，radiobutton表示单选框。比如，一个注册表单要收集用户爱好可以使用checkbox，性别选择使用radiobutton按钮。

#### checkbox

- 如果checkbox有id属性可直接通过id定位，如果没有可通过input标签名称定位，然后通过type属性进行过滤；
- 选择或反选checkbox，可使用click()方法；

#### radiobutton

- radiobutton有相同名称，多个值，可先通过名称获取，然后按值过滤；
- 选择或反选checkbox，使用click()；

接下来我们就展示下具体的使用细节。

- forms.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="javascript:alert('test')"></form>
swimming: <input type="checkbox" name="swimming" value="swimming"><br>
reading: <input type="checkbox" name="reading" value="reading"><br>
    <hr>
    gendor: <input type="radio" name="gender" value="male"><br>
    <input type="radio" name="gender" value="female"><br>
<input type="submit" value="login">

</body>
</html>
```

```python
from selenium import webdriver
from time import sleep
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = "file:///" + path + '/forms2.html'
        print(file_path)
        print(path)
        self.driver.get(file_path)
        self.driver.maximize_window()

    def test_checkbox(self):
        swimming = self.driver.find_element_by_name('swimming')
        if not swimming.is_selected():
            swimming.click()
        reading = self.driver.find_element_by_name('reading')
        if not reading.is_selected():
            reading.click()
        sleep(5)
        swimming.click()
        sleep(5)
        self.driver.quit()

    def test_radio(self):
        lst = self.driver.find_elements_by_name('gender')
        lst[0].click()
        sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_checkbox()
    case.test_radio()
```

### 2.7 Selenium操作下拉列表

处理下拉列表，需要用到Selenium中的一个工具类Select，接下来我们看下这个类中的常用方法。

| No   | 方法/属性                  | 方法/属性描述 |
| ---- | -------------------------- | ------------- |
| 1    | select_by_value()          | 根据值选择    |
| 2    | select_by_index()          | 根据索引选择  |
| 3    | select_by_visible_text()   | 根据文本选择  |
| 4    | deselect_by_value()        | 根据值反选    |
| 5    | deselect_by_index()        | 根据索引反选  |
| 6    | deselect_by_visible_text() | 根据文本反选  |
| 7    | deselect_all()             | 反选所有      |
| 8    | options()                  | 所有选项      |
| 9    | all_selected_options()     | 所有选中选项  |
| 10   | first_selected_option()    | 第一个选择项  |

接下来，我们看看Selenium操作下拉列表的实例。

我们先创建一个forms.html网页，网页源代码如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="javascript:alert('test')">
    provide:
    <select name="provise" id="provise">
        <option value="bj">Beijing</option>
        <option value="tj">TianJin</option>
        <option value="sh">ShangHai</option>
    </select>
</form>

</body>
</html>
```

selenium实际代码如下：

```python
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
        select.select_by_index(2)
        sleep(2)
        select.select_by_value('bj')
        sleep(2)
        select.select_by_visible_text('TianJin')
        sleep(2)
        for i in range(3):
            select.select_by_index(i)
            sleep(2)
        sleep(3)

        self.driver.quit()

    def test_select_all(self):
        se = self.driver.find_element_by_id('provise')
        select = Select(se)
        for i in range(3):
            select.select_by_index(i)
            sleep(1)
        sleep(3)
        # select.deselect_all()
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_select()
    
```

### 2.8 Selenium处理弹窗

页面弹框有三种：

- alert：用来提示；
- confirm：用来确认；
- prompt：输入内容；

具体方法如下表所示，

| No   | 方法/属性  | 方法/属性描述 |
| ---- | ---------- | ------------- |
| 1    | accept()   | 接受          |
| 2    | dismiss()  | 取消          |
| 3    | text()     | 显示的文本    |
| 4    | sen_keys() | 输入内容      |

接下来我们看看Selenium处理弹窗的实例。我们先创建一个test_alert.html，然后在展示下操作实例。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<a href="javascript:alert('提示框')" id="alert">Alert</a><br>
<a href="javascript:confirm('真的要删除数据吗？')" id="confirm">Confirm</a><br>
<a href="javascript:var age = prompt('请输入年龄');document.write(age)" id="prompt">Prompt</a><br>

</body>
</html>
```

```python
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
```

### 2.9 Selenium的三种等待方式

在UI自动化测试中，难免会遇到网络环境不稳定，网络慢的情况，这时如果不做任何处理，必然会导致代码执行失败，因为找不到指定的页面元素。另外一种情况是ajax异步加载机制。这时候我们就需要用到wait，而在Selenium中，有三种等待方式，接下来我们一一介绍下。

- time.sleep (固定等待时间)。

> 在开发自动化测试框架中，最忌讳使用python自带的time模块的sleep方法，虽然可以指定等待时间，但是当网络状况良好时，必然会造成时间浪费。导致整个项目执行时间延长，不推荐使用。不过可以用于代码调试中。

- implicity_wait (隐式等待)

> - 隐式等待实际上指定了一个最长的等待时间，如果在规定时间内，网页加载完成，则执行下一步。否则一直等到时间结束，然后执行下一步。这样的隐式等待会有一个坑就是，javaScript一般是放在body的最后才加载。实际上页面元素已经加载完毕，却还在等待全部页面加载结束。
>
> - 隐式等待对整个driver周期都起作用，只需要设置一次。

- WebDriverWait　(显示等待)

  - WebDriverWait是selenium提供的显示等待模块路径。

  ```python
  from selenium.webdriver.support.wait import WebDriverWait
  ```

  - WebDriverWait介绍

  | No   | 参数               | 参数说明                                        |
  | ---- | ------------------ | ----------------------------------------------- |
  | 1    | driver             | 传入WebDriver实例                               |
  | 2    | timeout            | 超时时间                                        |
  | 3    | poll_frequency     | 调用until或until_not中方法时间间隔，默认为0.5秒 |
  | 4    | ignored_exceptions | 忽略的异常                                      |

  这个模块只有两个方法，即until和until_not，具体参数如下：

  | No   | 参数    | 参数说明                                                     |
  | ---- | ------- | ------------------------------------------------------------ |
  | 1    | method  | 在等待间隙，每隔一段时间调用这个方法的传入，直到返回值不是false。 |
  | 2    | message | 如果超时，抛出TimeoutException，将message传入异常            |

接下来，我们看下具体操作实例

```python
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
```

### 2.10 Selenium等待条件

Selenium中的鼠标和键盘事件被封装在ActionChains类中，正确的使用方法是`ActionChains(driver).click(btn).perform()`下表中列出的方法。

| NO   | 方法描述                           | 方法描述                                                     | 返回值     |
| ---- | ---------------------------------- | ------------------------------------------------------------ | ---------- |
| 1    | title_is                           | 判断title是否出现                                            | 布尔值     |
| 2    | title_contains                     | 判断title是否包含某些字符                                    | 布尔值     |
| 3    | presence_of_element_located        | 判断某个元素是否被加载到dom树中，并不代表该元素一定可见      | WebElement |
| 4    | visibility_of_element_located      | 判断某个元素是否被加载到dom树中，并且该元素一定可见，宽高大于０ | WebElement |
| 5    | visibility_of                      | 判断某个元素是否可见，如果可见就返回这个元素                 | WebElement |
| 6    | presence_of_all_elements_located   | 判断至少一个元素是否被加载到dom树中                          | 列表       |
| 7    | visibility_of_any_elements_located | 判断至少一个元素是否可见                                     | 列表       |
|      |                                    |                                                              |            |


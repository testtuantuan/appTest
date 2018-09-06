# AppTester
本程序参照pyse的思路改编而成

#### 介绍：
AppTester基于 appium ( webdriver )进行了二次封装，为UI自动化提供更方便简洁的操作方法

#### 特点：
* 支持多种定位方法
* 本框架只是对appium原生方法进行简单的封装，精简部分，目前足够使用

#### 安装说明：
* python3.5+ : http://www.python.org/
* selenium 3.12.0 : http://pypi.python.org/pypi/selenium
* appium : http://appium.io/
* android SDK : http://www.androiddevtools.cn/#
* ios Xcode : https://developer.apple.com/xcode/ide/

```
> python setup.py install
```

#### 例子：
请查看case/test_main.py

```python
from base.apper import Apper
from base.test_runner import TestRunner
from base.base_case import TestCase


class MainProcess(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Apper()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_main(self):
        """测试主流程:"""
        self.element_wait("id", "com.czb.chezhubang:id/guide_image")
        self.swipe_left()
        self.swipe_left()
        self.element_wait("id", "com.czb.chezhubang:id/button")
        self.click("id=>.com.czb.chezhubang:id/button")
        if self.element_wait("id", "com.czb.chezhubang:id/ad_close"):
            self.click("css=>.com.czb.chezhubang:id/ad_close")
        else:
            pass
        print("已经进入油站列表啦！")
        if self.get_element("css=>.com.czb.chezhubang:id/cardView"):
            print("列表中有油站！")


if __name__ == '__main__':
    run = TestRunner('./', '车主邦测试用例', '测试环境：android', 'Medivh')
    run.debug()
```

运行测试用例说明：
* 测试用例文件命名必须以“__test__”开头。
* `TestRunner()` 默认匹配当前目录下"test*.py"的文件并执行。当然也可以指定测试目录，例如：
TestRunner("path/you/project/test_case/")  # 注意用斜线"/"表示路径。
* 执行`run()`方法运行测试用例并生成测试报告，在调试测试用例过程中可以使用 `debug()` 方法将不会生成HTML测试报告。


  css选择器参考手册：
  http://www.w3school.com.cn/cssref/css_selectors.asp
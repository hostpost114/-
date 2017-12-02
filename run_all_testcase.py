import unittest
from HTMLTestRunner import HTMLTestRunner
import time

testcase_dir = 'E:\\unittest\\alarm'


def creat_suit():
    suit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover('alarm', pattern='test_*.py', top_level_dir=None)
    for test_suit in discover:
        for test_case in test_suit:
            suit.addTest(test_case)
    return suit
"""1.discover方法里面有三个参数：

-case_dir:这个是待执行用例的目录。

-pattern：这个是匹配脚本名称的规则，test*.py意思是匹配test开头的所有脚本。

-top_level_dir：这个是顶层目录的名称，一般默认等于None就行了。"""

all_test_cases = creat_suit()
f = open('test.html', 'wb')
runner = HTMLTestRunner(stream=f,
                        title=u'测试报告',
                        description=u'测试用例执行情况')
runner.run(all_test_cases)
f.close()

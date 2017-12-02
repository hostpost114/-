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


all_test_cases = creat_suit()
f = open('test.html', 'wb')
runner = HTMLTestRunner(stream=f,
                        title=u'测试报告',
                        description=u'测试用例执行情况')
runner.run(all_test_cases)
f.close()

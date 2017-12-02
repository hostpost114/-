from alarm.test_case import *
from HTMLTestRunner import HTMLTestRunner

if __name__ == "__main__":
    suit = unittest.TestSuite()
    x = [Home_page('test_001_click_set_clock'), Home_page('test_002_click_repeat'),
         Home_page('test_003_click_touch_ring'), Home_page('test_004_click_vibration'),
         Home_page('test_005_click_touch_lable')]
    suit.addTests(x)
    # suit.addTest(MyTestCase('test_something'),MyTestCase('test_wec'))
    runner = unittest.TextTestRunner(verbosity=2)
    f = open('test.html', 'wb')
    runner = HTMLTestRunner(stream=f,
                            title=u'测试报告',
                            description=u'测试用例执行情况')
    runner.run(suit)
    f.close()

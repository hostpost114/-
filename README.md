# -
Clock














from message_test.testcase_message import *
from HTMLTestRunner import HTMLTestRunner


if __name__=="__main__":
    suit =unittest.TestSuite()
    suit.addTests(unittest.TestLoader().loadTestsFromTestCase(Home_page))
    # x=[Home_page('test_001_check'),Home_page('test_002_touch_search_button'), Home_page('test_003_add_button')]
    # suit.addTests(x)
    # suit.addTest(MyTestCase('test_something'),MyTestCase('test_wec'))
    #runner = unittest.TextTestRunner(verbosity=2)
    with open('test.html','wb') as f:
        runner =HTMLTestRunner(stream=f,
                           title=u'测试报告',
                           description=u'测试用例执行情况'，
                           verbosity=2)
        runner.run(suit)

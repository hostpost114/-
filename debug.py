import time
from time import sleep
from appium import webdriver
import unittest
class MyTestCase(unittest.TestCase):
    now_time = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
    print(now_time)
    @classmethod
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'DU2SSE15C3115777'
        desired_caps['appPackage'] = 'com.android.deskclock'
        desired_caps['appActivity'] = '.AlarmsMainActivity'
        # desired_caps['unicodekeybord'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def test_process(self):
        try:
            self.driver.find_element_by_id('alarm_tv_add').click()


        except Exception as e:
            print(e)
        def tearDown(self):
            self.driver.quit()
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(MyTestCase('test_process'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)
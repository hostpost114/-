from alarm.page import Clock_nao
from appium import webdriver
import unittest
from time import sleep


class Home_page(unittest.TestCase):
    # 测试闹钟主页的新建闹钟和设置
    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.4',
            'deviceName': 'DU2SSE15C3115777',
            'appPackage': 'com.android.deskclock',  # 'com.android.contacts'
            'appActivity': '.AlarmsMainActivity',  # '.activities.DialtactsActivity'
            'unicodekeybord': 'True',
            "resetKeyboard": "True"
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.main_page = Clock_nao(cls.driver)
        # self.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 点击新建闹钟
    def test_001_click_set_clock(self):
        li = Clock_nao(self.driver)
        li.click_set_clock()
        """点击新建闹钟按钮"""
        self.assertEqual(self.driver.find_element_by_name('只响一次').text, '只响一次')

    # 点击重复
    def test_002_click_repeat(self):
        self.main_page.click_repeat()
        self.assertEqual(self.driver.find_element_by_name('自定义').text, '自定义')
        self.main_page.click_every_day()
        self.assertEqual(self.driver.find_element_by_name('每天').text, '每天')
        self.main_page.save_alarm()

    # 点击铃声
    def test_003_click_touch_ring(self):
        self.test_001_click_set_clock()
        self.main_page.click_touch_ring()
        self.main_page.click_none()
        self.main_page.save_alarm()
        self.assertEqual(self.driver.find_element_by_name('静音').text, '静音')
        # 点击振动按钮

    def test_004_click_vibration(self):
        self.test_001_click_set_clock()
        self.main_page.click_vibration()
        self.main_page.not_save_alarm()

    # 点击标签
    def test_005_click_touch_lable(self):
        self.test_001_click_set_clock()
        self.main_page.click_touch_lable()
        self.main_page.input_lable2()
        self.main_page.click_lable_ok()
        self.assertEqual(self.driver.find_element_by_name('my first alarm').text, 'my first alarm')
        self.main_page.save_alarm()

    # 进入闹钟设置
    def test_006_touch_settinga(self):
        self.test_001_click_set_clock()
        self.main_page.touch_settinga()
        self.driver.keyevent(4)

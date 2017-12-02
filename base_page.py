# coding=utf-8
# Date:2017.12.02
# 测试机闹钟的一些共有元素的封装
from selenium.webdriver.support.ui import WebDriverWait
import time, os


class Base_page(object):
    def __init__(self, driver):
        self.driver = driver

    def fin_element(self, *loc):
        try:
            WebDriverWait(self.driver, 30).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:

            print("%s未找到%s" % (self, loc))

    def send_key(self, loc, value, clear_first=True, click_first=True):
        try:
            if clear_first:
                self.fin_element(*loc).click()
            if click_first:
                self.fin_element(*loc).clear()
                self.fin_element(*loc).send_key(value)
        except AttributeError:
            print("%s未能点击该元素%s" % (self, loc))

    def click(self, loc):
        try:
            self.fin_element(*loc).click()
            time.sleep(2)
        except AttributeError:
            print("%s未找到%s" % (self, loc))

    # 进行屏幕截图操作
    def get_screenshot(self):
        dir_path = "E:\Fail_screen_shot/"
        pic_name = time.strftime('%Y%m%d%H%M%S') + '.png'
        pic_url = dir_path + pic_name
        try:
            self.driver.save_screenshot(pic_url)
            print("screen_name:%s" % pic_name)
        except:
            raise

    # 获取屏幕高度和宽度
    def get_windowsize(self):
        height = self.driver.get_windows_size()["height"]
        width = self.driver.get_windows_size()["width"]
        return height, width

    # 输入滑动的坐标来滑动手机
    def swip_all(self, start_x, start_y, end_x, end_y, duration=None):
        self.get_windowsize()
        self.driver.swip(start_x, start_y, end_x, end_y, duration)
        """
     其他写法
     # 获取屏幕的高度和宽度
    def get_windowsize(self):
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        return height, width
    # 向上滑动屏幕
    def swipe_up(self):
        height, width = self.get_windowsize()
        self.driver.swipe(width/2, height * 3/4, width/2, height * 1/4)  
     其他写法
    def get_size(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return x,y
    #获取屏幕尺寸平滑动
    def swipe_left(self):#封装滑动坐标
        l=self.get_size()
        # x1=int(l[0]*0.95)
        # y1=int(l[1]*0.5)
        # x2=int(l[0]*0.05)
        self.driver.swip(x1,y1,x2,y1)
        """

    # 向上滑动屏幕
    def swipe_up(self):
        height, width = self.get_windowsize()
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height * 1 / 4)

    # 向下滑动屏幕
    def swipe_down(self):
        height, width = self.get_windowsize()
        self.driver.swipe(width / 2, height * 1 / 4, width / 2, height * 3 / 4)

    # 向左滑动屏幕
    def swipe_left(self):
        height, width = self.get_windowsize()
        self.driver.swipe(width * 3 / 4, height / 2, width * 1 / 4, height / 2)

    # 向右滑动屏幕
    def swipe_right(self):
        height, width = self.get_windowsize()
        self.driver.swipe(width * 1 / 4, height / 2, width * 3 / 4, height / 2)

    # 获取当前activity的名称
    def get_curent_activity_name(self):
        activity_name = self.driver.current_activity
        print('Current activity name is: %s' % activity_name)

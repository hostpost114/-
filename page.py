from alarm.base_page import Base_page
from selenium.webdriver.common.by import By


# 继承Basepage类
class Clock_nao(Base_page):
    # 定位元素：通过元素属性定位 闹钟 页面中的元素

    """ 新建闹钟"""
    set_clock = (By.ID, 'alarm_tv_add')
    # 重复
    repeat = (By.ID, 'repeat_layout')
    every_day = (By.NAME, '每天')
    cencel = (By.ID, 'button2')

    """铃声"""
    # 点击铃声
    touch_ring = (By.ID, 'Ringtone_layout')
    # 无玲声
    none = (By.ID, 'checkedtextview')
    # 取消
    ring_celcel = (By.ID, 'icon1')
    # 确定
    ring_ok = (By.ID, 'icon2')

    """振动"""
    vibration = (By.ID, 'btn_Vibrate')

    """标签"""
    # 点击标签
    touch_lable = (By.ID, 'label_layout')
    # 确定标签
    lable_cencel = (By.ID, 'button1')
    # 取消标签
    lable_ok = (By.ID, 'button2')
    # 标签输入框
    input_lable = (By.ID, 'username_edit')
    """闹钟新建后是否保存"""
    alarm_save = (By.ID, 'icon2')
    alarm_celcel = (By.ID, 'icon1')
    """ """
    # 封装
    # 设置
    # 里面的页面元素
    # 点击设置
    touch_setting = (By.ID, 'com.android.deskclock:id/alarm_tv_settings')
    """点击新建闹钟"""

    def click_set_clock(self):
        self.click(self.set_clock)
        # self.click('set_clock')
        self.get_screenshot()

    # 点击重复
    def click_repeat(self):
        self.click(self.repeat)
        self.get_screenshot()

    # 点击每天
    def click_every_day(self):
        self.click(self.every_day)
        self.get_screenshot()

    # 点击取消
    def click_cencel(self):
        self.click(self.cencel)
        self.get_screenshot()

    """点击铃声 """

    # 点击铃声
    def click_touch_ring(self):
        self.click(self.touch_ring)

    # 选择无铃声
    def click_none(self):
        self.click(self.none)
        self.get_screenshot()

    # 点击取消
    def click_ring_celcel(self):
        self.click(self.ring_celcel)
        self.get_screenshot()

    # 点击确定
    def click_ring_ok(self):
        self.click(self.ring_ok)
        self.get_screenshot()

    """点击震动按钮"""

    def click_vibration(self):
        self.click(self.vibration)
        self.get_screenshot()

    """点击标签"""

    # 点击标签
    def click_touch_lable(self):
        self.click(self.touch_lable)

    # 标签中输入字符
    def input_lable2(self):
        self.send_key('input_lable', 'my first alarm')

    # 点击取消
    def click_lable_cencel(self):
        self.click(self.lable_cencel)

    # 点击确定
    def click_lable_ok(self):
        self.click(self.lable_ok)

    # 取消保存闹钟
    def not_save_alarm(self):
        self.click(self.alarm_celcel)

    # 保存闹钟
    def save_alarm(self):
        self.click(self.alarm_save)

    """点击设置"""

    def touch_settinga(self):
        self.click(self.touch_setting)

    # 点击在响设置
    def ring_agin(self):
        self.driver.tap([(777, 538)])
        self.get_screenshot()

# -*- coding: utf-8  -*-
"""
Author:Cy
 向左翻页
 向右翻页
 向上翻页
 向下翻页

"""
import sys

from appium.webdriver.common.touch_action import TouchAction


def SwipeLeft(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1 = int(x * 0.7)
    x2 = int(x * -0.5)
    y1 = int(y * 0.5)
    driver.swipe(x1, y1, x2, y1, 1500)
    pass


def SwipeRight(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1 = int(x * 0.1)
    x2 = int(x * 0.5)
    y1 = int(y * 0.7)
    driver.swipe(x1, y1, x2, y1, 1500)
    pass


def SwipeUp(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1 = int(x * 0.5)
    y1 = int(y * 0.7)
    y2 = int(y * -0.5)
    driver.swipe(x1, y1, x1, y2, 1500)
    pass


def SwipeDown(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    x1 = int(x * 0.5)
    y1 = int(y / 4)
    y2 = int(y * 3 / 4)
    action = TouchAction(driver)
    action.press(x=x1, y=y1).wait(ms=500).move_to(x=x1, y=y2).release()
    action.perform()
    pass

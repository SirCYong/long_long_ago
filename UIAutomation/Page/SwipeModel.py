from UIAutomation.Page import BasePage


class SwipeModel(BasePage):
    # 获取屏幕宽和高
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

        # 向下滑动
    def swipe_down(self, t):
        len = self.get_size()
        x1 = int(len[0] * 0.5)
        y1 = int(len[1] * 0.25)
        y2 = int(len[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)
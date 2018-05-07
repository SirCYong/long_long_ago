from .GlobalVar import GlobalVarClass
from .Logger import run_info_log
import time


def initial_element_error_wrapper(driver):
    screenshot_file = GlobalVarClass.get_case_name() + "_" + str(time.time()) + "_screenshot.png"
    driver.save_screenshot(GlobalVarClass.get_screenshot_path() + screenshot_file)
    print("错误截图：")
    print('<img src="' + GlobalVarClass.get_screenshot_path() + screenshot_file + '" width="800px" />')
    run_info_log(u'XML解析失败.', GlobalVarClass.get_log_file())
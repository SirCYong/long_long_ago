from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://172.16.7.37:801/base/uploadFile.jsp")
driver.maximize_window()
sleep(10)
a = driver.find_element_by_xpath("html/body/form/input[1]")
a.send_keys('/Users/cy/Downloads/test1107.xlsx')
driver.quit()
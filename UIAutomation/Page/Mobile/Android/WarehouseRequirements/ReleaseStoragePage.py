# -*- coding:utf-8 -*-
from time import sleep

from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
from UIAutomation.Page import BasePage

class ReleaseStoragePage(BasePage):
    def __init__(self,driver):
        BasePage.__init__(self,driver, __file__)
        self.driver = driver
        try:
            self.is_loaded()
        except ParseXmlErrorException:
            assert False

    def initial_element(self):
        try:
            self.is_loaded()
            self.page_factory()
        except NoSuchWindowException():
            BasePage.screen_shot(self)
            assert False
        pass

    def page_factory(self):
        name_list = ['Cross_BorderBtn','TransPort_Btn','E_CommerceBtn','Un_E_CommerceBtn',
                     'RunningVolumeBtn','PublicBtn','LightExtravagantBtn',
                     'luxuryBtn','BeginTime','EndTime','Location'
                     'Province','CityBtn','ProcessingCapacityBtn','WarehouseAreaBtn',
                     'CompleteBtn','ContinueBtn']
        ele_dic = page_element_factory(__file__, name_list)
        self.Cross_BorderBtn_element = get_element(self.driver, ele_dic['Cross_BorderBtn'])
        self.TransPort_Btn_element = get_element(self.driver, ele_dic['TransPort_Btn'])
        self.E_CommerceBtn_element = get_element(self.driver, ele_dic['E_CommerceBtn'])
        self.Un_E_CommerceBtn_element = get_element(self.driver, ele_dic['Un_E_CommerceBtn'])
        self.RunningVolumeBtn_element = get_element(self.driver, ele_dic['RunningVolumeBtn'])
        self.PublicBtn_element = get_element(self.driver, ele_dic['PublicBtn'])
        self.LightExtravagantBtn_element = get_element(self.driver, ele_dic['LightExtravagantBtn'])
        self.luxuryBtn_element = get_element(self.driver, ele_dic['luxuryBtn'])
        self.BeginTime_element = get_element(self.driver, ele_dic['BeginTime'])
        self.EndTime_element = get_element(self.driver, ele_dic['EndTime'])
        self.Location_element = get_element(self.driver, ele_dic['Location'])
        self.Province_element = get_element(self.driver, ele_dic['Province'])
        self.CityBtn_element = get_element(self.driver, ele_dic['CityBtn'])
        self.ProcessingCapacityBtn_element = get_element(self.driver, ele_dic['ProcessingCapacityBtn'])
        self.WarehouseAreaBtn_element = get_element(self.driver, ele_dic['WarehouseAreaBtn'])
        self.CompleteBtn_element = get_element(self.driver, ele_dic['CompleteBtn'])
        self.ContinueBtn_element = get_element(self.driver, ele_dic['ContinueBtn'])
        pass

    def click_Cross_BorderBtn(self):
        self.initial_element()
        get_element(self.driver, self.Cross_BorderBtn_element).click()
        pass

    def click_TransPort_Btn(self):
        self.initial_element()
        get_element(self.driver, self.TransPort_Btn_element).click()
        pass
    def click_E_CommerceBtn(self):
        self.initial_element()
        get_element(self.driver, self.E_CommerceBtn_element).click()
        pass

    def click_Un_E_CommerceBtn(self):
        self.initial_element()
        get_element(self.driver, self.Un_E_CommerceBtn_element).click()
        pass

    def click_RunningVolumeBtn(self):
        self.initial_element()
        get_element(self.driver, self.RunningVolumeBtn_element).click()
        pass

    def click_PublicBtn(self):
        self.initial_element()
        get_element(self.driver, self.PublicBtn_element).click()
        pass

    def click_LightExtravagantBtn(self):
        self.initial_element()
        get_element(self.driver, self.LightExtravagantBtn_element).click()
        pass

    def click_luxuryBtn(self):
        self.initial_element()
        get_element(self.driver, self.luxuryBtn_element).click()
        pass

    def click_BeginTime(self):
        self.initial_element()
        get_element(self.driver, self.BeginTime_element).click()
        pass

    def click_EndTime(self):
        self.initial_element()
        get_element(self.driver, self.EndTime_element).click()
        pass

    def click_Location(self):
        self.initial_element()
        get_element(self.driver, self.Location_element).click()
        pass

    def click_Province(self):
        self.initial_element()
        get_element(self.driver, self.Province_element).click()
        pass
    def click_CityBtn(self):
        self.initial_element()
        get_element(self.driver, self.CityBtn_element).click()
        pass

    def click_ProcessingCapacityBtn(self):
        self.initial_element()
        get_element(self.driver, self.ProcessingCapacityBtn_element).click()
        pass

    def click_WarehouseAreaBtn(self):
        self.initial_element()
        get_element(self.driver, self.WarehouseAreaBtn_element).click()
        pass

    def click_CompleteBtn(self):
        self.initial_element()
        get_element(self.driver, self.CompleteBtn_element).click()
        pass
    
    def click_ContinueBtn(self):
        self.initial_element()
        get_element(self.driver, self.ContinueBtn_element).click()
        pass





































    def is_loaded(self):
        pass


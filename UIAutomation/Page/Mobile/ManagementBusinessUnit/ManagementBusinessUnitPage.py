from selenium.common.exceptions import NoSuchWindowException
from UIAutomation.Page import BasePage
from UIAutomation.Utils import page_element_factory, get_element, ParseXmlErrorException
__author__ = 'zhoujin'


class ManagementBusinessUnit(BasePage):
    """
    管理业务单位
    假定已经创建过一个一级业务单位
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver, __file__)
        self.driver = driver
        self.management_button_locator = None
        self.add_locator = None
        self.fleeting_locator = None
        self.purview_locator = None
        self.append_locator = None
        self.life_locator = None
        self.third_set_locator = None
        self.finish_locator = None
        self.pay_locator = None
        self.build_locator = None
        self.sign_locator = None
        self.management_locator = None
        self.perfect_locator = None
        self.update_locator = None
        self.import_locator = None
        self.carriage_locator = None
        self.transport_locator = None
        self.change_locator = None
        self.settlement_locator = None
        self.owner_locator = None
        self.storage_locator = None
        self.supply_locator = None
        self.set_locator = None
        self.end_locator = None
        self.icon_back = None
        try:
            self.is_loaded()
            self.initial_element()
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
        if self.is_run_ios():
            self._page_factory_ios()
        else:
            self._page_factory_android()

    def _page_factory_ios(self):
        name_list = ['management_button', 'add', 'end', 'purview', 'append', 'third_set', 'finish', 'pay', 'build',
                     'sign', 'management', 'perfect', 'update', 'import', 'carriage', 'transport', 'change',
                     'settlement', 'owner', 'storage', 'supply', 'set', 'icon_back']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.management_button_locator = ele_dic['management_button']  # 管理按钮
        self.add_locator = ele_dic['add']  # 添加二级业务单位
        self.end_locator = ele_dic['end']  # 输入名字完成
        self.purview_locator = ele_dic['purview']  # 选择权限
        self.append_locator = ele_dic['append']  # 添加三级业务单位
        self.third_set_locator = ele_dic['third_set']  # 三级业务单位设置权限
        self.finish_locator = ele_dic['finish']  # 完成业务单位管理
        self.pay_locator = ele_dic['pay']  # 支付
        self.build_locator = ele_dic['build']  # 创建业务单位
        self.sign_locator = ele_dic['sign']  # 签订系统服务
        self.management_locator = ele_dic['management']  # 管理业务单位
        self.perfect_locator = ele_dic['perfect']  # 完善商品资料
        self.update_locator = ele_dic['update']  # 支付完成更新原业务状态
        self.import_locator = ele_dic['import']  # 导入库位库存
        self.carriage_locator = ele_dic['carriage']  # 找运输供应
        self.transport_locator = ele_dic['transport']  # 完善运输契约
        self.change_locator = ele_dic['change']  # 管理者权限变更
        self.settlement_locator = ele_dic['settlement']  # 运输费用结算记录
        self.owner_locator = ele_dic['owner']  # 填写拥有的资产类型
        self.storage_locator = ele_dic['storage']    # 为三级业务单位设置权限
        self.supply_locator = ele_dic['supply']     # 为三级业务单位设置权限
        self.set_locator = ele_dic['set']  # 权限设置完成
        self.icon_back_locator = ele_dic['icon_back']   # 返回按钮
        pass

    def _page_factory_android(self):
        name_list = ['management_button', 'add', 'fleeting', 'end', 'purview', 'append', 'life', 'third_set',
                     'finish', 'pay', 'build', 'sign', 'management', 'perfect', 'update', 'import',
                     'carriage', 'transport', 'change', 'settlement', 'owner', 'storage', 'supply', 'set']
        ele_dic = page_element_factory(self.xml_file, name_list)
        self.management_button_locator = ele_dic['management_button']  # 管理按钮
        self.add_locator = ele_dic['add']  # 添加二级业务单位
        self.fleeting_locator = ele_dic['fleeting']   # 二级业务单位名字“流年”
        self.end_locator = ele_dic['end']  # 输入名字完成
        self.purview_locator = ele_dic['purview']  # 选择权限
        self.append_locator = ele_dic['append']  # 添加三级业务单位
        self.life_locator = ele_dic['life']     # 三级业务单位名字“生活”
        self.third_set_locator = ele_dic['third_set']  # 三级业务单位设置权限
        self.finish_locator = ele_dic['finish']  # 完成业务单位管理
        self.pay_locator = ele_dic['pay']  # 支付
        self.build_locator = ele_dic['build']  # 创建业务单位
        self.sign_locator = ele_dic['sign']  # 签订系统服务
        self.management_locator = ele_dic['management']  # 管理业务单位
        self.perfect_locator = ele_dic['perfect']  # 完善商品资料
        self.update_locator = ele_dic['update']  # 支付完成更新原业务状态
        self.import_locator = ele_dic['import']  # 导入库位库存
        self.carriage_locator = ele_dic['carriage']  # 找运输供应
        self.transport_locator = ele_dic['transport']  # 完善运输契约
        self.change_locator = ele_dic['change']  # 管理者权限变更
        self.settlement_locator = ele_dic['settlement']  # 运输费用结算记录
        self.owner_locator = ele_dic['owner']  # 填写拥有的资产类型
        self.storage_locator = ele_dic['storage']  # 为三级业务单位设置权限
        self.supply_locator = ele_dic['supply']  # 为三级业务单位设置权限
        self.set_locator = ele_dic['set']  # 权限设置完成

    def is_loaded(self):
        pass

    def management_business_unit(self):
        if self.is_run_ios():
            self._management_business_unit_ios()
        else:
            self._management_business_unit_android()

    def _management_business_unit_ios(self):
        """
        进入管理业务单位
        """
        # 管理
        self.action.click(self.management_button_locator)
        # 添加第一个二级业务单位
        self.action.click(self.add_locator)
        # 输入二级业务单位名
        mobile_size = self.action.get_window_size()
        print(mobile_size)
        width = mobile_size['width']
        height = mobile_size['height']
        h = 0.65 * height
        w = width * 0.06
        self.driver.tap([(w, h)], 100)
        # 输入名字完成
        self.action.click(self.end_locator)
        # 为二级业务单位添加权限
        self.action.click(self.purview_locator)
        # 添加权限
        self.action.click(self.pay_locator)
        self.action.click(self.build_locator)
        self.action.click(self.sign_locator)
        self.action.click(self.management_locator)
        self.action.click(self.perfect_locator)
        self.action.click(self.update_locator)
        self.action.click(self.import_locator)
        self.action.click(self.carriage_locator)
        self.action.click(self.transport_locator)
        self.action.click(self.change_locator)
        self.action.click(self.settlement_locator)
        self.action.click(self.owner_locator)
        # 设置完成
        self.action.click(self.set_locator)
        # 添加第一个三级业务单位
        self.action.click(self.append_locator)
        # 输入三级业务单位名
        mobile_size = self.action.get_window_size()
        print(mobile_size)
        width = mobile_size['width']
        height = mobile_size['height']
        h = 0.65 * height
        w = width * 0.06
        self.driver.tap([(w, h)], 100)
        # 输入名字完成
        self.action.click(self.end_locator)
        # 为三级业务单位添加权限
        self.action.click(self.third_set_locator)
        # 添加权限
        self.action.click(self.storage_locator)
        self.action.click(self.supply_locator)
        # 设置完成
        self.action.click(self.set_locator)
        # 完成选择权限
        self.action.click(self.finish_locator)

    def _management_business_unit_android(self):
        """
        进入管理业务单位
        """
        # 管理
        self.action.click(self.management_button_locator)
        # 添加第一个二级业务单位
        self.action.click(self.add_locator)
        # 输入二级业务单位名
        self.action.send_keys(self.fleeting_locator, u'流年')
        # 输入名字完成
        self.action.click(self.end_locator)
        # 为二级业务单位添加权限
        self.action.click(self.purview_locator)
        # 添加权限
        self.action.click(self.pay_locator)
        self.action.click(self.build_locator)
        self.action.click(self.sign_locator)
        self.action.click(self.management_locator)
        self.action.click(self.perfect_locator)
        self.action.click(self.update_locator)
        self.action.click(self.import_locator)
        self.action.click(self.carriage_locator)
        self.action.click(self.transport_locator)
        self.action.click(self.change_locator)
        self.action.click(self.settlement_locator)
        self.action.click(self.owner_locator)
        # 设置完成
        self.action.click(self.set_locator)
        # 添加第一个三级业务单位
        self.action.click(self.append_locator)
        # 输入三级业务单位名
        self.action.send_keys(self.life_locator, u'生活')
        # 输入名字完成
        self.action.click(self.end_locator)
        # 为三级业务单位添加权限
        self.action.click(self.third_set_locator)
        # 添加权限
        self.action.click(self.storage_locator)
        self.action.click(self.supply_locator)
        # 设置完成
        self.action.click(self.set_locator)
        # 完成选择权限
        self.action.click(self.finish_locator)

    def submit(self):
        if self.is_run_ios():
            self._submit_ios()
        else:
            self._submit_android()

    def _submit_ios(self):
        get_element(self.driver, ['ACCESSIBILITY_ID', 'icon back']).click()
        pass

    def _submit_android(self):
        self.driver.keyevent(4)
        self.driver.keyevent(4)
        pass

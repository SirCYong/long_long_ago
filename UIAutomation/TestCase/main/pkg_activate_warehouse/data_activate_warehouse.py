import random


class DataActivateWarehouse(object):
    """
    激活仓库测试数据
    """
    def __init__(self):
        pass

    # 激活仓库长期卡片名称
    activate_warehouse_long_card_name = "激活仓库"
    # 登录账户
    username = '15806044444'
    # 密码
    password = 'a123456'
    # 用户user_id
    user_id = '10001124'

    # ——激活仓库成功用例——
    # 仓库名称
    warehouse_name_success = "自动化新增仓库" + str(random.randint(10000000000, 99999999999))
    # 详细地址
    warehouse_area_success = "5000"
    # 仓库租金
    warehouse_rent_success = "20"
    # 仓库联系人
    warehouse_contact_success = "张三"
    # 仓库联系人电话号码
    warehouse_phone_success = "15806034323"

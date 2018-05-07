import random


class DataJobPointTypeSetting(object):
    """
    作业点设置测试数据
    """
    def __init__(self):
        pass

    # 作业点设置长期卡片名称
    job_point_type_setting_long_card_name = "作业点设置"
    # 登录账户
    username = '15806044444'
    # 密码
    password = 'a123456'
    # 用户user_id
    user_id = '10001124'

    # ——作业点设置成功用例——
    # 作业点类型名称
    job_point_type_name = "自动化新增的作业点" + str(random.randint(10000000000, 99999999999))


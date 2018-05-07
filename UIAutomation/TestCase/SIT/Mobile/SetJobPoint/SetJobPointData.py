# coding = utf-8


class SetJobPointData(object):
    """
    维护工作点测试数据
    """
    def __init__(self):
        pass

    # 维护工作点长期卡片名称
    job_point_long_card_name = "维护工作点"
    # 登录账户
    username = '15060020679'
    # 密码
    password = '123456'
    # 用户user_id
    user_id = '10001604'

    # ——新增工作点成功用例——
    # 扫码的特殊条码
    job_point_code_add_success = "666"

    # ——新增工作点条码无效用例——
    # 扫码的无效条码
    job_point_code_add_fail = "123435"

    # ——修改工作点成功用例——
    # 扫码的工作点条码
    job_point_code_modify_success = ""

    # --修改工作点失败用例——
    # 扫码的工作点条码
    job_point_code_modify_fail = ""


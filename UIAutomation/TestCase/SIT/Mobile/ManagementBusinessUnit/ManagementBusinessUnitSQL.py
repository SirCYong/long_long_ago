# -*- coding: utf-8 -*-
# language:zh-CN
'''
    author: zhoujin
   管理业务单位恢复数据
'''
# from UIAutomation.TestCase.SIT.Mobile.ManagementBusinessUnitSQL.ManagementBusinessUnit import get_creator_ukid
# from UIAutomation.Utils import basic_cit, close_oracle
from UIAutomation.Utils import basic_sit, close_oracle


def delete_business_unit(user_id=None):
    # con, curs = basic_cit()
    con, curs = basic_sit()
    # 删除业务单位
    try:
        # creator_ukid = get_creator_ukid(user_id)
        sql = '''delete from xdw_app.au_business_unit where  create_user_id='%s' and name not in ('岁月')
                 ''' % user_id
        curs.execute(sql)
        con.commit()
        close_oracle(con, curs)
        print('删除管理业务单位成功')
    except Exception as e:
        print('删除管理业务单位失败')
        print(e)
        close_oracle(con, curs)


def get_new_business_unit(user_id=10001474):
    # 建立业务单位后，查看新生成的记录来进行判断
    # con, curs = basic_cit()
    con, curs = basic_sit()
    try:
        dic = {}
        # creator_ukid = get_creator_ukid(user_id)
        sql = '''select t.name from xdw_app.au_business_unit t where create_user_id = '%s' ''' % user_id
        print(sql)
        # print(name)
        curs.execute(sql)
        result1 = curs.fetchall()
        print(result1)
        return dic
    except Exception as e:
        print('获取业务单位信息失败')
        print(e)
        close_oracle(con, curs)

# 还原发布供货供应条件
from UIAutomation.Utils import Independent_cit
__author__ = 'ytz'


def RestoreSQL():
    try:  # 连接数据库配置还原信息，方便加载模块
        con, curs = Independent_cit()
        sql = '''UPDATE XDW_APP.MS_CARD SET status=0 WHERE  CARD_UKID=51755600000012177'''
        # 将结果赋值给state
        curs.execute(sql)
        con.commit()
        con.close()
    except Exception as e:
        print(e)
    print("数据库数据恢复")
    pass


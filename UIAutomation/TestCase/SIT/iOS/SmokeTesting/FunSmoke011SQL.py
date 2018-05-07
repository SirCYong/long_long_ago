# -*- coding:utf-8 -*-
# language:zh-CN
# Description：发布仓储需求的SQL 使用USER_ID为199294 登录账号：13318071102 密码:123456
from UIAutomation.Utils import Independent_cit, close_oracle


def FunSmoke011SQL():
        con, curs = Independent_cit()
        try:
            sql = [
                '''UPDATE XDW_APP.TS_OPERATION SET STATUS=0 WHERE OPERATION_UKID=51767600000016047''',  # 更新任务
                '''UPDATE XDW_APP.cm_participant_relation SET relation_status = 20 WHERE RELATED_UKID= 51767600000016047 ''', # 更新明细 此ID为任务的UKID
                '''UPDATE XDW_APP.MS_CARD SET STATUS = 0 WHERE OPERATION_UKID=51767600000016047''',  # 更新卡片状态
                '''UPDATE XDW_APP.cm_participant_relation SET RELATION_STATUS = 20 WHERE RELATED_UKID= 51767000000016045 '''] # 此ID为卡片的UKID

            for sql1 in sql:
                curs.execute(sql1)
                con.commit()
            close_oracle(con, curs)
            print("恢复数据成功!")
        except Exception as e:
            print (e)
            print("恢复数据失败!")


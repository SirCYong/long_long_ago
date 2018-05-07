from UIAutomation.Utils import basic_sit
from UIAutomation.Utils import close_oracle


def assert_publish_labour():
    con, curs = basic_sit()
    try:
        sql = ['''select o.status from xdw_app.ms_card o where o.card_type='PublishLaborDemand'order by
                o.create_time desc''']
        for sql1 in sql:
            curs.execute(sql1)
            cur = curs.fetchone()
            print(cur[0])
            assert cur[0]==10
            close_oracle(con, curs)
    except Exception as e:
        print(e)
        close_oracle(con, curs)
    print("数据验证成功")


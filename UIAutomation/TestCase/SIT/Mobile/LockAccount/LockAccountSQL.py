from UIAutomation.Utils import basic_sit
from UIAutomation.Utils import close_oracle


def assert_lock_account():
    """
    验证锁定数据是否正确
    :return:
    """
    con, curs = basic_sit()
    try:
        sql = ['''select oo.locked from xdw_app.ba_user  oo  where oo.user_id=10001625''']
        for sql1 in sql:
            curs.execute(sql1)
            cur = curs.fetchone()
            print(cur[0])
            assert cur[0] == 1
            close_oracle(con, curs)
    except Exception as e:
        print(e)
        close_oracle(con, curs)
    print("锁定数据验证成功")


def assert_unlock_account():
    """
    验证解锁数据是否正确
    :return:
    """
    con, curs = basic_sit()
    try:
        sql = ['''select oo.locked from xdw_app.ba_user oo  where oo.user_id=10001625''']
        for sql1 in sql:
            curs.execute(sql1)
            cur = curs.fetchone()
            print(cur[0])
            assert cur[0] == 0
            close_oracle(con, curs)
    except Exception as e:
        print(e)
        close_oracle(con, curs)
    print("解锁数据验证成功")
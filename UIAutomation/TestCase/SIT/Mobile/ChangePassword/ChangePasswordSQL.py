from UIAutomation.Utils import cit
from UIAutomation.Utils import close_oracle


def get_test_code():
    """
    获取验证码
    :return:
    """
    con, curs = cit()
    try:
        #select a.send_content from xdw_app.sa_sms a where a.create_time<trunc(sysdate+1) order by a.create_time desc
        sql = ['''
 SELECT a.send_content FROM xdw_app.sa_sms a WHERE a.create_time<trunc(sysdate+1)
 AND  a.mobile_no='enc_23EB56B76F418687F02A9137C891FCE3'ORDER BY a.create_time DESC ''']
        for sql1 in sql:
            curs.execute(sql1)
            cur = curs.fetchone()
            a = str(cur)
            import re
            line = re.findall(r"\d+\.?\d*", a)
            close_oracle(con, curs)
            print(line[0])
            return line[0]
    except Exception as e:
        print(e)
        close_oracle(con, curs)

if __name__ == '__main__':
    get_test_code()
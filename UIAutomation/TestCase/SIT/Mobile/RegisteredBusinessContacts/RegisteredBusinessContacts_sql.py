from UIAutomation.Utils import close_oracle, basic_cit

__author__ = "xuwangchao"

def get_first_info(user_id = 10001475):
    """
    获得第一页填写内容
    :param user_id:
    :return:
    """
    get_info = {}
    con, curs = basic_cit()
    try:
        sql0 = '''select * from xdw_app.cm_company_partner_relation t  where t.create_user_id={0} order by t.create_time desc'''.format(user_id)
        curs.execute(sql0)
        result = curs.fetchall()
        get_info["duijieren"]=result[0][2]
        get_info["duizhangren"] = result[0][4]
        get_info["lianxiren"] = result[0][6]
        get_info["lianxiren_mobile"] = result[0][7]
        get_info["jiedanren"] = result[0][8]
        get_info["location"] = result[0][20]
        close_oracle(con, curs)
        return get_info
    except Exception as e:
        print('获取第1页填写内容失败')
        close_oracle(con, curs)
        pass


def get_second_info(user_id = 10001475):
    """
    获得第二页填写内容
    :param user_id:
    :return:
    """
    get_info = set()
    con, curs = basic_cit()
    try:
        sql0 = '''select * from cm_identify t where t.create_user_id = {0} order by t.create_time desc'''.format(user_id)
        curs.execute(sql0)
        result = curs.fetchall()
        get_info.add(result[1][3])
        get_info.add(result[0][3])
        print(get_info)
        close_oracle(con, curs)
        return get_info
    except Exception as e:
        print('获取第2页填写内容失败')
        close_oracle(con, curs)
        pass

def get_second_empty_info(user_id = 10001475):
    """
    获得第二页填写内容
    :param user_id:
    :return:
    """
    get_info = set()
    con, curs = basic_cit()
    try:
        sql0 = '''select * from cm_identify t where t.create_user_id = {0} order by t.create_time desc'''.format(user_id)
        curs.execute(sql0)
        result = curs.fetchall()
        get_info.add(result[0][3])
        close_oracle(con, curs)
        return get_info
    except Exception as e:
        print('获取第2页填写内容失败')
        close_oracle(con, curs)
        pass

def clear_second_sql(user_id = 10001475):
    """
        :param user_id:
        :return:
        """
    con, curs = basic_cit()
    try:
        sql0 = '''delete from cm_identify a where a.create_user_id= {0}'''.format(user_id)
        curs.execute(sql0)
        con.commit()
        close_oracle(con, curs)
    except Exception as e:
        print('清除注册联系人数据第2页失败')
        close_oracle(con, curs)
        pass

def clear_first_sql(user_id = 10001475):
    """
        :param user_id:
        :return:
        """
    con, curs = basic_cit()
    try:
        sql0 = '''delete from xdw_app.cm_company_partner_relation a where a.create_user_id= {0}'''.format(user_id)
        curs.execute(sql0)
        con.commit()
        close_oracle(con, curs)
    except Exception as e:
        print('清除注册联系人数据第一页失败')
        close_oracle(con, curs)
        pass


if __name__ == '__main__':
    get_second_empty_info()
    get_first_info()


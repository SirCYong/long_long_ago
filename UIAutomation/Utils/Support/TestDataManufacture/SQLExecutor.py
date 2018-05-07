# -*- coding:utf-8 -*-
# 具体用户执行SQL的细节在这个模块里
# 这个模块的初始版本使用SQL语句拼接的方式,后面会改用SQLObject的方式来实现
from common.common_method.database.ConnetToOracleDatabase import basic_cit, close_oracle
from testcase.Support.TestDataManufacture import DataBaseTableConstants


# 条件是字典类型, 目前支持的条件性太简单,只支持输入1个或者2个and的条件查询,后面会根据输入的参数动态构建SQL语句
def sql_select(cursor, table_name, restrict):
    """
    拼接SQL select语句
    :param restrict: 条件
    :type restrict: dict
    :return:
    :rtype:
    :param cursor: DB
    :type cursor: curios
    :param table_name:
    :type table_name:string
    """
    if type(restrict) is not dict:
        raise Exception
    elif len(restrict) == 1:
        db_cursor = cursor.execute("""Select * from %s where %s = %s""" % (table_name, restrict.keys()[0], restrict.values()[0]))
    elif len(restrict) == 2:
        db_cursor = cursor.execute("""Select * from %s where %s = %s AND %s = %s""" % (table_name, restrict.keys()[0], restrict.values()[0],
                                                                                       restrict.keys()[1], restrict.values()[1]))
    else:
        raise SyntaxError
    result = []
    for rt in db_cursor:
        result.append(rt)
    return result
    pass


def sql_insert(cursor, table_name, column_name, *values):
    """
    拼接SQL insert语句
    :param cursor:
    :type cursor:
    :param table_name:
    :type table_name:
    :param column_name:
    :type column_name:
    :param values:
    :type values:
    """
    cursor.execute("""insert into %s %s VALUES %s""" % (table_name, column_name, values))
    pass


# 目前只能传入一个字典条件，后面会用map方法扩展一下支持多个
def sql_update(cursor, table_name, column_name, *values, **restrict):
    """
    拼接SQL Update语句
    :param cursor: SQL的浮标类型
    :type cursor: db curios
    :param table_name:
    :type table_name:
    :param column_name:
    :type column_name:
    :param values:
    :type values:
    :param restrict:
    :type restrict:
    """
    cursor.execute("""update %s set %s = %s where %s = %s """ % (table_name,
                   column_name, values, restrict.keys()[0], restrict.values()[0]))
    pass


# 返回SQL结果
def __list_result(db_cursor):
    list_result = []
    for result in db_cursor:
        list_result.append(result)
    return list_result
    pass


if __name__ == '__main__':
    conn, cur = basic_cit()
    # is_account_initialized(cur, '199083')
    sql_select(cur, DataBaseTableConstants.LOGIN_BASIC_USER, 'hah')
    close_oracle(conn, cur)

# -*- coding: utf-8 -*- #


from common.common_method.database.ConnetToOracleDatabase import basic_cit, basic
from common.exception.IscsException import NoSuchEnvironmentException, UserHasNotRegisterYetException
from testcase.Support.TestDataManufacture import DataBaseTableConstants
from testcase.Support.TestDataManufacture.SQLExecutor import sql_select

"""
Author: yong_li
这个模块为了实现自动化测试数据中注册用户的数据恢复
"""


def is_account_initialized(cursor, user_id):
    """
    这个方法去检查四个表格来判断这个用户是否存在于数据库中

    :param cursor: DB浮标类型,用来执行拼接的SQL语句
    :type cursor: curios
    :param user_id: 用户在DB里生成的ID
    :type user_id: string
    """

    # 把ID前面加一个前缀“TEST_ACCOUNT"
    account_name = 'TEST_ACCOUNT_%s' % user_id
    # 导入模块，利用反射去确认这个用户定义是否存在
    constance_module = __import__('UserDataConstants')
    try:
        account_defined_info = getattr(constance_module, account_name)
    except Exception as e:
        print(e.message)
        # 需要用户去手动把微信信息注册进入系统,然后把账号信息写入Constants文件,此为临时方案,如果工作量巨大，可以考虑使用安卓手机去完成第三方注册的任务
        raise NotImplementedError

    # 如果数据库用户值和手机号码返回值为空的话
    len_x = len(sql_select(cursor, DataBaseTableConstants.LOGIN_BASIC_USER, {'USER_ID': account_defined_info['id'],
                                                                             'MOBILE': account_defined_info['phone']}))
    if len_x == 0:
        raise UserHasNotRegisterYetException
    else:
        return True
    pass


def is_already_exists(table_name, cursor, **kwargs):
    """
    检测某个Table里面的项和值是否存在
    :param table_name: string， TableName是从用户定义的属性里面得来,有多少个Table会执行多少次.
    :type table_name: str
    :param cursor:
    :type cursor: cursor
    :param kwargs:
    :type kwargs: dict
    :return:
    :rtype: bool
    """
    if len(sql_select(table_name, cursor, **kwargs)) == 0:
        return False
    else:
        return True
    pass


def is_updated():
    pass


def is_recovered(**kwargs):
    pass



def get_db_connection():
    # 读取配置文件,得到当前脚本运行在那个环境上，CIT 或者 SIT
    # 从而建立不同的数据库连接,以及不同的用户数据

    pass


# 在数据库里判断这个用户ID是否满足已经定义的角色所需要的数据
# 为整个模块的主入口
def is_satisfied_for_this_role(user_id):
    """
    用户定义的元数据从excel表格里面获取
    :param cursor:
    :type cursor:
    :param user_id:
    :type user_id:str
    """
    db_conn, db_cursor = get_db_connection()

    #
    #
    #
    # is_account_initialized(db_cursor, user_id)
    # user_meta_data = with open;
    # # 去确认用户名下定义的必须存在的项是否全部存在
    # for line in user_meta_data:
    #     is_already_exists(db_cursor, line[])
    # defined_user_info = {}
    # is_already_exists(**defined_user_info)
    # is_updated()
    # is_recovered(**defined_user_info)

    pass


def restore_executor(env, user_id):
    """
    :param env:
    :type env: 
    :param user_id: 
    :type user_id: str
    """
    oracle_conn, oracle_curs = '', ''
    if env not in ['cit', 'sit', 'CIT', 'SIT']:
        raise NoSuchEnvironmentException
    if env in ['CIT', 'cit']:
        oracle_conn, oracle_curs = basic_cit
    if env in ['SIT', 'sit']:
        oracle_conn, oracle_curs = basic
    # 确认这个用户是否在相应的环境里已经存在
    is_account_initialized(oracle_curs, str(user_id))



    # restore(oracle_conn, oracle_curs, *restore_sql)

    restore_confirm()

    pass


def restore(SQL, oracle_conn, oracle_curs):
    """

    :param SQL:
    :type SQL:
    :param oracle_conn:
    :type oracle_conn:
    :param oracle_curs:
    :type oracle_curs:
    """
    pass


def restore_confirm(function, *SQL_ORIGINAL):

    """

    :param function:
    :type function:
    :param SQL_ORIGINAL:
    :type SQL_ORIGINAL:
    """
    pass


if __name__ == '__main__':
    dict_test = {'bm_opeartion_ukid': '7973973917', 'jdaljdal': '79839729732'}
    is_already_exists(**dict_test)
    # is_already_exists('kw' = '1332322','mg' = '322323')
    is_satisfied_for_this_role()
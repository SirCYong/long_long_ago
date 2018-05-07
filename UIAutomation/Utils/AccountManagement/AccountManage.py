# coding=utf-8
from .MysqlHelper import MySQL


class AccountManage(object):
    def __init__(self):
        self.mysql = MySQL()
        self.account = None

    def get_account_by_role(self, role):
        """
        通过用户角色获取用户
        :param role: 用户角色
        :return:
        """
        sql_str = "select * from webapp_testaccount t where t.role='{0}'".format(role)
        self.mysql.query(sql_str)
        all_account = self.mysql.fetch_all_rows()
        my_account = None
        for account_one in all_account:
            if account_one[4] == "不在用":
                my_account = account_one
                break
        if not my_account:
            raise Exception("不存在该角色的账号")
        self.account = my_account
        # 设置账号已在用
        sql_str = "update webapp_testaccount set is_use='在用' where id={0}".format(my_account["id"])
        result = self.mysql.update(sql_str)
        if result <= 0:
            raise Exception("获取账号失败")
        return my_account

    def close_mysql(self):
        """
        关闭数据库连接
        :return:
        """
        self.mysql.close()

# coding=utf-8
"""
 对MySQLdb常用函数进行封装的类
 注意：使用这个类的前提是正确安装 MySQL-Python模块。
 官方网站：http://mysql-python.sourceforge.net/
"""

import pymysql
import time

# 数据库连接参数
dbconfig = {'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': 'root',
            'db': 'uiautomationweb',
            'charset': 'utf8'}


class MySQL:
    """
    对MySQLdb常用函数进行封装的类
    """

    error_code = ''  # MySQL错误号码

    _instance = None  # 本类的实例
    _conn = None  # 数据库conn
    _cur = None  # 游标

    _TIMEOUT = 30  # 默认超时30秒
    _timecount = 0

    def __init__(self):
        """
        构造器：根据数据库连接参数，创建MySQL连接
        :param dbconfig:
        """
        try:
            self._conn = pymysql.connect(host=dbconfig['host'],
                                         port=dbconfig['port'],
                                         user=dbconfig['user'],
                                         passwd=dbconfig['passwd'],
                                         db=dbconfig['db'],
                                         charset=dbconfig['charset'])
        except pymysql.Error as e:
            self.error_code = e.args[0]
            error_msg = 'MySQL error! ', e.args[0], e.args[1]
            print(error_msg)

            # 如果没有超过预设超时时间，则再次尝试连接，
            if self._timecount < self._TIMEOUT:
                interval = 5
                self._timecount += interval
                time.sleep(interval)
                self.__init__()
            else:
                raise Exception(error_msg)

        self._cur = self._conn.cursor()
        self._instance = pymysql

    def query(self, sql):
        """
        执行 SELECT 语句
        :param sql:
        :return:
        """
        try:
            self._cur.execute("SET NAMES utf8")
            result = self._cur.execute(sql)
        except pymysql.Error as e:
            self.error_code = e.args[0]
            print("数据库错误代码:", e.args[0], e.args[1])
            result = False
        return result

    def update(self, sql):
        """
        执行 UPDATE 及 DELETE 语句
        :param sql:
        :return:
        """
        try:
            self._cur.execute("SET NAMES utf8")
            result = self._cur.execute(sql)
            self._conn.commit()
        except pymysql.Error as e:
            self.error_code = e.args[0]
            print("数据库错误代码:", e.args[0], e.args[1])
            result = False
        return result

    def insert(self, sql):
        """
        执行 INSERT 语句。如主键为自增长int，则返回新生成的ID
        :param sql:
        :return:
        """
        try:
            self._cur.execute("SET NAMES utf8")
            self._cur.execute(sql)
            self._conn.commit()
            return self._conn.insert_id()
        except pymysql.Error as e:
            self.error_code = e.args[0]
            return False

    def fetch_all_rows(self):
        """
        返回结果列表
        :return:
        """
        return self._cur.fetchall()

    def fetch_one_row(self):
        """
        返回一行结果，然后游标指向下一行。到达最后一行以后，返回None
        :return:
        """
        return self._cur.fetchone()

    def get_row_count(self):
        """
        获取结果行数
        :return:
        """
        return self._cur.rowcount

    def commit(self):
        """
        数据库commit操作
        :return:
        """
        self._conn.commit()

    def rollback(self):
        """
        数据库回滚操作
        :return:
        """
        self._conn.rollback()

    def __del__(self):
        """
        释放资源（系统GC自动调用）
        :return:
        """
        try:
            self._cur.close()
            self._conn.close()
        except:
            pass

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        self.__del__()


if __name__ == '__main__':
    """
    示例
    """
    # 连接数据库，创建这个类的实例
    db = MySQL()

    # 操作数据库
    sql = "SELECT * FROM webapp_testaccount"
    db.query(sql)

    # 获取结果列表
    result = db.fetch_all_rows()

    # 相当于php里面的var_dump
    print(result)

    # 对行进行循环
    for row in result:
        # 使用下标进行取值
        print(row[0])

        # 对列进行循环
        for colum in row:
            print(colum)

    sql = "update webapp_testaccount set is_use='不在用'"
    result = db.update(sql)


    # 关闭数据库
    db.close()
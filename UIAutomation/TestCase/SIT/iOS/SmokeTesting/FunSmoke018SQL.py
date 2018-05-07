# -*- coding: utf-8 -*-

from UIAutomation.Utils import close_oracle, Independent_cit

'''
__author__ = 'ytz'
Description: 注册供应商SQL
'''


def Restore_RegisterSupplier_SQL():
    try:
        con, curs = Independent_cit()
        sql1 = [''' delete from  XDW_APP.ts_registered_supplier t where businesss_name='CISCOSystem' ''']
        curs.execute(sql1)
        con.commit()
        sql2 = ['''select count(*) from  XDW_APP.ts_registered_supplier t where businesss_name= 'CISCOSystem%s' ''']
        result = curs.fetchall()
        curs.execute(sql2)
        if result[0] == 1:
            assert True
            print('删除数据失败')
        con.commit()
        close_oracle(con, curs)
        print('此供应商已删除')
    except Exception as e:
        print(e)

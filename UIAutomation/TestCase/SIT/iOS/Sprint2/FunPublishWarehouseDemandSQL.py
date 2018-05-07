from UIAutomation.Utils import Independent_cit


def PublishWarehouseDemandSQl():
    try:
        con, curs = Independent_cit()
        # 发布仓储需求SQL
        sql = ['''delete FROM xdw_app.DD_CONTRACT
WHERE create_user_id =10001473''',
               '''delete FROM xdw_app.DD_CONTRACT_ITEM
  WHERE create_user_id = 10001473''']
        for sql1 in sql:
            curs.execute(sql1)
            con.commit()
        # result = curs.fetchall()
        con.close()
    except Exception as e:
        print(e)
        print("CIT 数据库数据恢复")
    pass






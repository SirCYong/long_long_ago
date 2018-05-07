from UIAutomation.Utils import close_oracle, basic_cit, basic_sit
__author__ = 'chenyanxiu'


# 还原运输契约
def delete_unit_convert(user_id, unit_name, item_ukid='51845300000005028'):
    con, curs = basic_cit()
    # con, curs = basic_sit()
    try:
        creator_ukid = get_creator_ukid(user_id)
        sql2 = ['''delete from xdw_app.BA_UNIT_CUSTOM buc where buc.unit_name='%s'and buc.creator_ukid='%s'and
                   buc.unit_status='10' ''' % (unit_name, creator_ukid),
                '''delete from xdw_app.IM_TRANSFORM_UNIT iu where iu.im_transform_unit_ukid in(select
                   itud.im_transform_unit_ukid from xdw_app.IM_TRANSFORM_UNIT_DETAIL itud where
                   itud.item_ukid='%s')and iu.transform_status=10 ''' % item_ukid,
                '''delete from xdw_app.IM_TRANSFORM_UNIT_DETAIL itud where itud.item_ukid='%s' ''' % item_ukid]
        for sql in sql2:
            curs.execute(sql)
            con.commit()
            print(sql)
        close_oracle(con, curs)
        print('删除单位和转换关系成功')
    except Exception as e:
        print('删除单位和转换关系失败')
        print(e)
        close_oracle(con, curs)


# 获取创造者id
def get_creator_ukid(user_id):
    con, curs = basic_cit()
    # con, curs = basic_sit()
    try:
        sql1 = '''select count(*) from xdw_app.au_role where role_type = 1 and participant_ukid='%s' ''' \
               % user_id
        curs.execute(sql1)
        result = curs.fetchall()
        if result[0][0] >= 1:
            return user_id
        else:
            sql2 = '''select creator_ukid from xdw_app.hm_creator_relation where participant_ukid='%s' ''' \
                   % user_id
            curs.execute(sql2)
            result2 = curs.fetchall()
            return result2[0][0]
    except Exception as e:
        print('获取创造者信息失败')
        print(e)
        close_oracle(con, curs)

print(delete_unit_convert(10001502, '15箱'))

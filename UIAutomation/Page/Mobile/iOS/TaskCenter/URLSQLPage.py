# -*- coding: utf-8 -*-
"""
订单状态 为200（已转为订单）
    商品铺货：
    创建订单、等待买家付款、等待卖家发货
    商品无需发货：
    创建订单、等待买家付款、等待卖家发货、交易完成

契约状态 草稿（10）
    商品铺货：
    创建订单、等待买家付款
    商品有一个无需发货的商品：
    创建订单
契约内容 草稿（10）
    商品铺货：
    创建订单、等待买家付款
    只要铺货、且发货，契约内容就是对应契约的状态
    商品铺货
"""
from nose.tools import assert_equal

from UIAutomation.Utils import cit, close_oracle, sit


def create_and_buyer_order_two_commodity():    # 创建订单、买家待付款
    dic = {'3': '200', '2': '200', '1': '10', '0': '10'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''',
           '''select t.contract_status from xdw_app.dd_contract t where t.contract_id = '2313605630412700' ''',
           '''select item_status  from xdw_app.dd_contract_item t where t.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1


def seller_order_two_commodity():     # 卖家待发货
    dic = {'3': '200', '2': '200', '1': '20', '0': '20'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''',
           '''select t.contract_status from xdw_app.dd_contract t where t.contract_id = '2313605630412700' ''',
           '''select item_status  from xdw_app.dd_contract_item t where t.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1
        pass


def finish_order_two_commodity():     # 交易完成
    dic = {'3': '200', '2': '200', '1': '30', '0': '30'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''',
           '''select t.contract_status from xdw_app.dd_contract t where t.contract_id = '2313605630412700' ''',
           '''select item_status  from xdw_app.dd_contract_item t where t.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1


def close_order():  # 关闭订单 所有的关闭都是不生成契约
    dic = {'1': '400', '0': '400'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1
        pass


# "商品有一个未铺货"


def create_and_buyer_order_one_commodity():    # 创建订单、买家待付款
    dic = {'1': '130', '0': '100'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1


def buyer_order_one_commodity():     # 卖家待发货
    dic = {'1': '130', '0': '100'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1
        pass


def finish_order_one_commodity():     # 交易完成
    dic = {'1': '130', '0': '100'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1


def close_order_one_commodity():  # 关闭订单 所有的关闭都是不生成契约
    dic = {'1': '400', '0': '400'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1
        pass

# 商品未铺货


def order_none_commodity():    # 创建订单、买家待付款、等待卖家发货、交易完成
    dic = {'1': '130', '0': '130'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1


def close_order_none_commodity():  # 关闭订单 所有的关闭都是不生成契约
    dic = {'1': '400', '0': '400'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1
        pass

# 商品有一个无需发货


def create_and_buyer_order_one_deliver():    # 创建订单、买家待付款
    dic = {'3': '200', '2': '400', '1': '10', '0': '10'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''',
           '''select t.contract_status from xdw_app.dd_contract t where t.contract_id = '2313605630412700' ''',
           '''select item_status  from xdw_app.dd_contract_item t where t.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1


def buyer_order_one_deliver():     # 卖家待发货
    dic = {'3': '200', '2': '400', '1': '20', '0': '20'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''',
           '''select t.contract_status from xdw_app.dd_contract t where t.contract_id = '2313605630412700' ''',
           '''select item_status  from xdw_app.dd_contract_item t where t.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1
        pass


def finish_order_one_deliver():     # 交易完成
    dic = {'3': '200', '2': '400', '1': '30', '0': '30'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''',
           '''select t.contract_status from xdw_app.dd_contract t where t.contract_id = '2313605630412700' ''',
           '''select item_status  from xdw_app.dd_contract_item t where t.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1


def close_order_one_deliver():  # 关闭订单 所有的关闭都是不生成契约
    dic = {'1': '400', '0': '400'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1
        pass

# 无需发货


def order_none_deliver():  # 全部状态
    dic = {'1': '400', '0': '400'}
    con, curs = cit()
    sql = ['''select t.origin_trade_status from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''select t.origin_order_status from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700' )''']
    a = len(sql) - 1
    for sql1 in sql:
        curs.execute(sql1)
        status = curs.fetchone()
        assert_equal(int(status[0]), int(dic[str(a)]))
        a -= 1
        pass


def order_contract_content():    # 契约内容
    try:
        con, curs = cit()
        sql = '''select item_status  from xdw_app.dd_contract_item t where t.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')'''
        curs.execute(sql)
        con.commit()
        status = curs.fetchone()
        print (status[0])
        assert status[0] == 10
        close_oracle(con, curs)
    except Exception as e:
        print ('ERROR：创建契约内容不为10\n')
        print (e)


def delete_all():  # 恢复数据
    con, curs = cit()
    sql = ['''delete from xdw_app.se_taobao_item t where t.trade_ukid =
(select trade_ukid from xdw_app.se_taobao_trade where se_taobao_trade.order_id = '2313605630412700')''',
           '''delete from xdw_app.se_taobao_trade t where t.order_id = '2313605630412700' ''',
           '''delete from xdw_app.cm_address where cm_address.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')''',
           '''delete from xdw_app.dd_obligation where dd_obligation.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')''',
           '''delete from xdw_app.dd_unit_price where dd_unit_price.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')''',
           '''delete from xdw_app.dd_fee_amount where dd_fee_amount.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')''',
           '''delete from xdw_app.dd_fee_add_item where dd_fee_add_item.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')''',
           '''delete from xdw_app.dd_contract_item where dd_contract_item.contract_ukid =
(select t.contract_ukid from xdw_app.dd_contract t where t.contract_id = '2313605630412700')''',
           '''delete from xdw_app.dd_contract t where t.contract_id = '2313605630412700' ''']
    for sql1 in sql:
        curs.execute(sql1)
        con.commit()
    close_oracle(con, curs)
    pass


def all_commodity(admin=None):    # 商品全铺货
    con, curs = cit()
    sql = ['''delete from xdw_app.im_platform_item t where t.sku_num_id in (3103351104677,3103351104877)''',
           '''insert into xdw_app.im_platform_item (PLATFORM_ITEM_UKID, PLATFORM_ID, SHOP_ID, OWNER_ID, IDENTIFY_CODE,
              IDENTIFY_UKID, ITEM_STATUS, PRODUCT_NUM_ID, PRODUCT_OUTER_ID, SKU_NUM_ID, SKU_OUTER_ID, PRODUCT_TITLE, SKU_NAME,
              SELL_PRICE, PLATFORM_IMG_URL, BRAND_NAME, CATEGORY, CREATE_TIME, CREATE_USER_ID, UPDATE_TIME, UPDATE_USER_ID,
              ITEM_COUNT)values ('51768000000008002', '10', '251627', '251627', '34143554352kz7206002110', '51768800000008007',
              '90', '1489161932', '34143554352', '3103351104677', 'kz7206002110',
              '宝宝蝴蝶结打底裙裤 2016秋季女童童装 儿童长裤打底裤女 kz-7206', null, '0',
              'http://img03.taobao.net/bao/uploaded/i3/T1HXdXXgPSt0JxZ2.8_070458.jpg', null, null,
              to_date('03-11-2016 20:10:05', 'dd-mm-yyyy hh24:mi:ss'), '199284',
              to_date('03-11-2016 20:10:05', 'dd-mm-yyyy hh24:mi:ss'), null, '8888')''',
           '''insert into xdw_app.im_platform_item (PLATFORM_ITEM_UKID, PLATFORM_ID, SHOP_ID, OWNER_ID, IDENTIFY_CODE,
              IDENTIFY_UKID, ITEM_STATUS, PRODUCT_NUM_ID, PRODUCT_OUTER_ID, SKU_NUM_ID, SKU_OUTER_ID, PRODUCT_TITLE, SKU_NAME,
              SELL_PRICE, PLATFORM_IMG_URL, BRAND_NAME, CATEGORY, CREATE_TIME, CREATE_USER_ID, UPDATE_TIME, UPDATE_USER_ID,
              ITEM_COUNT)values ('51768200000009001', '10', '251627', '251627', '34143000001kz7206002111', '51768900000008006', '90',
              '8888800001', '34143000001', '3103351104877', 'kz7206002111', '宝宝尿不湿 儿童长裤打底裤女 kz-7206', null, '0',
              'http://taobao.net/bao/uploaded/i0.jpg', null, null, to_date('03-11-2016 20:10:05', 'dd-mm-yyyy hh24:mi:ss'), '199284',
              to_date('03-11-2016 20:10:06', 'dd-mm-yyyy hh24:mi:ss'), null, '9999')
              ''']
    for sql1 in sql:
        curs.execute(sql1)
        con.commit()
    close_oracle(con, curs)
    print ("商品全部铺货"+'%s'+"test\n" % admin)
    pass


def commodity_one_one():  # 商品一个铺货一个未铺货
    con, curs = cit()
    sql = ['''delete from xdw_app.im_platform_item t where t.sku_num_id in (3103351104677,3103351104877)''',
           '''insert into xdw_app.im_platform_item (PLATFORM_ITEM_UKID, PLATFORM_ID, SHOP_ID, OWNER_ID, IDENTIFY_CODE,
IDENTIFY_UKID, ITEM_STATUS, PRODUCT_NUM_ID, PRODUCT_OUTER_ID, SKU_NUM_ID, SKU_OUTER_ID, PRODUCT_TITLE, SKU_NAME,
SELL_PRICE, PLATFORM_IMG_URL, BRAND_NAME, CATEGORY, CREATE_TIME, CREATE_USER_ID, UPDATE_TIME, UPDATE_USER_ID,
ITEM_COUNT)values ('51768000000008002', '10', '251627', '251627', '34143554352kz7206002110', '51768800000008007',
'90', '1489161932', '34143554352', '3103351104677', 'kz7206002110',
'宝宝蝴蝶结打底裙裤 2016秋季女童童装 儿童长裤打底裤女 kz-7206', null, '0',
'http://img03.taobao.net/bao/uploaded/i3/T1HXdXXgPSt0JxZ2.8_070458.jpg', null, null,
to_date('03-11-2016 20:10:05', 'dd-mm-yyyy hh24:mi:ss'), '199284',
to_date('03-11-2016 20:10:05', 'dd-mm-yyyy hh24:mi:ss'), null, '8888')''']
    for sql1 in sql:
        curs.execute(sql1)
        con.commit()
    close_oracle(con, curs)
    pass


def commodity_none():   # 商品都未铺货
    con, curs = cit()
    sql = ['''delete from xdw_app.im_platform_item t where t.sku_num_id in (3103351104677,3103351104877)''']
    curs.execute(sql)
    con.commit()
    close_oracle(con, curs)
    pass


def two_commodity_not_deliver():    # 俩商品无需发货
    con, curs = cit()
    sql = ['''delete from xdw_app.im_platform_item t where t.sku_num_id in (3103351104677,3103351104877)''',
           '''insert into xdw_app.im_platform_item (PLATFORM_ITEM_UKID, PLATFORM_ID, SHOP_ID, OWNER_ID, IDENTIFY_CODE,
IDENTIFY_UKID, ITEM_STATUS, PRODUCT_NUM_ID, PRODUCT_OUTER_ID, SKU_NUM_ID, SKU_OUTER_ID, PRODUCT_TITLE, SKU_NAME,
SELL_PRICE, PLATFORM_IMG_URL, BRAND_NAME, CATEGORY, CREATE_TIME, CREATE_USER_ID, UPDATE_TIME, UPDATE_USER_ID,
ITEM_COUNT)values ('51768000000008002', '10', '251627', '251627', '34143554352kz7206002110', '51768800000008007',
'30', '1489161932', '34143554352', '3103351104677', 'kz7206002110',
'宝宝蝴蝶结打底裙裤 2016秋季女童童装 儿童长裤打底裤女 kz-7206', null, '0',
'http://img03.taobao.net/bao/uploaded/i3/T1HXdXXgPSt0JxZ2.8_070458.jpg', null, null,
to_date('03-11-2016 20:10:05', 'dd-mm-yyyy hh24:mi:ss'), '199284',
to_date('03-11-2016 20:10:05', 'dd-mm-yyyy hh24:mi:ss'), null, '8888')''',
           '''insert into xdw_app.im_platform_item (PLATFORM_ITEM_UKID, PLATFORM_ID, SHOP_ID, OWNER_ID, IDENTIFY_CODE,
IDENTIFY_UKID, ITEM_STATUS, PRODUCT_NUM_ID, PRODUCT_OUTER_ID, SKU_NUM_ID, SKU_OUTER_ID, PRODUCT_TITLE, SKU_NAME,
SELL_PRICE, PLATFORM_IMG_URL, BRAND_NAME, CATEGORY, CREATE_TIME, CREATE_USER_ID, UPDATE_TIME, UPDATE_USER_ID,
ITEM_COUNT)values ('51768200000009001', '10', '251627', '251627', '34143000001kz7206002111', '51768900000008006', '30',
'8888800001', '34143000001', '3103351104877', 'kz7206002111', '宝宝尿不湿 儿童长裤打底裤女 kz-7206', null, '0',
'http://taobao.net/bao/uploaded/i0.jpg', null, null, to_date('03-11-2016 20:10:05', 'dd-mm-yyyy hh24:mi:ss'), '199284',
to_date('03-11-2016 20:10:06', 'dd-mm-yyyy hh24:mi:ss'), null, '9999')
''']
    for sql1 in sql:
        curs.execute(sql1)
        con.commit()
    close_oracle(con, curs)
    pass


def one_commodity_not_deliver():
    con, curs = sit()
    sql = ['''delete from xdw_app.im_platform_item t where t.sku_num_id in (3103351104677,3103351104877)''',
           '''insert into xdw_app.im_platform_item (PLATFORM_ITEM_UKID, PLATFORM_ID, SHOP_ID, OWNER_ID, IDENTIFY_CODE,
IDENTIFY_UKID, ITEM_STATUS, PRODUCT_NUM_ID, PRODUCT_OUTER_ID, SKU_NUM_ID, SKU_OUTER_ID, PRODUCT_TITLE, SKU_NAME,
SELL_PRICE, PLATFORM_IMG_URL, BRAND_NAME, CATEGORY, CREATE_TIME, CREATE_USER_ID, UPDATE_TIME, UPDATE_USER_ID,
ITEM_COUNT)values ('51768000000008002', '10', '251627', '251627', '34143554352kz7206002110', '51768800000008007',
'30', '1489161932', '34143554352', '3103351104677', 'kz7206002110',
'宝宝蝴蝶结打底裙裤 2016秋季女童童装 儿童长裤打底裤女 kz-7206', null, '0',
'http://img03.taobao.net/bao/uploaded/i3/T1HXdXXgPSt0JxZ2.8_070458.jpg', null, null,
to_date('03-11-2016 20:10:05', 'dd-mm-yyyy hh24:mi:ss'), '199284',
to_date('03-11-2016 20:10:05', 'dd-mm-yyyy hh24:mi:ss'), null, '8888')''',
           '''insert into xdw_app.im_platform_item (PLATFORM_ITEM_UKID, PLATFORM_ID, SHOP_ID, OWNER_ID, IDENTIFY_CODE,
IDENTIFY_UKID, ITEM_STATUS, PRODUCT_NUM_ID, PRODUCT_OUTER_ID, SKU_NUM_ID, SKU_OUTER_ID, PRODUCT_TITLE, SKU_NAME,
SELL_PRICE, PLATFORM_IMG_URL, BRAND_NAME, CATEGORY, CREATE_TIME, CREATE_USER_ID, UPDATE_TIME, UPDATE_USER_ID,
ITEM_COUNT)values ('51768200000009001', '10', '251627', '251627', '34143000001kz7206002111', '51768900000008006', '90',
'8888800001', '34143000001', '3103351104877', 'kz7206002111', '宝宝尿不湿 儿童长裤打底裤女 kz-7206', null, '0',
'http://taobao.net/bao/uploaded/i0.jpg', null, null, to_date('03-11-2016 20:10:05', 'dd-mm-yyyy hh24:mi:ss'), '199284',
to_date('03-11-2016 20:10:06', 'dd-mm-yyyy hh24:mi:ss'), null, '9999')
''']
    for sql1 in sql:
        curs.execute(sql1)
        con.commit()
    close_oracle(con, curs)
    pass


def activation_depot_status(admin=None):
    con, curs = sit()
    sql = '''select t.client_show from xdw_app.ms_card t where t.owner_bu_id = '%s'and t.card_name = '激活仓库' ''' % admin
    curs.execute(sql)
    status = curs.fetchone()
    print(status[0])
    assert_equal(status[0], 1)
    close_oracle(con, curs)
    pass


def activation_entity_shop_status(admin=None):
    con, curs = sit()
    sql = ['''select t.client_show from xdw_app.ms_card t where t.owner_bu_id = '%s'
    and t.card_name = '激活仓库' ''' % admin]
    curs.execute(sql)
    status = curs.fetchone()
    print (status[0])
    assert_equal(status[0], 1)
    close_oracle(con, curs)
    pass




if __name__ == '__main__':
    get_user_id('18205010265')






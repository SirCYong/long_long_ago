# -*- coding: utf-8 -*-
import requests
from common.common_method.database.ConnetToOracleDatabase import close_oracle, cit


def download_create_order():   # 创建订单
    try:
        requests.get(url="http://192.168.6.31:9180/datasync/api/"
                         "tradepush?tid=2313605630412700&status=TRADE_CREATE&buyer_nick="
                         "%E6%9D%A8%E6%9C%88%E7%90%B41983&seller_nick=%E5%8D%A0%E6%9C%88%E6%98%9F")
        print ('创建订单\n')

    except Exception as e:
        print (e)


def download_buyer_order():  # 下载买家未付款订单
    try:
        requests.get(url="http://192.168.6.31:9180/datasync/api/"
                         "tradepush?tid=2313605630412700&status=WAIT_BUYER_PAY&buyer_nick="
                         "%E6%9D%A8%E6%9C%88%E7%90%B41983&seller_nick=%E5%8D%A0%E6%9C%88%E6%98%9F")
        print ('下载买家订单\n')
    except Exception as e:
        print (e)


def download_seller_order():
    try:
        requests.get(url="http://192.168.6.31:9180/datasync/api/"
                         "tradepush?tid=2313605630412700&status=WAIT_SELLER_SEND_GOODS&buyer_nick="
                         "%E6%9D%A8%E6%9C%88%E7%90%B41983&seller_nick=%E5%8D%A0%E6%9C%88%E6%98%9F")
        print ('下载等待卖家发货\n')
    except Exception as e:
        print (e)


def downloade_close_order():
    try:
        requests.get(url="http://192.168.6.31:9180/datasync/api/"
                         "tradepush?tid=2313605630412700&status=TRADE_CLOSED&buyer_nick="
                         "%E6%9D%A8%E6%9C%88%E7%90%B41983&seller_nick=%E5%8D%A0%E6%9C%88%E6%98%9F")
        print ('下载关闭订单\n')
    except Exception as e:
        print (e)


def update_create_order():
    try:
        requests.get(url="http://192.168.6.31:9180/datasync/api/"
                         "updateTradeStatus?tid=2313605630412700&status=TRADE_CREATE")
        print ('update订单\n')
    except Exception as e:
        print (e)


def update_buyer_order():
    try:
        requests.get(url="http://192.168.6.31:9180/datasync/api/"
                         "updateTradeStatus?tid=2313605630412700&status=WAIT_BUYER_PAY")
        print ('update买家订单\n')
    except Exception as e:
        print (e)


def update_seller_order():
    try:
        requests.get(url="http://192.168.6.31:9180/datasync/api/"
                         "updateTradeStatus?tid=2313605630412700&status=WAIT_SELLER_SEND_GOODS")
        print ('update卖家订单\n')
    except Exception as e:
        print (e)


def update_close_order():
    try:
        requests.get(url="http://192.168.6.31:9180/datasync/api/"
                         "updateTradeStatus?tid=2313605630412700&status=TRADE_CLOSED")
        print ('update关闭订单\n')
    except Exception as e:
        print (e)

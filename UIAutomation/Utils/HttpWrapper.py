import hashlib
from random import Random

import requests
from datetime import datetime

from UIAutomation.Utils import LoginFailException, GlobalSettingErrorException, parse_cfg, get_setting_configuration, \
    sleep

__package__ = "IscsUIAutomation"

def get_request_post_head_parameters(token='', userid='100188'):
    """
     构造http请求需要放在头文件里面的token,sign, v，m，t五个参数
     sign = token+str(2016-09-20 29:39:34)+m+userid 然后去MD5的值，最后转化为大写即为sign值
    :param token: token是来自于用户log后，系统生成的token值.
    :type token: string
    :param userid:
    :type userid: str
    :return:
    :rtype: dict
    """
    v = '1.0.0'
    m = 'test'
    head_parameter = {'v': v, 'm': m}
    current_time = datetime.now().strftime('%Y-%m-%d %I:%M:%S')
    head_parameter['token'] = token
    head_parameter['t'] = current_time
    string_sign = token + str(current_time) + m + userid
    mymd5 = hashlib.md5()
    mymd5.update(string_sign.encode('utf-8'))
    mymd5_digest = mymd5.hexdigest()
    sign = mymd5_digest.upper()
    head_parameter['sign'] = sign
    return head_parameter


def http_login(url_login,  ID, password, url_task=None,values=None):
    # 系统发送post请求
    try:
        login_data = {"userId": ID, "password": password}
        login_response = requests.post(url=url_login, json=login_data)
        token = login_response.json()
        send_headers = get_request_post_head_parameters(str(token['data']['token']))
        response = requests.post(url=url_task, json=values, headers=send_headers)
        # 判断请求是否成功
        assert response.status_code == 200
        return response.status_code

    except Exception as e:
        raise LoginFailException


def eject_logged_user(account, password):
    """
    在测试执行前,调用此方法顶掉已经登录的账号,执行环境参数直接在配置文件里面读取了.
    :param account:
    :type account:
    :param password:
    :type password:
    :return:
    :rtype:
    """
    env = get_setting_configuration('Env', 'scriptrunon')
    if env == 'CIT':
        login_url = 'http://192.168.6.31:8080/base/loginWithAccount'
        bind_user_accout = 'http://192.168.6.32:8080/base/loginWithBind'
    elif env == 'SIT':
        login_url = 'http://192.168.6.32:8080/base/loginWithAccount'
        bind_user_accout = 'http://192.168.6.32:8080/base/loginWithBind'
    else:
        raise GlobalSettingErrorException
    # 随机生成一个设备号,以防设备号相同导致顶掉账号失败
    dev_info = 'ACA92D9A-BFD3-46B9-AF2C-D76064C931F0-%s' % str(Random().randint(1000000000, 9999999999))
    login_parameters = {'platform': 'i', 'verificationCode': '', 'baiduChannelId': '5540137283439283384', 'accountId': account,
                'password': password, 'deviceInfo': dev_info}
    # 发起登录
    login_resp = requests.post(login_url, json=login_parameters)
    # 930036 means 'need bind new device'
    # assert login_resp.status_code == 200 and login_resp.json()['code'] == '930036'
    # 发起绑定
    sleep(2)
    if login_resp.json()['code'] == '0':
        return login_resp.json()['data']['token'], login_resp.json()['data']['user']['userId']
    else:
        token = login_resp.json()['data']['token']
        header_sample = {'Content-type': 'application/json;charset=UTF-8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko Firefox/32.0'}
        token_header = {'token':token}
        header_sample.update(token_header)
        bind_resp = requests.post(bind_user_accout, headers=header_sample)
        sleep(2)
        assert bind_resp.status_code == 200 and bind_resp.json()['code'] == '0'
        return token, bind_resp.json()['data']['user']['userId']


def get_table_list(token, userid):
    """
    可以通过eject_logged_user方法得到token和userid， 返回这个用户在系统中的所有临时卡片的位置排序信息
    :param token: 绑定用户的token
    :type token:
    :param userid: 绑定用户在系统中的userid
    :type userid:
    :return:
    :rtype:
    """
    header_sample = {'Content-type': 'application/json;charset=UTF-8',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko Firefox/32.0'}
    token_header = get_request_post_head_parameters(token, userid)
    header_sample.update(token_header)
    env = get_setting_configuration('Env', 'scriptrunon')
    desktop_url = get_setting_configuration(env, 'desktop_url')
    response = requests.post(url=desktop_url, headers=header_sample)
    result = response.json()['data']['cardTable']
    return result








if __name__ == '__main__':
    # eject_logged_user('15711041212', '123456')
    eject_logged_user('13788883333', '123456')

from UIAutomation.Utils.DriverConf import parse_cfg


def get_setting_configuration(sector, value):
    """
    此方法去读取setting配置文件里面的值,一键切换测试环境, 只要传入settitng里面区块和里面要读取的值
    :param sector: setting里面的大区块
    :type sector:
    :param value:
    :type value: setting里面的具体的值
    :return:
    :rtype:
    """
    val = value.lower()
    cfg = parse_cfg('setting', sector)
    return cfg[val]


def get_env_script_runs_on():
    """
    当DEBUG模式打开的时候,才可以配置是RUN在CIT上还是SIT上
    :return:
    :rtype:
    """
    if get_setting_configuration('Env', 'debug').lower() == 'on':
        return get_setting_configuration('Env', 'scriptrunon')
    else:
        return 'SIT'


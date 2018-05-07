# coding: utf-8
# author: yong_li
import re

from datetime import datetime
import paramiko
import os
from scp import SCPClient
from jira import JIRA
import logging
from common.common_method.Logger import get_logger

# 远端服务上的log_path,也是本地服务上的后半段path
log_base_abs_path = '/webapp/tomcat8_base/logs/'
log_labor_abs_path = '/webapp/tomcat8_labor/logs/'
log_supply_abs_path = '/webapp/tomcat8_supply/logs/'
log_warehouse_abs_path = '/webapp/tomcat8_warehouse/logs/'
log_data_sync_abs_path = '/webapp/tomcat8_datasync/logs/'
log_sales_abs_path = '/webapp/tomcat8_sales/logs/'
log_transportation_abs_path = '/webapp/tomcat8_transportation/logs/'


dev2_ip_address = '192.168.6.25'
cit_ip_address = '192.168.6.31'
sit_ip_address = '192.168.6.61'
username = 'root'
password = 'iscs@2016up'

# Linux Log分析服务器上文件copy后保存地址
local_path = '/home/yongli/tomcat_logs'

# Copy过来的文件放置的文件路径为, 后面会生成.sh的脚本去自动创建这些目录
base_log = '/home/yongli/tomcat_logs/webapp/tomcat8_base/logs/'
warehouse_log = '/home/yongli/tomcat_logs/webapp/tomcat8_warehouse/logs/'
supply_log = '/home/yongli/tomcat_logs/webapp/tomcat8_supply/logs/'
data_sync_log = '/home/yongli/tomcat_logs/webapp/tomcat8_datasync/logs/'
labor_log = '/home/yongli/tomcat_logs/webapp/tomcat8_labor/logs/'
sales_log = '/home/yongli/tomcat_logs/webapp/tomcat8_sales/logs/'
transportation_log = '/home/yongli/tomcat_logs/webapp/tomcat8_transportation/logs/'


# 分析的结果存放的位置为,已经分析过的就不再进行分析,但Catalina.out需要异常处理
base_analysis_result = '/home/yongli/tomcat_logs/webapp/tomcat8_base/analysis_result/'
warehouse_analysis_result = '/home/yongli/tomcat_logs/webapp/tomcat8_warehouse/analysis_result/'
supply_analysis_result = '/home/yongli/tomcat_logs/webapp/tomcat8_supply/analysis_result/'
data_sync_analysis_result = '/home/yongli/tomcat_logs/webapp/tomcat8_datasync/analysis_result/'
labor_analysis_result = '/home/yongli/tomcat_logs/webapp/tomcat8_labor/analysis_result/'
sales_analysis_result = '/home/yongli/tomcat_logs/webapp/tomcat8_sales/analysis_result/'
transportation_analysis_result = '/home/yongli/tomcat_logs/webapp/tomcat8_transportation/analysis_result/'
"""
[root@localhost logs]# mkdir /home/yongli/tomcat_logs/webapp/tomcat8_warehouse/analysis_result/
[root@localhost logs]# mkdir /home/yongli/tomcat_logs/webapp/tomcat8_supply/analysis_result/
[root@localhost logs]# mkdir /home/yongli/tomcat_logs/webapp/tomcat8_datasync/analysis_result/
[root@localhost logs]# mkdir /home/yongli/tomcat_logs/webapp/tomcat8_labor/analysis_result/
[root@localhost logs]# mkdir /home/yongli/tomcat_logs/webapp/tomcat8_sales/analysis_result/
[root@localhost logs]# mkdir /home/yongli/tomcat_logs/webapp/tomcat8_warehouse/analysis_result/
[root@localhost logs]# mkdir /home/yongli/tomcat_logs/webapp/tomcat8_transportation/analysis_result/
"""
# JIRA支持组项目id
project_id_support = '10102'
# JIRA网仓3号项目id
project_id_iscs_NO3 = '10000'

# error code
error_code_catalina_out = 'java.lang.NullPointerException'

# analysis result
analysis_result_path = '/home/yongli/tomcat_logs/'

# catalina.out analysis result
catalina_analysis_result = '/home/yongli/tomcat_logs/catalina/'

# catalina.out reported error save path
catalina_reported_error = '/home/yongli/tomcat_logs/catalina/reported_err.txt'

logger = get_logger('/home/yongli/tomcat_logs/catalina/execute_log.log')


# 这个文件单独处理catlalina.out文件，屏蔽重复上报的问题，并且空指针错误也只存在于catalina.out文件里
def log_handler_catalina_out(env, err_code):
    if re.findall('cit', env, flags=re.IGNORECASE):
        host = cit_ip_address
    elif re.findall('sit', env, flags=re.IGNORECASE):
        host = sit_ip_address
    elif re.findall('dev', env, flags=re.IGNORECASE):
        host = dev2_ip_address
    else:
        logger.err('输入环境名称错误！')
        raise ValueError

    log_paths = [log_base_abs_path, log_data_sync_abs_path, log_labor_abs_path, log_supply_abs_path,
                 log_sales_abs_path, log_transportation_abs_path, log_warehouse_abs_path]
    copied_path = []
    ssh_executor = __ssh_connect_to_server(host)
    # 通过SCP协议下载文件
    scp = SCPClient(ssh_executor.get_transport())
    # 记录那个目录下,需要分析那些Log, 把文件名称作为Key, 文件夹路径作为value，因为key必须唯一
    catalina_out_local_files_abs_path = [base_log, warehouse_log, supply_log, data_sync_log, labor_log, sales_log, transportation_log]
    for path in log_paths:
        copied_path.append(path+'catalina.out')
    for file_to_copy in range(len(log_paths)):
        scp.get('%s' % copied_path[file_to_copy], '%s' % catalina_out_local_files_abs_path[file_to_copy])
    scp.close()

    local_catalina_file_abs_path = []
    for local in catalina_out_local_files_abs_path:
        local_catalina_file_abs_path.append(local+'catalina.out')
    temp_line = []
    line_number_fifty = []
    analysis_result_abs_name = catalina_analysis_result + datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(' ', '-'). \
        replace(':', '-') + '.txt'
    for catalina_file in local_catalina_file_abs_path:
        with open(catalina_file) as f:
            line = f.readline()
            try:
                while True:
                    # 把每一行先装进去
                    if len(temp_line) < 10:
                        temp_line.append(line)
                    else:
                        # 如果行太长，清空再加入新的行
                        temp_line.pop(0)
                        temp_line.append(line)
                    if is_line_contain_errcode(line, err_code):
                        # 把下面的60行写入result,但50行内部就不用判断是否包含error code了
                        for x in range(60):
                            line_number_fifty.append(line)
                            line = f.next()
                        write_into_result(temp_line, analysis_result_abs_name)
                        write_into_result(line_number_fifty, analysis_result_abs_name)
                        write_into_result('*' * 20 + 'sub_result___' + '*' * 20 + '\n', analysis_result_abs_name)
                        line_number_fifty = []
                    line = f.next()
            except StopIteration:
                logger.debug("End of File")

    create_jira_issue_content(analysis_result_abs_name, error_code_catalina_out)


# Copy只copy增量, 目前只支持从LinuxCopy到分析服务器Linux上,还不支持copy到windows上,后面会用SFTP实现从Linux-Windows
def log_handler_copy_others(env):
    if re.findall('cit', env, flags=re.IGNORECASE):
        host = cit_ip_address
    elif re.findall('sit', env, flags=re.IGNORECASE):
        host = sit_ip_address
    elif re.findall('dev', env, flags=re.IGNORECASE):
        host = dev2_ip_address
    else:
        logger.err('输入环境名称错误！')
        raise ValueError

    # 决定要要Copy多少个目录下的log
    log_paths = [log_base_abs_path, log_data_sync_abs_path, log_labor_abs_path, log_supply_abs_path,
                 log_sales_abs_path, log_transportation_abs_path, log_warehouse_abs_path]

    # 得到本地所有文件列表, 后面添加一个空格, 然后转换为set格式去和本地的文件比较，只去下载不同的的文件
    ssh_executor = __ssh_connect_to_server(host)
    # 通过SCP协议下载文件
    scp = SCPClient(ssh_executor.get_transport())
    # 记录那个目录下,需要分析那些Log, 把文件名称作为Key, 文件夹路径作为value，因为key必须唯一
    log_to_analysis = {}

    for path in log_paths:
        logger.debug('当前处理的目录为:')
        logger.debug(local_path + path)
        files = os.listdir(local_path+path)
        logger.debug('当前目录下的所有文件')
        files_need_to_filter = []
        for fi in files:
            # 这个工具暂时不处理catalina.out文件，后面会开发一个新的方法通过记录行数来分析catalina.out文件内部增量的工作分析
            if fi.find('catalina') == 0 and fi.find('catalina.out') == -1:
                files_need_to_filter.append(fi + ' ')  # 添加空格在末尾,否则set.difference会查找不到
        files_need_to_filter_set = set(files_need_to_filter)
        logger.debug('#' * 10)
        logger.debug('当前操作的路径为%s' % path)
        # 拼接命令,得到所有copy目录内的所有文件名,然后找出增量项，再进行scp copy
        ssh_std_in, ssh_stdout, ssh_stderr = ssh_executor.exec_command('cd %s;ls' % path)
        files_under_path = ssh_stdout.readlines()
        files_under_path_ = []
        for f in files_under_path:
            if f.find('catalina') == 0 and f.find('catalina.out') == -1:
                files_under_path_.append(f.replace("\n", ' '))
        files_under_path_set = set(files_under_path_)
        logger.debug('在路径下的所有文件名为：')
        logger.debug(files_under_path)
        files_need_to_copy_in_current_folder = files_under_path_set.difference(files_need_to_filter_set)
        logger.debug('需要copy的文件为')
        logger.debug(files_need_to_copy_in_current_folder)

        for file_to_copy in files_need_to_copy_in_current_folder:
            logger.debug('Scp Get的目标和本地目录分别为：')
            logger.debug('%s%s' % (path, file_to_copy), '%s%s' % (local_path, path))
            # [:-1]拿掉文件名称末尾的空格, 否则SCP-get会执行失败
            scp.get('%s%s' % (path, file_to_copy[:-1]), '%s%s' % (local_path, path))
            log_to_analysis.update({file_to_copy[:-1]: '%s%s' % (local_path, path)})

    ssh_executor.close()
    # 确保后面分析的只是增量的LOG, catalina.out除外
    return log_to_analysis
    pass


# 定义一个固定长度的字段60行,一旦发现有异常就把前面10行以及后面的50行全部copy过来,10和50是可配置的
def log_handler_analysis(files, err_code):
    # 处理文件路径
    if type(files) is dict and len(files) != 0:
        paths = files.values()
        files_name = files.keys()
        tuple_values = zip(paths, files_name)
        log_need_to_analysis_abs_path = []
        # 用来暂存前面的10行
        temp_line = []
        # 后面50行内容
        line_number_fifty = []
        # 结果文件绝对路径和文件名
        analysis_result_abs_name = analysis_result_path + datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(' ', '-').\
            replace(':', '-') + '.txt'
        for item in tuple_values:
            log_need_to_analysis_abs_path.append('%s%s' % (item[0], item[1]))
        # 打开文件，分析错误,
        for log in log_need_to_analysis_abs_path:
            with open(log, 'r') as f:
                line = f.readline()
                try:
                    while True:
                        # 把每一行先装进去
                        if len(temp_line) < 10:
                            temp_line.append(line)
                        else:
                            # 如果行太长，清空再加入新的行
                            temp_line.pop(0)
                            temp_line.append(line)
                        if is_line_contain_errcode(line, err_code):
                            # 把下面的60行写入result,但50行内部就不用判断是否包含error code了
                            for x in range(60):
                                line_number_fifty.append(line)
                                line = f.next()
                            write_into_result(temp_line, analysis_result_abs_name)
                            write_into_result(line_number_fifty, analysis_result_abs_name)
                            write_into_result('*'*20+'sub_result___'+'*'*20 + '\n', analysis_result_abs_name)
                            line_number_fifty = []
                        line = f.next()

                except StopIteration:
                    logger.debug('End of File')
        # 返回给JIRA模块进行操作
        return analysis_result_abs_name
    else:
        logger.debug("需要分析的新的Log为空.")
        raise ValueError
    pass


def get_jira_connection():
    jira = JIRA('http://jira.iscs.com.cn', basic_auth=('zhuangyongli', '8002860'))
    return jira
    pass


# Reported err save path: /home/yongli/
# 打开初次结果分析文件,原始的sub_result文件
def grep_class_error(sub_result_file, existed_error_file):
    sep = 'sub_result___'
    for sub_result in get_sub_result(sub_result_file, sep):
        sub_result_list = sub_result.split('\n')
        # 整个大的字符串里面发现有ERROR才去摘取error class
        if sub_result.find(' ERROR ') != -1:
            for line in sub_result_list:
                if str(line).find(' ERROR ') != -1:
                    err_d = get_error_detail(str(line)+'\n')
                    # 如果的到的错误是新的,则上报
                    if is_error_exists(existed_error_file, err_d) is not True:
                        write_into_result(err_d, existed_error_file)
                        # 这里report to JIRA

                    # write_into_result(get_error_detail(str(line)+'\n'), 'D://temp//existed_error.txt')
    pass


# 剔除文件内的重复项, 利用Set的属性剔除重复项, 重新写入没有重复项的文件， 这只是工具,第一次的时候使用一下,后面就不需要了.
def remove_duplicator(existed_error_file, file_without_duplicator):
    set_line = set()
    with open(existed_error_file, 'r') as f:
        try:
            while True:
                set_line.add(next(f))
        except StopIteration:
            logger.debug('End of File.')

    with open(file_without_duplicator, 'a') as f:
        for x in list(set_line):
            f.writelines(str(x))


def is_error_exists(reported_err_file, err):
    if str(err).__contains__('\n') is not True:
        err = str(err)+'\n'
    err_set = {str(err)}
    all_err_set = set()

    with open(reported_err_file, 'r') as f:
        line = f.readline()
        try:
            while True:
                all_err_set.add(line)
                line = f.next()
        except StopIteration:
            print("End of File")
    logger.debug('结果是%s' % err_set.issubset(all_err_set))
    return err_set.issubset(all_err_set)


def get_error_detail(line_with_error):
    line_with_error_list = list(line_with_error)
    list_message = []
    for sy in range(len(line_with_error)):
        if sy > line_with_error.find(' ERROR ') + 6 and line_with_error[sy] != ' ':
            list_message.append(line_with_error_list[sy])
        else:
            continue
    temp_str = ''
    list_message_str = temp_str.join(list_message)
    return list_message_str


# 创造有个生成器,打开文件，每到有个sub_result___就出来一次处理一下
def get_sub_result(file_name,sub_result_msg):
    message = ''
    with open(file_name, 'r') as f:
        line = f.readline()
        try:
            while True:
                if is_line_contain_errcode(line, sub_result_msg) is not True:
                    message += line
                else:
                    yield message
                    message = ''
                line = f.next()
        except StopIteration:
            logger.debug('End of File')
            pass


# 创造有个生成器,打开文件，每到有个sub_result___就出来一次处理一下
def get_subset(file_name, end_msg):
    message = ''
    with open(file_name, 'r') as f:
        try:
            while True:
                if is_line_contain_errcode(next(f), end_msg) is not True:
                    message += next(f)
                else:
                    yield
                    message = ''
        except StopIteration:
            logger.debug('End of File')


# 传入结果分析文件
def create_jira_issue_content(issue_description, err_code):
    issue_desc_sample = {
            "project": {
            "id": "10102"
            },
            "summary": "[自动工具上报]系统后台%s错误." % err_code,
            "description": """ """,
            "issuetype": {
            "id": "10005"
            },
            "customfield_10100": {
            "value": "CIT测试环境"
            },
            "customfield_10300": {
                "value": "严重"
            }
            }
    single_issue_description_content = ''
    with open(issue_description, 'r') as f:
        line = f.readline()
        try:
            while True:
                # 不能用列表,列表的话不会实现换行
                single_issue_description_content += line
                if is_line_contain_errcode(line, "sub_result___"):
                    issue_desc_sample['description'] = "========后台LOG详情为:=========\n %s" %\
                                                       single_issue_description_content
                    issue_desc_sample['summary'] = "[自动工具上报]系统后台%s错误@%s." % (err_code, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    report_to_jira(issue_desc_sample)
                    single_issue_description_content = ''
                line = f.next()
        except StopIteration:
            logger.debug("End of file")
    pass


def report_to_jira(issue_content):
    jira_connect = get_jira_connection()
    jira_connect.create_issue(fields=issue_content)
    pass


def __ssh_connect_to_server(host):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, 22, username, password, timeout=5)
    except Exception:
        logger.error('SSH 连接失败！')
        raise IOError
    return ssh
    pass


# err_code 分别考虑元祖和字符串类型,假如元祖内只有一个值的话，需要转化为STR类型在处理
def is_line_contain_errcode(line, err_code):
    if type(err_code) is str:
        if re.findall(err_code, line, re.IGNORECASE):
            return True
        else:
            return False
    elif type(err_code) is tuple:
        result = False
        for err in err_code:
            if re.findall(err, line, re.IGNORECASE):
                result = True
        return result
    else:
        raise ValueError
    pass


# 写入模式必须为a，重复写入,如果没有这个文件则创新一个新的
def write_into_result(line, analysis_result_file_name):
    with open(analysis_result_file_name, 'a')as f:
        f.writelines(line)
    pass


def log_recorder():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S', filename=catalina_analysis_result+'recorder.log', filemode='w')
    logging.debug('debug message')
    logging.info('info message')
    logging.warn('error message')
    logging.error('error message')
    logging.critical('critical message')
    return logging.getLogger()
    pass


if __name__ == '__main__':
    # log_handler_copy('dev')
    logger.debug(analysis_result_path + datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(' ', '-'))







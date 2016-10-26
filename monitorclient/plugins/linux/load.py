#!/usr/bin/env python
#coding:utf-8


# import commands
import subprocess


def monitor():
    shell_command = 'uptime'

    try:
        result = subprocess.check_output(shell_command,shell=True).decode()
        value_dic = {}
        uptime = result.split(',')[:1][0]
        load1,load5,load15 = result.split('load average:')[1].split(',')
        value_dic= {
            #'uptime': uptime,
            'load1': load1,
            'load5': load5,
            'load15': load15,
            'status': 0
        }
    except Exception as e:
        status = e.__str__().split(" ")[-1:]
        value_dic = {'status':status}

    return value_dic


    # status,result = commands.getstatusoutput(shell_command)
    # if status != 0: #cmd exec error
    #     value_dic = {'status':status}
    # else:
    #     value_dic = {}
    #     uptime = result.split(',')[:1][0]
    #     load1,load5,load15 = result.split('load average:')[1].split(',')
    #     value_dic= {
    #         #'uptime': uptime,
    #         'load1': load1,
    #         'load5': load5,
    #         'load15': load15,
    #         'status': status
    #     }
    # return value_dic

#!/usr/bin/env python
#coding:utf-8

# import commands
import subprocess


def monitor(frist_invoke=1):
    monitor_dic = {
        'SwapUsage': 'percentage',
        'MemUsage'  : 'percentage',
    }
    shell_command ="grep 'MemTotal\|MemFree\|Buffers\|^Cached\|SwapTotal\|SwapFree' /proc/meminfo"
    try:
        result = subprocess.check_output(shell_command, shell=True).decode()
        value_dic = {'status': 0}
        tem_list = []
        for i in result.split('kB\n'):
            tem_list.append(i)
        keys = []
        values = []
        for i in tem_list:
            if i:
                # print(type(i),i)
                key = i.split(":")[0]  # factor name
                value = i.split(":")[1].strip()  # factor name
                keys.append(key)
                values.append(value)
        for (k,v) in zip(keys,values):
            value_dic[k] = v

        if monitor_dic['SwapUsage'] == 'percentage':
            value_dic['SwapUsage_p'] = str(100 - int(value_dic['SwapFree']) * 100 / int(value_dic['SwapTotal']))

        # real SwapUsage value
        value_dic['SwapUsage'] = int(value_dic['SwapTotal']) - int(value_dic['SwapFree'])

        MemUsage = int(value_dic['MemTotal']) - (int(value_dic['MemFree']) + int(value_dic['Buffers']) + int(value_dic['Cached']))

        if monitor_dic['MemUsage'] == 'percentage':
            value_dic['MemUsage_p'] = str(int(MemUsage) * 100 / int(value_dic['MemTotal']))

        # real MemUsage value
        value_dic['MemUsage'] = MemUsage
        # return value_dic
    except Exception as e:
        value_dic = {'status': 1}

    return value_dic

    # status, result = commands.getstatusoutput(shell_command)
    # if status != 0:  # cmd exec error
    #     value_dic = {'status': status}
    # else:
    #     value_dic = {'status': status}
    #     for i in result.split('kB\n'):
    #         key = i.split()[0].strip(':')  # factor name
    #         value = i.split()[1]  # factor value
    #         value_dic[key] = value
    #
    #     if monitor_dic['SwapUsage'] == 'percentage':
    #         value_dic['SwapUsage_p'] = str(100 - int(value_dic['SwapFree']) * 100 / int(value_dic['SwapTotal']))
    #     # real SwapUsage value
    #     value_dic['SwapUsage'] = int(value_dic['SwapTotal']) - int(value_dic['SwapFree'])
    #
    #     MemUsage = int(value_dic['MemTotal']) - (
    #     int(value_dic['MemFree']) + int(value_dic['Buffers']) + int(value_dic['Cached']))
    #     if monitor_dic['MemUsage'] == 'percentage':
    #         value_dic['MemUsage_p'] = str(int(MemUsage) * 100 / int(value_dic['MemTotal']))
    #     # real MemUsage value
    #     value_dic['MemUsage'] = MemUsage
    # return value_dic


if __name__ == '__main__':
    a = monitor()
    print(a)
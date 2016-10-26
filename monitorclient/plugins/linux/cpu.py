#!/usr/bin/env python
#coding:utf-8

#import commands
import subprocess

#apt-get install sysstat
def monitor(frist_invoke=1):
    shell_command = 'sar 1 3| grep "^Average:"'
    try:
        result = subprocess.check_output(shell_command, shell=True).decode()
        value_dic = {}
        user, nice, system, iowait, steal, idle = result.split()[2:]
        value_dic = {
            'user': user,
            'nice': nice,
            'system': system,
            'iowait': iowait,
            'steal': steal,
            'idle': idle,
            'status': 0
        }
    except Exception as e:
        status = e.__str__().split(" ")[-1:]
        value_dic = {'status': status}

    return value_dic

    # status, result = commands.getstatusoutput(shell_command)
    # # result = subprocess.Popen(shell_command,shell=True,stdout=subprocess.PIPE).stdout.read()
    # if status != 0:
    #     value_dic = {'status': status}
    # else:
    #     value_dic = {}
    #     user, nice, system, iowait, steal, idle = result.split()[2:]
    #     value_dic = {
    #         'user': user,
    #         'nice': nice,
    #         'system': system,
    #         'iowait': iowait,
    #         'steal': steal,
    #         'idle': idle,
    #         'status': status
    #     }
    # return value_dic

if __name__ == '__main__':
    a = monitor()
    print(a)
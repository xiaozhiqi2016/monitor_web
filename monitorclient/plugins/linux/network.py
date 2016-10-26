#_*_coding:utf-8_*_

import subprocess

def monitor(frist_invoke=1):
    shell_command = 'sar -n DEV 1 1 |grep -v IFACE |grep Average'
    result = subprocess.Popen(shell_command,shell=True,stdout=subprocess.PIPE).stdout.readlines()
    # result = subprocess.check_output(shell_command,shell=True).decode()
    # print(type(result),result)
    value_dic = {'status':0, 'data':{}}
    for line in result:
        line = line.decode().split()
        nic_name,t_in,t_out = line[1],line[4],line[5]
        value_dic['data'][nic_name] = {"t_in":line[4], "t_out":line[5]}
    #print(value_dic)
    return value_dic

if __name__ == '__main__':
    a = monitor()
    print(a)
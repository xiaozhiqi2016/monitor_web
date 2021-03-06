#_*_coding:utf-8_*_
from plugins.linux import sysinfo,load,cpu_mac,cpu,memory,network,host_alive


def LinuxSysInfo():
    #print __file__
    return  sysinfo.collect()


def WindowsSysInfo():
    from windows import sysinfo as win_sysinfo
    return win_sysinfo.collect()

def GetMacCPU():
    #return cpu.monitor()
    return cpu_mac.monitor()


def GetLinuxCpuStatus():
    return cpu.monitor()


def GetLinuxMemStatus():
    return memory.monitor()


def GetLinuxNetworkStatus():
    return network.monitor()

def host_alive_check():
    return host_alive.monitor()

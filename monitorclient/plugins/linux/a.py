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
        for i in result.split('kB\n'):
            key = i.split()[0].strip(':')  # factor name
            value = i.split()[1]  # factor value
            value_dic[key] = value
            print(value_dic)

        if monitor_dic['SwapUsage'] == 'percentage':
            value_dic['SwapUsage_p'] = str(100 - int(value_dic['SwapFree']) * 100 / int(value_dic['SwapTotal']))

        # real SwapUsage value
        value_dic['SwapUsage'] = int(value_dic['SwapTotal']) - int(value_dic['SwapFree'])

        MemUsage = int(value_dic['MemTotal']) - (int(value_dic['MemFree']) + int(value_dic['Buffers']) + int(value_dic['Cached']))

        if monitor_dic['MemUsage'] == 'percentage':
            value_dic['MemUsage_p'] = str(int(MemUsage) * 100 / int(value_dic['MemTotal']))
        # real MemUsage value
        value_dic['MemUsage'] = MemUsage

    except Exception as e:
        print(e)
        status = e.__str__().split(" ")[-1:]
        value_dic = {'status': status}

    return value_dic

a = monitor()
print(a)

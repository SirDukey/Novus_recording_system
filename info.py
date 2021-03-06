import subprocess as sp


def disk_usage():

    cmd= ['df', '-h']
    res = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    if output:
        output = output.split('\n')
        for line in output:
            if '/Novus_recording_system/mnt/broadcast' in line:
                line = line.split(' ')
                used_perc = list(filter(None, line))
                return used_perc[-2]

    elif error:
        print(error)
    else:
        print('unsuccessful')


def mem_usage():

    cmd= ['free', '-m']
    res = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    if output:
        output = output.split('\n')
        output = output[1]
        output = output.split(' ')
        output = list(filter(None, output))
        total = int(output[1])
        used = int(output[2])
        diff_perc = (total - used) / total * 100
        used_perc = 100 - diff_perc
        output = '%.0f' % used_perc + '%'
        return output

    elif error:
        print(error)
    else:
        print('unsuccessful')


def cpu_usage():
    cmd = ['mpstat']
    res = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')
    outlist = output.split(' ')
    idle = outlist[-1]
    used = 100.00 - float(idle)
    return '%.0f' % used + '%'


def watcher_service():
    res = sp.Popen(['systemctl', 'is-active', 'Novus_watcher.service'], stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('utf-8')
    return output


def watcher_start():
    sp.Popen(['systemctl', 'start', 'Novus_watcher.service'])


def watcher_stop():
    sp.Popen(['systemctl', 'stop', 'Novus_watcher.service'])


def restart_stats(station_list):
    results = dict()
    for station in station_list:
        wc = 0
        with open('logs/watcher.log', 'r') as f:
            for line in f:
                if station[0] in line:
                    wc += 1
        amount = wc / 4
        results[station[0]] = amount
    return results
import subprocess as sp


def disk_usage():

    cmd= ['df', '-h']
    res = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    if output:
        outlist = output.split('\n')
        outlist = outlist[3].split(' ')
        return outlist[-2]

    elif error:
        print(error)
    else:
        print('unsuccessful')


def mem_usage():

    cmd= ['free', '-h']
    res = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    if output:
        outlist = output.split('\n')
        outlist = outlist[1].split(' ')
        total = outlist[12].strip('G')
        used = outlist[20].strip('G')
        total = float(total)
        used = float(used)
        diff_perc = (total - used) / total * 100
        used_perc = 100 - diff_perc
        output = '%.0f' % used_perc + '%'
        return output

    elif error:
        print(error)
    else:
        print('unsuccessful')


def cpu_usage():

    pass

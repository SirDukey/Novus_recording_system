import subprocess as sp


def show_running_ps():

    res = sp.Popen(['ps', '-ax'], stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')
    if output:
        ps_ls = output.split('\n')
        new_ls = {'PID': 'NAME'}
        for l in sorted(ps_ls):
            if 'ffmpeg' in l:
                l = l.split(' ')
                new_ls['PID'] = l[0]
                new_ls['NAME'] = l[-1]
                print(new_ls['PID'], new_ls['NAME'])


if __name__ == '__main__':
    show_running_ps()
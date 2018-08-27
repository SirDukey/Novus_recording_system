from os import kill
import subprocess as sp
from flask import flash


def kill_pid(pid_num, name, url):

    def kill_it(pid_num):
        kill(int(pid_num), 15)
        print('killed pid:', pid_num)

    '''first test'''
    cmd = 'pgrep ffmpeg'
    res = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    '''second test'''
    cmd2 = 'ps -ax'
    res2 = sp.Popen(cmd2, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    output2, error2 = res2.communicate()
    output2 = output2.decode('ascii')
    error2 = error2.decode('ascii')

    if str(pid_num) in output and url in output2:
        kill_it(pid_num)
        flash('stopped recording pid: ' + str(pid_num))

    elif str(pid_num) not in output2 and url not in output2:
        print('process is no longer running')
        with open('pids/' + name + '.pid', 'w') as f:
            f.write('none')
    elif str(pid_num) not in output:
        print(str(pid_num), 'pid not found')
        with open('pids/' + name + '.pid', 'w') as f:
            f.write('none')
    elif error:
        print(error)
    elif error2:
        print(error2)


def kill_all():
    sp.Popen(['pkill', 'ffmpeg'])


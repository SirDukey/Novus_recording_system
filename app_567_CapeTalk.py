from flask import request
from process_control import kill_pid
from radio_recorder import record
import subprocess as sp


def check_pid(pid_num, name, url):
    '''first test'''
    cmd = 'pgrep ffmpeg'
    res = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    '''second test'''
    cmd2 = 'ps -ax | grep ffmpeg'
    res2 = sp.Popen(cmd2, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    output2, error2 = res2.communicate()
    output2 = output2.decode('ascii')
    error2 = error2.decode('ascii')

    if str(pid_num) in output and url not in output2:
        with open('pids/' + name + '.pid', 'w') as f:
            f.write('none')

    elif str(pid_num) not in output2 and url not in output2:
        with open('pids/' + name + '.pid', 'w') as f:
            f.write('none')

    elif str(pid_num) not in output:
        with open('pids/' + name + '.pid', 'w') as f:
            f.write('none')

    elif error:
        print(error)

    elif error2:
        print(error2)


def main_567_CapeTalk():

    name = '567_CapeTalk'
    url = 'http://19373.live.streamtheworld.com:3690/CAPE_TALK_SC'

    if request.method == 'POST':

        if '567_CapeTalk_start' in request.form:

            print('567_CapeTalk_start')
            record(name, url)

        elif '567_CapeTalk_stop' in request.form:

            print('567_CapeTalk_stop')
            try:
                with open('pids/567_CapeTalk.pid', 'r') as f:
                    try:
                        kill_pid(f.read(), name, url)
                    except:
                        print('no such process')
            finally:
                with open('pids/567_CapeTalk.pid', 'w') as f:
                    f.write('none')

    elif request.method == 'GET':

        pidf = open('pids/' + name + '.pid', 'r')
        pid_num = pidf.read()
        pidf.close()
        check_pid(pid_num, name, url)
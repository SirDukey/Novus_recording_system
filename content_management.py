from flask import request
from process_control import kill_pid
from radio_recorder import rad_record
from tv_recorder import tv_record
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


def rmain(name, url):

    if name + '_start' in request.form:

        print(name + '_start')
        rad_record(name, url)

    elif name + '_stop' in request.form:

        print(name + '_stop')
        try:
            with open('pids/{}.pid'.format(name), 'r') as f:
                try:
                    kill_pid(f.read(), name, url)
                except:
                    print('no such process')
        finally:
            with open('pids/{}.pid'.format(name), 'w') as f:
                f.write('none')

    elif request.method == 'GET':

        pidf = open('pids/' + name + '.pid', 'r')
        pid_num = pidf.read()
        pidf.close()
        check_pid(pid_num, name, url)


def tmain(name, url):

    if name + '_start' in request.form:

        print(name + '_start')

        tv_record(name, url)

    elif name + '_stop' in request.form:

        print(name + '_stop')
        try:
            with open('pids/{}.pid'.format(name), 'r') as f:
                try:
                    kill_pid(f.read(), name, url)
                except:
                    print('no such process')
        finally:
            with open('pids/{}.pid'.format(name), 'w') as f:
                f.write('none')

    elif request.method == 'GET':

        pidf = open('pids/' + name + '.pid', 'r')
        pid_num = pidf.read()
        pidf.close()
        check_pid(pid_num, name, url)


def get_pid(name):
    with open(name + '.pid', 'r') as f:
        return f.read()


def content():

    CMS_DICT = {
        'radio': [
            ['1FM', 'http://5.153.107.45:2016/mp3_ultra', rmain, get_pid],
            ['5FM', 'http://albert.antfarm.co.za:8000/5fm', rmain, get_pid],
            ['94_7_Highveld_Stereo', 'http://19113.live.streamtheworld.com:3690/FM947_SC', rmain, get_pid]
                  ],
        'tv': [
            ['MNET', 'rtp://@225.0.1.101:1100', tmain, get_pid],
            ['VUZU', 'rtp://@225.0.1.103:1200', tmain, get_pid],
            ['KYKNET', 'rtp://@225.0.1.116:1100', tmain, get_pid]
                ]
    }

    return CMS_DICT


CMS_DICT = content()
radio = CMS_DICT['radio']
tv = CMS_DICT['tv']

for item in radio:
    print(item[0])



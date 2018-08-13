from flask import request
from process_control import kill_pid
from radio_recorder import record


def main_94_7():
    '''94_7 channel'''
    if '94_7_start' in request.form:
        print('94_7_start')
        name = '94_7_Highveld_Stereo'
        url = 'http://19073.live.streamtheworld.com:3690/FM947_SC'
        record(name, url)

    elif '94_7_stop' in request.form:
        print('94_7_stop')
        try:
            with open('pids/94_7_Highveld_Stereo.pid', 'r') as f:
                try:
                    kill_pid(f.read())
                except:
                    print('no such process')
        finally:
            with open('pids/94_7_Highveld_Stereo.pid', 'w') as f:
                f.write('none')
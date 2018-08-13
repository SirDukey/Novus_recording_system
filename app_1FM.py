from flask import request
from process_control import kill_pid
from radio_recorder import record


def main_1FM():
    '''1FM channel'''
    if '1FM_start' in request.form:
        print('1FM_start')
        name = '1FM'
        url = 'http://5.153.107.45:2016/mp3_ultra'
        record(name, url)

    elif '1FM_stop' in request.form:
        print('1FM_stop')
        try:
            with open('pids/1FM.pid', 'r') as f:
                try:
                    kill_pid(f.read())
                except:
                    print('no such process')
        finally:
            with open('pids/1FM.pid', 'w') as f:
                f.write('none')
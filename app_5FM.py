from flask import request
from process_control import kill_pid
from radio_recorder import record


def main_5FM():
    '''5FM channel'''
    if '5FM_start' in request.form:
        print('5FM_start')
        name = '5FM'
        url = 'http://albert.antfarm.co.za:8000/5fm'
        record(name, url)

    elif '5FM_stop' in request.form:
        print('5FM_stop')
        try:
            with open('pids/5FM.pid', 'r') as f:
                try:
                    kill_pid(f.read())
                except:
                    print('no such process')
        finally:
            with open('pids/5FM.pid', 'w') as f:
                f.write('none')
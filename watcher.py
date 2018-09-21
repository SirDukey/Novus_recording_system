#!/usr/bin/python3

from os.path import getmtime
from app import content
from time import sleep
from schedule import every, run_pending
from os import kill
from radio_recorder import rad_record
from television_recorder import tv_record
import subprocess as sp
from datetime import datetime

CMS_DICT = content()
radio = CMS_DICT['radio']
tv = CMS_DICT['tv']


def double_check_for_duplicate_process():
    pass

def get_time():
    return str(datetime.now())


def job():

    # print('checking radio for enabled')
    for station in radio:

        if station[5](station[0]) == 'enabled':
            if 'timestamps/{}.ts'.format(station[0]):
                first_timestamp = getmtime('timestamps/{}.ts'.format(station[0]))
                sleep(10)
                second_timestamp = getmtime('timestamps/{}.ts'.format(station[0]))

                if str(second_timestamp) in str(first_timestamp):
                    with open('logs/watcher.log', 'a') as f:
                        f.write(get_time() + ' ' + station[0] + ' restart\n')
                    print(get_time(), station[0], 'restart')
                    try:
                        with open('logs/watcher.log', 'a') as f:
                            f.write(get_time() + ' attempting to kill station {}\n'.format(station[0]))
                        print(get_time(), 'attempting to kill station {}'.format(station[0]))
                        kill(station[3](station[0]), 9)
                    except:
                        with open('logs/watcher.log', 'a') as f:
                            f.write(get_time() + ' ' + station[0] + ' pid not present\n')
                        print(get_time(), station[0], 'pid not present')
                    finally:
                        with open('logs/watcher.log', 'a') as f:
                            f.write(get_time() + ' starting {}\n'.format(station[0]))
                        print(get_time(), 'starting {}'.format(station[0]))
                        sleep(2)
                        rad_record(station[0], station[1])

                else:
                    try:
                        sp.Popen(['truncate', '-s0', 'timestamps/{}.ts'.format(station[0])])
                    except:
                        pass
        else:
            pass

    # print('checking tv for enabled')
    for station in tv:

        if station[5](station[0]) == 'enabled':
            if 'timestamps/{}.ts'.format(station[0]):
                first_timestamp = getmtime('timestamps/{}.ts'.format(station[0]))
                sleep(10)
                second_timestamp = getmtime('timestamps/{}.ts'.format(station[0]))

                if str(second_timestamp) in str(first_timestamp):
                    with open('logs/watcher.log', 'a') as f:
                        f.write(get_time() + ' ' + station[0] + ' restart\n')
                    print(get_time(), station[0], 'restart')
                    try:
                        with open('logs/watcher.log', 'a') as f:
                            f.write(get_time() + ' attempting to kill station {}\n'.format(station[0]))
                        print(get_time(), 'attempting to kill station {}'.format(station[0]))
                        kill(station[3](station[0]), 9)
                    except:
                        with open('logs/watcher.log', 'a') as f:
                            f.write(get_time() + ' ' + station[0] + ' pid not present\n')
                        print(get_time(), station[0], 'pid not present')
                    finally:
                        with open('logs/watcher.log', 'a') as f:
                            f.write(get_time() + ' starting {}\n'.format(station[0]))
                        print(get_time(), 'starting {}'.format(station[0]))
                        sleep(2)
                        tv_record(station[0], station[1])

                else:
                    try:
                        sp.Popen(['truncate', '-s0', 'timestamps/{}.ts'.format(station[0])])
                    except:
                        pass
        else:
            pass


if __name__ == '__main__':

    every(30).seconds.do(job)

    while True:
        run_pending()
        sleep(2)

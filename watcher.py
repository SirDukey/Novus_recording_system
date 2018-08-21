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


def get_time():
    return str(datetime.now())


def job():

    # print('checking radio for enabled')
    for station in radio:

        if station[5](station[0]) == 'enabled':
            if 'timestamps/{}.ts'.format(station[0]):
                first_timestamp = getmtime('timestamps/{}.ts'.format(station[0]))
                sleep(1)
                second_timestamp = getmtime('timestamps/{}.ts'.format(station[0]))

                if str(second_timestamp) in str(first_timestamp):
                    print(get_time(), station[0], 'restart')
                    try:
                        print(get_time(), 'attempting to kill station {}'.format(station[0]))
                        kill(station[3](station[0]), signal.SIGKILL)
                    except:
                        print(get_time(), station[0], 'pid not present')
                    finally:
                        print(get_time(), 'starting {}'.format(station[0]))
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

        if station[5] == 'enabled':
            if 'timestamps/{}.ts'.format(station[0]):
                first_timestamp = getmtime('timestamps/{}.ts'.format(station[0]))
                sleep(1)
                second_timestamp = getmtime('timestamps/{}.ts'.format(station[0]))

                if str(second_timestamp) in str(first_timestamp):
                    print(get_time(), station[0], 'restart')
                    try:
                        print(get_time(), 'attempting to kill station {}'.format(station[0]))
                        kill(station[3](station[0]), signal.SIGKILL)
                    except:
                        print(get_time(), station[0], 'pid not present')
                    finally:
                        print(get_time(), 'starting {}'.format(station[0]))
                        tv_record(station[0], station[1])

                else:
                    try:
                        sp.Popen(['truncate', '-s0', 'timestamps/{}.ts'.format(station[0])])
                    except:
                        pass
        else:
            pass


if __name__ == '__main__':

    every(5).seconds.do(job)

    while True:
        run_pending()
        sleep(1)

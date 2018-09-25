#!/usr/bin/python3

from os.path import getmtime
from app import content
from time import sleep
from schedule import every, run_pending
from os import kill
from radio_recorder import rad_record, rad_record_m3u8
from television_recorder import tv_record
import subprocess as sp
from datetime import datetime

CMS_DICT = content()
radio = CMS_DICT['radio']
tv = CMS_DICT['tv']


def double_check_for_duplicate_process():
    res = sp.Popen(['ps', '-ax'], stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')
    psl = list()
    occurance = dict()
    dups = list()
    new_psl = dict()

    if output:
        ps_ls = output.split('\n')
        for l in sorted(ps_ls):
            if 'ffmpeg' in l:
                l = l.split(' ')
                l = list(filter(None, l))
                l_pid = l[0]
                l_name = l[-1].split('/')
                l_name = l_name[-1].split('.')
                l_name = l_name[0]
                psl.append((l_name, int(l_pid)))

    if error:
        print(error)

    for t in psl:
        if t[0] in occurance:
            occurance[t[0]] += 1
        else:
            occurance[t[0]] = 1

    for station in occurance.items():
        if station[1] > 1:
            dups.append(station[0])

    for station in psl:
        if station[0] in dups:
            new_psl[station[0]] = []

    for station in psl:
        if station[0] in dups:
            new_psl[station[0]].append(station[1])

    for x in new_psl.items():
        pid = min(x[1])
        kill(pid, 15)


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

                        # TODO: add logic if it is dab or www stream
                        if 'm3u8' in station[1]:
                            rad_record_m3u8(station[0], station[1])
                        else:
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

    double_check_for_duplicate_process()


if __name__ == '__main__':

    every(30).seconds.do(job)

    while True:
        run_pending()
        sleep(2)

import subprocess as sp
from multiprocessing import Process
from os.path import exists
from datetime import datetime
from flask import flash


def rad_record(name, url):

    #loc = '/home/mike/Documents/Python/Novus_recording_system/'
    loc = '/Novus_recording_system/mnt/broadcast/unindexed/'

    def ffmpeg(name, url, loc):

        process = sp.Popen(['ffmpeg',
                            #'-re',
                            '-nostats',
                            '-loglevel', '0',
                            '-xerror',
                            '-progress', 'timestamps/' + name + '.ts',
                            #'-y'
                            '-live_start_index', '-1',
                            '-i', '{}'.format(url),
                            '-stimeout', '10000',
                            # '-c, 'copy',
                            '-codec:a', 'libmp3lame',
                            '-b:a', '64000',
                            '-ac', '1',
                            '-ar', '16000',
                            # '-b:v', '1M',
                            # '-vf', 'scale=320:240',
                            '-f', 'segment',
                            '-segment_time', '120',
                            '-segment_atclocktime', '1',
                            '-strftime', '1',
                            # '-force_key_frames', '120',
                            '-reset_timestamps', '1',
                            loc + name + '.%Y-%m-%d_%H-%M-%S.mp3'])

        with open('pids/' + name + '.pid', 'w') as f:
            f.write(str(process.pid))

        print(str(datetime.now().strftime('%d-%m-%Y__%H:%M:%S ')) + 'started recording', name, 'on process id:',
              str(process.pid))

        return process.pid

    p = Process(target=ffmpeg, args=(name, url, loc))

    if exists(loc):
        p.start()

    else:
        print(str(datetime.now().strftime('%d-%m-%Y__%H:%M:%S ')) + loc, 'is not mounted')
        flash(loc + ' is not mounted')


def dab_record(name, dab_id, freq):

    loc = '/Novus_recording_system/clips_dab/'
    #loc = '/mnt/broadcast/unindexed/'

    def ffmpeg(name, dab_id, freq, loc):

        rtl = sp.Popen(['rtl_fm',
                        '-d', str(dab_id),
                        '-f', freq,
                        '-M', 'fm',
                        '-s', '170k',
                        '-A', 'std',
                        '-l', '0',
                        '-E', 'deemp',
                        '-r', '44.1k'], stdout=sp.PIPE)

        process = sp.Popen(['ffmpeg',
                            # '-re',
                            '-nostats',
                            '-loglevel',
                            '0',
                            '-xerror',
                            '-progress',
                            'timestamps/' + name + '.ts',
                            # '-y'
                            '-f', 's16le',
                            '-i',
                            'pipe:0',
                            '-stimeout',
                            '10000',
                            # '-c, 'copy',
                            '-codec:a',
                            'libmp3lame',
                            '-b:a',
                            '64000',
                            '-ac',
                            '1',
                            '-ar',
                            '16000',
                            # '-b:v', '1M',
                            # '-vf', 'scale=320:240',
                            '-f',
                            'segment',
                            '-segment_time',
                            '120',
                            '-strftime',
                            '1',
                            # '-force_key_frames', '120',
                            '-reset_timestamps',
                            '1',
                            loc + name + '.%Y-%m-%d_%H-%M-%S.mp3'], stdin=rtl.stdout)

        with open('pids/' + name + '.pid', 'w') as f:
            f.write(str(process.pid))

        print(str(datetime.now().strftime('%d-%m-%Y__%H:%M:%S ')) + 'started recording', name, 'on process id:',
              str(process.pid))

        return process.pid

    p = Process(target=ffmpeg, args=(name, dab_id, freq, loc))

    if exists(loc):
        p.start()

    else:
        print(str(datetime.now().strftime('%d-%m-%Y__%H:%M:%S ')) + loc, 'is not mounted')
        flash(loc + ' is not mounted')


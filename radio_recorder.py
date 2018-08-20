import subprocess as sp
from multiprocessing import Process
from os.path import exists
from datetime import datetime
from flask import flash


def rad_record(name, url):

    #loc = '/home/mike/Documents/Python/Novus_recording_system/'
    loc = '/mnt/broadcast/unindexed/'

    def ffmpeg(name, url, loc):

        process = sp.Popen(['ffmpeg',
                            #'-re',
                            '-nostats',
                            '-loglevel',
                            '0',
                            '-xerror',
                            '-progress',
                            'timestamps/' + name + '.ts',
                            #'-y'
                            '-i',
                            url,
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
                            loc + name + '.%Y-%m-%d_%H-%M-%S.mp3'])

        with open('pids/' + name + '.pid', 'w') as f:
            f.write(str(process.pid))

        print(str(datetime.now().strftime('%d-%m-%Y__%H:%M:%S ')) + 'started recording', name, 'on process id:', str(process.pid))
        #flash('started ' + name + ' on pid: ' + str(process.pid))
        return process.pid

    p = Process(target=ffmpeg, args=(name, url, loc))

    if exists(loc):
        p.start()

    else:
        print(str(datetime.now().strftime('%d-%m-%Y__%H:%M:%S ')) + loc, 'is not mounted')
        flash(loc + ' is not mounted')
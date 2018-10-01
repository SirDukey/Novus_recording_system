import subprocess as sp
from multiprocessing import Process
from os.path import exists
from datetime import datetime
from flask import flash


def tv_record(name, url):

    loc = '/Novus_recording_system/clips/'

    def ffmpeg(name, url, loc):

        process = sp.Popen(['ffmpeg',
                            '-re',
                            '-nostats',
                            '-loglevel', '0',
                            '-progress', 'timestamps/' + name + '.ts',
                            '-i', url,
                            '-stimeout', '10000',
                            '-c:a', 'libvo_aacenc',
                            '-b:a', '64000',
                            '-ac', '1',
                            '-ar', '16000',
                            '-af', 'aresample=async=1',
                            '-c:v', 'libx264',
                            '-preset', 'ultrafast',
                            '-b:v', '768K',
                             '-vf', 'scale=320:240',
                            '-f', 'segment',
                            '-segment_time', '120',
                            '-segment_atclocktime', '1',
                            '-strftime', '1',
                            '-reset_timestamps', '1',
                            loc + name + '.%Y-%m-%d_%H-%M-%S.mp4'])

        with open('pids/' + name + '.pid', 'w') as f:
            f.write(str(process.pid))

        print(str(datetime.now().strftime('%d-%m-%Y__%H:%M:%S ')) + 'started recording', name, 'on process id:', str(process.pid))
        return process.pid

    p = Process(target=ffmpeg, args=(name, url, loc))

    if exists(loc):
        p.start()

    else:
        print(str(datetime.now().strftime('%d-%m-%Y__%H:%M:%S ')) + loc, 'is not mounted')
        flash(loc + ' is not mounted')
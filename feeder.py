import subprocess as sp
from app import content
from time import sleep

CMS_DICT = content()

for item in CMS_DICT['tv']:

    feed = sp.Popen(['ffmpeg', '-nostats', '-loglevel', '0', '-xerror',
                     '-i', item[1], 'http://127.0.0.1:8090/{}.ffm'.format(item[0])])
    print(item[0], 'feed on PID:', str(feed.pid))
    sleep(5)

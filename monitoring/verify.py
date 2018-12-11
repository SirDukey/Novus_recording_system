import subprocess as sp
import psycopg2
from sys import argv

namedFile = argv[1]

connect_str = "dbname='recording' user='postgres' host='mail.novusgroup.co.za' password='global01a'"
conn = psycopg2.connect(connect_str)
cur = conn.cursor()

def SQLupdate(v, a, t, c):
    SQL_UPDATE = "UPDATE channels " \
                 "SET video='{}',audio='{}',ftype='{}' " \
                 "WHERE name='{}'".format(v, a, t, c)

    cur.execute(SQL_UPDATE)
    conn.commit()


def verify(file):

    chanList = file.split('.')
    chan = chanList[0]
    fileType = chanList[-1]

    cmd = ['ffprobe', '-show_entries', 'stream=index,codec_type', '-of', 'csv=p=0', file]
    res = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    if output:
        print('=====OUTPUT=====')
        print('testing:', chan, fileType)
        print(output)
        
        if fileType == 'mp4':
            if 'video' in output and 'audio' in output:
                print('video and audio present')
                vid = 'TRUE'
                aud = 'TRUE'
                SQLupdate(vid, aud, fileType, chan)

            elif 'video' in output and 'audio' not in output:
                print('video present, no audio found')
                vid = 'TRUE'
                aud = 'FALSE'
                SQLupdate(vid, aud, fileType, chan)

            elif 'video' not in output and 'audio' in output:
                print('audio present, no audio found')
                vid = 'FALSE'
                aud = 'TRUE'
                SQLupdate(vid, aud, fileType, chan)

            elif 'video' not in output and 'audio' not in output:
                print('no video or audio found')
                vid = 'FALSE'
                aud = 'FALSE'
                SQLupdate(vid, aud, fileType, chan)

            else:
                print('error found with file')
            print()

        elif fileType == 'mp3':
            if 'audio' in output:
                print('audio present')
                aud = 'TRUE'
                vid = 'FALSE'
                chan = chanList[1]
                print(chan[1:])
                SQLupdate(vid, aud, fileType, chan[1:])

            elif 'audio' not in output:
                aud = 'FALSE'
                vid = 'FALSE'
                chan = chanList[1]
                print(chan[1:])
                SQLupdate(vid, aud, fileType, chan[1:])

            else:
                print('error found with file')
            print()

    elif error:
        print('=====ERROR======')
        print(error)
        print()



if __name__ == '__main__':

    verify(namedFile)

    cur.close()
    conn.close()

import psycopg2
from os import kill
import subprocess as sp
from datetime import datetime


def getTime():
    return str(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))


def testPID(n, p):
    psRes = sp.Popen(['ps', '-aux'], stdout=sp.PIPE, stderr=sp.PIPE)
    grepRes = sp.Popen(['grep', str(p)], stdin=psRes.stdout, stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = grepRes.communicate()
    if output:
        output = output.decode('ascii')
        if str(n) in output:
            print('-- pid {} belongs to {}'.format(p, n))
            killPID(p)
    elif error:
        error = error.decode('ascii')
        print(error)


def killPID(p):
    print('-- killing pid:', p)
    kill(p, 9)


def runTest():
    connect_str = "dbname='recording' user='postgres' host='mail.novusgroup.co.za' password='global01a'"
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()

    SQL_QUERY = "SELECT * FROM channels " \
                "WHERE ftype = 'mp4' " \
                "AND audio = FALSE"

    cur.execute(SQL_QUERY)
    results = cur.fetchall()

    for r in results:
        pid = r[1]
        audio = r[5]
        name = r[2]
        if audio is False:
            print()
            print('{}'.format(getTime()))
            print('no audio found for:', name)
            print('-- testing pid belongs to', name)
            testPID(name, pid)


if __name__ == '__main__':
    runTest()
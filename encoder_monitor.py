import subprocess as sp
import psycopg2
import socket
from app import content


def encoder_check():

    connect_str = "dbname='recording' user='postgres' host='mail.novusgroup.co.za' password='global01a'"
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    host_name = socket.gethostname()

    unit_dict = {
            '192.168.55.3': '',
            '192.168.55.4': '',
            '192.168.55.5': '',
            '192.168.55.6': '',
            '192.168.55.7': '',
            '192.168.55.8': '',
            '192.168.55.9': '',
            '192.168.55.10': '',
            '192.168.55.11': '',
            '192.168.55.12': '',
            '192.168.55.13': '',
            '192.168.55.14': '',
            '192.168.55.15': ''
        }

    if host_name == 'novflask':
        for unit in unit_dict.keys():
            res = sp.Popen(['ping', '-c1', unit], stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = res.communicate()
            output = output.decode('ascii')
            if '0 received' in output:
                unit_dict[unit] = '0'
            else:
                unit_dict[unit] = '1'

        for unit in unit_dict.items():
            SQL_UPDATE = "UPDATE encoders SET state={} WHERE ipaddr='{}';".format(unit[1], unit[0])

            cur.execute(SQL_UPDATE)
            conn.commit()

    else:
        print('not available for this host')

    cur.close()
    conn.close()


def channel_check():

    def SQL_TASK(channel):

        name = channel[0]
        pid = channel[3]
        pid = pid(name)
        if pid == 'none':
            pid = 0
        state = channel[5]
        state = state(name)
        svr = host_name

        SQL_QUERY = "SELECT * " \
                    "FROM  channels;"

        SQL_INSERT = "INSERT INTO channels (pid,name,state,svr) " \
                     "VALUES ({},'{}','{}','{}');".format(pid, name, state, svr)

        SQL_UPDATE = "UPDATE channels " \
                     "SET pid={},state='{}',svr='{}' " \
                     "WHERE name='{}' AND svr='{}';".format(pid, state, svr, name, svr)

        cur.execute(SQL_QUERY)
        res = cur.fetchall()
        my_list = []

        for item in res:
            my_list.append(item[2])

        if name in my_list:
            if state == 'enabled':
                cur.execute(SQL_UPDATE)
                conn.commit()
        else:
            cur.execute(SQL_INSERT)
            conn.commit()

    CMS_DICT = content()
    radio = CMS_DICT['radio']
    tv = CMS_DICT['tv']

    connect_str = "dbname='recording' user='postgres' host='mail.novusgroup.co.za' password='global01a'"
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    host_name = socket.gethostname()

    if host_name == 'radio':
        for channel in radio:
            SQL_TASK(channel)

    elif host_name == 'radio-backup':
        for channel in radio:
            SQL_TASK(channel)

    elif host_name == 'novflask':
        for channel in tv:
            SQL_TASK(channel)


    cur.close()
    conn.close()


if __name__ == '__main__':
    encoder_check()
    channel_check()

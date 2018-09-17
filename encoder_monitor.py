import subprocess as sp
import psycopg2
import socket


def encoder_check():

    print('making database connection')
    connect_str = "dbname='recording' user='postgres' host='mail.novusgroup.co.za' password='global01a'"
    conn = psycopg2.connect(connect_str)
    cur = conn.cursor()
    host_name = socket.gethostname()
    print(host_name)

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

    print('checking hostname')
    if host_name == 'novflask':
        for unit in unit_dict.keys():
            print('checking if {} is online'.format(str(unit)))
            res = sp.Popen(['ping', '-c1', unit], stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = res.communicate()
            output = output.decode('ascii')
            if '0 received' in output:
                unit_dict[unit] = '0'
            else:
                unit_dict[unit] = '1'

        for unit in unit_dict.items():
            print('updating sql')
            SQL_UPDATE = "UPDATE encoders SET state={} WHERE ipaddr='{}';".format(unit[1], unit[0])

            cur.execute(SQL_UPDATE)
            conn.commit()

    else:
        print('not available for this host')

    cur.close()
    conn.close()


if __name__ == '__main__':
    print('running encoder check')
    encoder_check()

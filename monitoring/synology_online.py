import paramiko

client = paramiko.client.SSHClient()
client.load_system_host_keys()

try:
    client.connect('vpn.novusgroup.co.za', port=22019, username='admin', password='global01a')
    try:
        stdin, stdout, stderr = client.exec_command('cat /volume1/broadcast/sysadmin/online.txt', timeout=5)
        if stdout:
            x = stdout.read()
            x = x.decode('ascii')
            if x == 'online\n':
                print(0)
        elif stderr:
            print(1)

    except:
        '''cant read online.txt file'''
        print(1)
except:
    '''cant connect'''
    print(1)


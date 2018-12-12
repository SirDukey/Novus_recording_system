from sys import argv

chan = argv[1]

with open('/Novus_recording_system/auto/{}.auto'.format(chan), 'r') as e:
    if e.read() == 'enabled':
        with open('/Novus_recording_system/pids/{}.pid'.format(chan), 'r') as f:
            if f.read() == 'none':
                print(0)
            else:
                print(1)

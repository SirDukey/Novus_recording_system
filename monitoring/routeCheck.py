#!/usr/bin/python3

import subprocess as sp

res = sp.Popen(['ip', 'r'], stdout=sp.PIPE, stderr=sp.PIPE)
output, error = res.communicate()
output = output.decode('ascii')
error = error.decode('ascii')

with open('/Novus_recording_system/monitoring/routeTable.txt', 'r') as f:
    if output:
        control = f.read()
        if output == control:
            print(1)
        else:
            print(0)

    elif error:
        print(20)

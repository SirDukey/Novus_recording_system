import subprocess as sp

res = sp.Popen(['systemctl', 'is-active', 'Novus_watcher.service'], stdout=sp.PIPE, stderr=sp.PIPE)
output, error = res.communicate()
output = output.decode('ascii')
error = error.decode('ascii')

if output:
    output = output.split('\n')
    if output[0] == 'active':
        print(1)
    elif output[0] == 'inactive':
        print(0)

elif error:
    print(3)

from os import kill
import subprocess as sp
from datetime import datetime


def kill_pid(pid_num):

    def kill_it(pid_num):
        kill(int(pid_num), 15)
        print(str(datetime.now().strftime('%d-%m-%Y__%H:%M:%S ')) + 'killed pid:', pid_num)

    cmd = 'pgrep ffmpeg'
    res = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    if str(pid_num) in output:
        kill_it(pid_num)
    elif str(pid_num) not in output:
        print(str(datetime.now().strftime('%d-%m-%Y__%H:%M:%S ')) + 'pid not found')
    elif error:
        print(error)
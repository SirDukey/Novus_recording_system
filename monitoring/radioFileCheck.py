#!/usr/bin/python3

from sys import argv
import os, fnmatch

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

res = find(argv[1] + '*', '/Novus_recording_system/mnt/broadcast/unindexed/')
if res == []:
    print(0)
else:
    print(1)
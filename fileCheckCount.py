#!/usr/bin/python3

import os, fnmatch
from app import content

CMS = content()
channels = CMS['tv']
counter = 0

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


if __name__ == '__main__':
    for x in channels:
        res = find(x[0] + '*', '/Novus_recording_system/clips/')
        if res != []:
            counter += 1

    print(counter)

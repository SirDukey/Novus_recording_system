#!/bin/bash

cd /Novus_recording_system/clips

/usr/bin/find *.mp4 \
-type f \
-cmin +4 \
-exec /usr/bin/python3 /Novus_recording_system/monitoring/verify.py {} \; \
-exec /usr/bin/rsync --remove-source-files -av --no-p -O {} /Novus_recording_system/mnt/broadcast/unindexed/ \;


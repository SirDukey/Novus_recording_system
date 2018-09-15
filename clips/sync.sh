#!/bin/bash

/usr/bin/find /Novus_recording_system/clips/*.mp4 \
-type f \
-cmin +4 \
-exec \
/usr/bin/rsync --remove-source-files -av --no-p -O \
{} \
/Novus_recording_system/mnt/broadcast/unindexed/ \;

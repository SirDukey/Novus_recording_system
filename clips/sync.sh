#!/bin/bash

/usr/bin/find /Novus_recording_system/clips/*.mp4 \
-type f \
-cmin +5 \
-exec \
/usr/bin/rsync --remove-source-files -av --no-p -O \
{} \
/mnt/broadcast/unindexed/ \;

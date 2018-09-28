# Novus_recording_system

Flask application to control the Novus recording system

The system is a control platform to start/stop recording radio and tv sources.
The name_dab.py is used to start conversion from the DAB+FM usb dongle to an ip stream.
Checkout the screenshots folder to see examples of the system.

## Dependancies
* DAB+FM (Realtek 2832) usb dongle for stations that do not have an internet stream
* rtl_fm (found in rtl-sdr) for accessing the usb dongle fm stream
* gunicorn wsgi server
* mpstat from the systat package used for cpu info
* nginx for client requests, config is found in services directory
* DSTV streams via Televes HDMI encoders
* shellinabox (apt install shellinabox)
* crontab entries as follows:

  "# truncate timestamp files"
  "0 * * * * truncate -s0 /Novus_recording_system/timestamps/*
  "# rsync from clip dir to /mnt/broadcast/unindexed"
  "* * * * * sh /Novus_recording_system/clips/sync.sh >> /var/log/clips_sync.log"

* systemd service files to start main frontend and watcher, config in services directory

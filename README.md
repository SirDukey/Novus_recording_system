# Novus_recording_system

Flask application to control the Novus recording system

The system is a control platform to start/stop recording radio and tv sources.
The name_dab.py is used to start conversion from the DAB+FM usb dongle to an ip stream.
Checkout the screenshots folder to see examples of the system.

## Dependancies
* _DAB+FM_ (Realtek 2832) usb dongle for stations that do not have an internet stream
* _rtl_fm_ (found in rtl-sdr) for accessing the usb dongle fm stream
* _gunicorn_ wsgi server
* _mpstat_ from the _systat_ package used for cpu info
* _nginx_ for client requests, config is found in services directory
* DSTV streams via Televes HDMI encoders
* _shellinabox_ (apt install shellinabox)
* _pip3_
* _flask_ (pip3 install)
* _flask_simplelogin_ (pip3 install)
* _schedule_ for watcher(pip3 isntall)
* _paramiko_ for monitoring (pip3 install)
* _crontab_ entries as follows:

  "# truncate timestamp files"
  "_0 * * * * truncate -s0 /Novus_recording_system/timestamps/*_"

  "# rsync from clip dir to /mnt/broadcast/unindexed"
  "_* * * * * flock -xn /root/sync.lck -c '/root/sync.sh >> /var/log/sync.log'_"

* systemd service files to start main frontend and watcher, config in services directory

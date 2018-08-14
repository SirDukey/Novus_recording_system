# Novus_recording_system

Flask application to control the Novus recording system

The system is a control platform to start/stop recording radio and tv sources.
The name_dab.py is used to start conversion from the DAB+FM usb dongle to an ip stream.
Checkout the screenshots folder to see examples of the system.

## Dependancies
* DAB+FM (Realtek 2832) usb dongle for stations that do not have an internet stream
* rtl_fm (found in rtl-sdr) for accessing the usb dongle fm stream

## TODO: 
* logs
* create way for make display the running states, currently it reads a .pid file < DONE
* create cms dictionaries for control pages to iterate over, will allow system to be updated dynamically without hardcoding in channels

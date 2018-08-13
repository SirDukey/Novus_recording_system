from os import system

system('rtl_fm -d 0 -f 98M -M fm -s 170k -A std  -l 0 -E deemp -r 44.1k  | ffmpeg -nostats -loglevel 0 -f s16le -ac 1 -i pipe:0  -acodec libmp3lame -ab 128k -f rtp rtp://127.0.0.1:1234')

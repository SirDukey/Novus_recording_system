from flask import Flask, request, render_template, Response
from flask_simplelogin import SimpleLogin, login_required
from process_control import kill_pid, kill_all, show_running_ps, ps_kill
from radio_recorder import rad_record, dab_record, rad_record_m3u8
from television_recorder import tv_record
import subprocess as sp
from info import mem_usage, cpu_usage, disk_usage, watcher_service, watcher_start, watcher_stop, restart_stats
from get_watcher_log import watcher_log, clear_watcher_log
from os import listdir
import random
from time import sleep
import socket

app = Flask(__name__)

app.config['SIMPLELOGIN_USERNAME'] = 'admin'
app.config['SIMPLELOGIN_PASSWORD'] = 'global01a'
SECRET_KEY = 'oV8rgcvFY1YcEWo7jXmoPQi5gaeX1J'
app.config['SECRET_KEY'] = SECRET_KEY

SimpleLogin(app)


def get_hostname():
    return socket.gethostname()

def readme():
    read_me_file = []
    with open('README.md', 'r') as f:
        read_me_file.append(f.read().split('\n'))
    return read_me_file


def du_clip_dir():
    res = sp.Popen(['du', '-hs', 'clips'], stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')
    if output:
        if 'M' in output:
            output = output.split('M')
            return str(output[0]) + 'M'
        elif 'G' in output:
            output = output.split('G')
            return str(output[0]) + 'G'
        elif 'K' in output:
            output = output.split('K')
            return str(output[0]) + 'K'
    elif error:
        return error


def du_unindexed_dir():
    res = sp.Popen(['du', '-hs', 'mnt/broadcast/unindexed'], stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')
    if output:
        if 'M' in output:
            output = output.split('M')
            return str(output[0]) + 'M'
        elif 'G' in output:
            output = output.split('G')
            return str(output[0]) + 'G'
        elif 'K' in output:
            output = output.split('K')
            return str(output[0]) + 'K'
    elif error:
        return error


def check_pid(pid_num, name, url):

    '''first test'''
    cmd = 'pgrep ffmpeg'
    res = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    '''second test'''
    cmd2 = 'ps -ax | grep ffmpeg'
    res2 = sp.Popen(cmd2, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    output2, error2 = res2.communicate()
    output2 = output2.decode('ascii')
    error2 = error2.decode('ascii')

    if str(pid_num) in output and url not in output2:
        with open('pids/' + name + '.pid', 'w') as f:
            f.write('none')
            # kill ?

    elif str(pid_num) not in output2 and url not in output2:
        with open('pids/' + name + '.pid', 'w') as f:
            f.write('none')

    elif str(pid_num) not in output:
        with open('pids/' + name + '.pid', 'w') as f:
            f.write('none')

    elif error:
        print(error)

    elif error2:
        print(error2)


# TODO: get the freq to use in second test
def dab_check_pid(pid_num, name, rtl):

    '''first test'''
    cmd = 'pgrep ffmpeg'
    res = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    '''second test'''
    cmd2 = 'ps -ax | grep rtl_fm'
    res2 = sp.Popen(cmd2, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)

    output2, error2 = res2.communicate()
    output2 = output2.decode('ascii')
    error2 = error2.decode('ascii')

    if str(pid_num) in output and rtl not in output2:
        with open('pids/' + name + '.pid', 'w') as f:
            f.write('none')

    elif str(pid_num) not in output:
        with open('pids/' + name + '.pid', 'w') as f:
            f.write('none')

    elif error:
        print(error)

    elif error2:
        print(error2)


def rmain(name, url, rtype):

    if name + '_start' in request.form:

        print(name + '_start')

        #if 'www' in rtype:
        if 'www' in rtype and 'm3u8' not in url[-4:]:
            rad_record(name, url)
        elif 'www' in rtype and 'm3u8' in url[-4:]:
            rad_record_m3u8(name, url)
        elif 'dab' in rtype:
            dab_record(name, url[0], url[1])

    elif name + '_stop' in request.form:

        print(name + '_stop')
        try:
            with open('pids/{}.pid'.format(name), 'r') as f:
                try:
                    kill_pid(f.read(), name, url)
                except:
                    print('no such process')
        finally:
            with open('pids/{}.pid'.format(name), 'w') as f:
                f.write('none')

    elif request.method == 'GET':

        pidf = open('pids/' + name + '.pid', 'r')
        pid_num = pidf.read()
        pidf.close()

        if 'www' in rtype:
            check_pid(pid_num, name, url)
        elif 'dab' in rtype:
            dab_check_pid(pid_num, name, 'rtl')


def tmain(name, url):

    if name + '_start' in request.form:

        print(name + '_start')

        tv_record(name, url)

    elif name + '_stop' in request.form:

        print(name + '_stop')
        try:
            with open('pids/{}.pid'.format(name), 'r') as f:
                try:
                    kill_pid(f.read(), name, url)
                except:
                    print('no such process')
        finally:
            with open('pids/{}.pid'.format(name), 'w') as f:
                f.write('none')

    elif request.method == 'GET':

        pidf = open('pids/' + name + '.pid', 'r')
        pid_num = pidf.read()
        pidf.close()
        check_pid(pid_num, name, url)


def get_pid(name):

    with open('pids/' + name + '.pid', 'r') as f:
        return f.read()


def get_auto(name):

    with open('auto/' + name + '.auto', 'r') as f:
        return f.read()


def set_auto(name):
    if name + '_enabled' in request.form:
        with open('auto/' + name + '.auto', 'w') as f:
            f.write('enabled')

    elif name + '_disabled' in request.form:
        with open('auto/' + name + '.auto', 'w') as f:
            f.write('disabled')

    elif request.method == 'GET':
        pass


def mp3_running():
    cmd = 'ps -ef | grep ffmpeg | grep .mp3 | wc -l'
    res = sp.Popen(cmd, shell=True, stdout=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    output = int(output) - 1
    return output


def mp4_running():
    cmd = 'ps -ef | grep ffmpeg | grep .mp4 | wc -l'
    res = sp.Popen(cmd, shell=True, stdout=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    output = int(output) - 1
    return output


def rcount_enabled():

    CMS_DICT = content()
    radio = CMS_DICT['radio']

    counter = 0

    for item in radio:
        with open('auto/' + item[0] + '.auto', 'r') as f:
            res = f.read()
            if 'enabled' in res:
                counter += 1
    return counter


def tcount_enabled():

    CMS_DICT = content()
    tv = CMS_DICT['tv']

    counter = 0

    for item in tv:
        with open('auto/' + item[0] + '.auto', 'r') as f:
            res = f.read()
            if 'enabled' in res:
                counter += 1
    return counter


def rstart_all():

    for item in radio:
        item[2](item[0], item[1])


def renable_all():

    CMS_DICT = content()
    radio = CMS_DICT['radio']

    for item in radio:
        with open('auto/' + item[0] + '.auto', 'w') as f:
            f.write('enabled')


def tenable_all():

    CMS_DICT = content()
    tv = CMS_DICT['tv']

    for item in tv:
        with open('auto/' + item[0] + '.auto', 'w') as f:
            f.write('enabled')


def rdisable_all():

    CMS_DICT = content()
    radio = CMS_DICT['radio']

    for item in radio:
        with open('auto/' + item[0] + '.auto', 'w') as f:
            f.write('disabled')


def tdisable_all():

    CMS_DICT = content()
    tv = CMS_DICT['tv']

    for item in tv:
        with open('auto/' + item[0] + '.auto', 'w') as f:
            f.write('disabled')


def find_mp4(name):

    clips = listdir('clips/')
    count = 0
    my_ls = []
    try:
        for clip in clips:
            if name in clip:
                count += 1
                my_ls.append(clip)
                my_ls.sort()
        if count > 2:
            return my_ls[-2]
        elif count == 1:
            return 'test_pattern.mp4'
        else:
            return my_ls[0]
    except:
        return 'test_pattern.jpg'


def encoder_check():

    #ip = socket.gethostbyname(socket.gethostname())
    name = socket.gethostname()

    unit_dict = {
            '192.168.55.3': '',
            '192.168.55.4': '',
            '192.168.55.5': '',
            '192.168.55.6': '',
            '192.168.55.7': '',
            '192.168.55.8': '',
            '192.168.55.9': '',
            '192.168.55.10': '',
            '192.168.55.11': '',
            '192.168.55.12': '',
            '192.168.55.13': '',
            '192.168.55.14': '',
            '192.168.55.15': ''
        }

    if name == 'novflask':
        for unit in unit_dict.keys():
            res = sp.Popen(['ping', '-c1', unit], stdout=sp.PIPE, stderr=sp.PIPE)
            output, error = res.communicate()
            output = output.decode('ascii')
            if '0 received' in output:
                unit_dict[unit] = 'offline'
            else:
                unit_dict[unit] = 'online'
        if 'offline' in unit_dict.values():
            for unit in unit_dict.items():
                if 'offline' in unit:
                    yield str(unit[0]) + ' ' + str(unit[1])
        else:
            yield 'online'
    else:
        yield 'not available for this host'


def show_clips():
    clip_dir = listdir('clips/')
    clip_dir.sort()
    return clip_dir


def show_clips_dab():
    clip_dir = listdir('clips_dab/')
    clip_dir.sort()
    return clip_dir


def show_mnt():
    mnt_dir = listdir('mnt/broadcast/unindexed/')
    mnt_dir.sort()
    return mnt_dir


def get_routes():
    res = sp.Popen(['ip', 'r'], stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = res.communicate()
    output = output.decode('ascii')
    error = error.decode('ascii')

    if output:
        my_ls = []
        my_ls.append(output.split('\n'))
        return my_ls[0]
    elif error:
        return error


def set_routes():
    sp.Popen(['sh', 'routes.sh'])


def content():

    CMS_DICT = {
        'radio': [
            ['1FM', 'http://5.153.107.45:2016/mp3_ultra', rmain, get_pid, 'www', get_auto, set_auto],
            ['5FM', 'http://albert.antfarm.co.za:8000/5fm', rmain, get_pid, 'www', get_auto, set_auto],
            ['94_7_Highveld_Stereo', 'http://19113.live.streamtheworld.com:3690/FM947_SC', rmain, get_pid, 'www', get_auto, set_auto],
            ['94_5_KFM', 'http://19993.live.streamtheworld.com/KFM_SC', rmain, get_pid, 'www', get_auto, set_auto],
            ['2OceansVibe', 'http://playerservices.streamtheworld.com/api/livestream-redirect/OCEANSVIBE_SC', rmain, get_pid, 'www', get_auto, set_auto],
            ['567_CapeTalk', 'http://19373.live.streamtheworld.com:3690/CAPE_TALK_SC', rmain, get_pid, 'www', get_auto, set_auto],
            ['99FM', 'http://ice31.securenetsystems.net/99FM?type=mp3', rmain, get_pid, 'www', get_auto, set_auto],
            ['Algoa_FM', 'https://edge.iono.fm/xice/54_medium.aac?p=embed', rmain, get_pid, 'www', get_auto, set_auto],
            ['BayFM', 'http://85.25.18.48/;.mp3', rmain, get_pid, 'www', get_auto, set_auto],
            ['Cape_Pulpit', 'http://albert.antfarm.co.za:8000/RadioPulpit', rmain, get_pid, 'www', get_auto, set_auto],
            ['Capricorn', 'http://albert.antfarm.co.za:8000/CapricornFM', rmain, get_pid, 'www', get_auto, set_auto],
            ['ChaiFM', 'http://listenlive-c2p1.ndstream.net:8060/;', rmain, get_pid, 'www', get_auto, set_auto],
            ['Channel_Africa', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/557f47f80b264cea8e88346a123eedcd/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            ['Classic_FM', 'https://edge.iono.fm/xice/49_medium.aac?p=embed', rmain, get_pid, 'www', get_auto, set_auto],
            ['CliffCentral_com', 'http://edge.iono.fm/xice/cliffcentral_live_medium.mp3', rmain, get_pid, 'www', get_auto, set_auto],
            ['East_Coast_Radio', 'http://edge.iono.fm/xice/ecr_live_medium.mp3', rmain, get_pid, 'www', get_auto, set_auto],
            ['Eldos_FM', 'http://core2.netdynamix.co.za:8100/;', rmain, get_pid, 'www', get_auto, set_auto],
            ['Energy_100FM', 'http://196.44.136.119:8080/;', rmain, get_pid, 'www', get_auto, set_auto],
            ['Fine_Music_Radio', 'http://edge.iono.fm/xice/fmr_live_medium.mp3?p=embed', rmain, get_pid, 'www', get_auto, set_auto],
            ['Fresh_FM', 'http://ample-zeno-02.radiojar.com/2b729cqx73duv?rj-ttl=5&rj-token=AAABZTMPpQtBNgSGaINlnak7_XktOhkAJPzuWahBJlaZ6r70oYUqJQ', rmain, get_pid, 'www', get_auto, set_auto],
            ['Gagasi_FM', 'http://capeant.antfarm.co.za:8000/gagasi', rmain, get_pid, 'www', get_auto, set_auto],
            ['Good_Hope_FM', 'http://radiostream.co.za:9104/;', rmain, get_pid, 'www', get_auto, set_auto],
            ['Groot_FM', 'http://grootfm.highquality.radiostream.co.za/', rmain, get_pid, 'www', get_auto, set_auto],
            ['Heart_104_9_FM', 'http://capeant.antfarm.co.za:8000/HeartFM', rmain, get_pid, 'www', get_auto, set_auto],
            ['Hindvani', 'http://capeant.antfarm.co.za:8000/Hindvani', rmain, get_pid, 'www', get_auto, set_auto],
            ['Hot_91_9_FM', 'https://ice31.securenetsystems.net/HOT919?playSessionID=6BA86A5D-978A-CE95-E5FCD2BA152A9F00', rmain, get_pid, 'www', get_auto, set_auto],
            ['Ikwekwezi_FM', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/ff6c43748de44108a31d127b4b205c12/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            # ['IMPACT_RADIO', 'http://zas1.ndx.co.za/proxy/impactradio?mp=/stream', rmain, get_pid, 'www', get_auto, set_auto],
            ['Jacaranda_FM', 'https://edge.iono.fm/xice/jacarandafm_live_medium.aac', rmain, get_pid, 'www', get_auto, set_auto],
            ['Jozi_FM', 'http://capeant.antfarm.co.za:8000/JoziFM', rmain, get_pid, 'www', get_auto, set_auto],
            ['Kaya_FM', 'http://iceant.antfarm.co.za:8000/Kaya_MP3', rmain, get_pid, 'www', get_auto, set_auto],
            ['Kingfisher_FM', 'http://zas2.ndx.co.za/proxy/kingfisherfm?mp=/stream', rmain, get_pid, 'www', get_auto, set_auto],
            ['Lesedi_FM', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/273707ee34a94d87a51c4785b48256a5/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            ['Ligwalagwala_FM', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/568fc5738cce4434aa6db69e928084be/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            ['Lotus_FM', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/9d1c7019ff894e5191b954eff03d7c77/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            #['Lotus_FM', [0, '106.8M'], rmain, get_pid, 'dab', get_auto, set_auto],
            ['Metro_FM', 'https://proradiocloud.antfarm.co.za/ant-lre-sabc/30acd2358bc64be49d563b72f0d1d121/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            ['Mix_93_8_FM', 'http://50.7.77.114:8007/;', rmain, get_pid, 'www', get_auto, set_auto],
            ['Motsweding_FM', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/97f660b5d3c949e094ca1d8c983551d2/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            ['Munghana_FM', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/14e03c487fa44d3686ff65f483373d62/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            ['OFM', 'http://edge.iono.fm/xice/ofm_live_medium.mp3', rmain, get_pid, 'www', get_auto, set_auto],
            ['Phalaphala_FM', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/0e6fc9cfa7aa4264ad93f87dc4f75c3b/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            ['Power_FM', 'http://albert.antfarm.co.za:8000/PowerFM64k_BKP', rmain, get_pid, 'www', get_auto, set_auto],
            ['PRETORIA_FM', 'http://capeant.antfarm.co.za:8000/ptafm', rmain, get_pid, 'www', get_auto, set_auto],
            ['Radio_2000', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/a3d1e938cf9c49db874906a8138ecf10/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            ['Radio_aBr', 'http://20873.live.streamtheworld.com/AFRICABUSINESSRADIO_S01.mp3?tdsdk=js-2.9&pname=TDSdk&pversion=2.9&banners=none&sbmid=5986bfc2-741c-4dd0-a045-4ed9c00754fd', rmain, get_pid, 'www', get_auto, set_auto],
            ['Radio_Sonder_Grense', 'http://albert.antfarm.co.za:8000/RSG', rmain, get_pid, 'www', get_auto, set_auto],
            ['Radio_Today', 'http://radiotoday.ddns.net:8000/radio.mp3', rmain, get_pid, 'www', get_auto, set_auto],
            ['Radio_Tygerberg', 'http://radiotygerberg.highquality.radiostream.co.za/', rmain, get_pid, 'www', get_auto, set_auto],
            ['Radiowave', 'http://ice8.securenetsystems.net/967FM?playSessionID=6BF86BAD-EE45-8412-BAF6422EA13DEAA5', rmain, get_pid, 'www', get_auto, set_auto],
            ['Rise_FM', 'http://zas2.ndx.co.za/proxy/risefm?mp=/stream&1533914047229', rmain, get_pid, 'www', get_auto, set_auto],
            ['SAfm', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/620e01258f5b49568546ff239ff2a32f/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            # ['SAfm', [1, '105.1M'], rmain, get_pid, 'dab', get_auto, set_auto],
            ['Smile_90_4_FM', 'http://edge.iono.fm/xice/smile_live_medium.mp3', rmain, get_pid, 'www', get_auto, set_auto],
            ['Talk_Radio_702', 'http://20133.live.streamtheworld.com/FM702_SC', rmain, get_pid, 'www', get_auto, set_auto],
            ['Thobela_FM', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/58024f759ef343e5b43f99b0c55d84aa/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            ['TuksFM', 'https://edge.iono.fm/xice/tuksfm_live_medium.mp3', rmain, get_pid, 'www', get_auto, set_auto],
            ['UCT_Radio', 'https://edge.iono.fm/xice/uctradio_live_medium.aac?p=embed', rmain, get_pid, 'www', get_auto, set_auto],
            ['Ukhozi_FM', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/c04e80a90111477a88867b697e2203c0/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            ['Umhlobo_Wenene_FM', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/7844ef4be8164a66a0e21bdfe374bff5/playlist.m3u8', rmain, get_pid, 'www', get_auto, set_auto],
            ['Voice_of_the_Cape', 'http://edge.iono.fm/xice/voc_live_high.mp3', rmain, get_pid, 'www', get_auto, set_auto],
            ['Voice_of_Wits', 'http://146.141.76.196:8080/stream/live.mp3', rmain, get_pid, 'www', get_auto, set_auto],
            ['Wild_Coast_FM', 'http://91.109.4.193:8010/;', rmain, get_pid, 'www', get_auto, set_auto],
            ['YFM', 'http://node-05.strongradiohost.com/ahbatmbfpv5tv?rj-ttl=5&rj-token=AAABZSSHdcT8oxjvoPEluLP7TycxeODyiUX9Unko4spxzCwYx7nPVA', rmain, get_pid, 'www', get_auto, set_auto],
            # ['dab_test', [0, '98M'], rmain, get_pid, 'dab', get_auto, set_auto],
        ],
        'tv': [
            ['M_NET', 'udp://@225.0.1.101:1101', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['Vuzu', 'udp://@225.0.1.116:1116', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['kykNET', 'udp://@225.0.1.144:1144', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['Ignition', 'udp://@225.0.1.189:1189', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SABC_News', 'udp://@225.0.1.44:1404', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SABC1', 'udp://@225.0.1.191:1191', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SABC2', 'udp://@225.0.1.192:1192', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SABC3', 'udp://@225.0.1.193:1193', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['ETV', 'udp://@225.0.1.194:1194', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['Soweto_TV', 'udp://@225.0.1.251:1251', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SuperSport_1', 'udp://@225.0.1.201:1201', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SuperSport_2', 'udp://@225.0.1.202:1202', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SuperSport_3', 'udp://@225.0.1.203:1203', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SuperSport_4', 'udp://@225.0.1.204:1204', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SuperSport_5', 'udp://@225.0.1.205:1205', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SuperSport_6', 'udp://@225.0.1.206:1206', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SuperSport_7', 'udp://@225.0.1.207:1207', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SuperSport_8', 'udp://@225.0.1.208:1208', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['SuperSport_Blitz', 'udp://@225.0.1.200:1200', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['CNBC_Africa', 'udp://@225.0.1.41:1410', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['BusinessDay_TV', 'udp://@225.0.1.42:1412', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['BBC_World_News', 'udp://@225.0.1.40:1400', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['eNews_Channel_Africa', 'udp://@225.0.1.43:1403', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['Sky_News', 'udp://@225.0.1.45:1405', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['CNN_International', 'udp://@225.0.1.46:1401', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['BBC_Brit', 'udp://@225.0.1.120:1120', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['Mzansi_Magic', 'udp://@225.0.1.161:1161', tmain, get_pid, 'dstv', get_auto, set_auto],
            ['Parliament_SA', 'udp://@225.0.1.48:1408', tmain, get_pid, 'dstv', get_auto, set_auto]
        ]
    }

    return CMS_DICT


@app.route('/login')
def login():

    return render_template('login.html',
                           title='Novus recording system',
                           hostname=get_hostname())


@app.route('/logout')
def logout():

    return render_template('login.html',
                           title='Novus recording system',
                           hostname=get_hostname())


@app.route('/')
@login_required
def index():

    return render_template('index.html',
                           title='Novus recording system',
                           hostname=get_hostname(),
                           readme=readme())


@app.route('/info', methods=['GET', 'POST'])
@login_required
def info():

    if request.form.get('cwl'):
        clear_watcher_log()
    elif request.form.get('set_routes'):
        set_routes()
    elif request.form.get('watcher_start'):
        watcher_start()
    elif request.form.get('watcher_stop'):
        watcher_stop()

    CMS_DICT = content()
    radio = CMS_DICT['radio']
    tv = CMS_DICT['tv']

    du = disk_usage()
    mem = mem_usage()
    cpu = cpu_usage()
    ws = watcher_service
    radio_restart_stats = restart_stats(radio)
    tv_restart_stats = restart_stats(tv)

    return render_template('info.html',
                           title='Novus recording system',
                           hostname=get_hostname(),
                           radio=radio,
                           tv=tv,
                           mp3_running=mp3_running,
                           tv_running=mp4_running,
                           du=du,
                           mem=mem,
                           cpu=cpu,
                           ws=ws,
                           watcher_log=watcher_log,
                           encoder_check=encoder_check(),
                           du_clip_dir=du_clip_dir(),
                           du_unindexed_dir=du_unindexed_dir(),
                           get_routes=get_routes,
                           radio_restart_stats=radio_restart_stats,
                           tv_restart_stats=tv_restart_stats
           )

@app.route('/ps_list', methods=['GET', 'POST'])
@login_required
def ps_list():

    if request.method == 'POST':
        pid = request.form.get('ps_kill')
        ps_kill(pid)

    return render_template('ps_list.html', title='Novus recording system',
                           hostname=get_hostname(),
                           show_running_ps=show_running_ps,
                           mp3_running=mp3_running,
                           tv_running=mp4_running,
                           rcount_enabled=rcount_enabled,
                           tcount_enabled=tcount_enabled,
                           show_clips=show_clips,
                           show_clips_dab=show_clips_dab,
                           show_mnt=show_mnt
                           )


@app.route('/encoder')
@login_required
def encoder():

    return render_template('encoder.html', title='Novus recording system', hostname=get_hostname())


@app.route('/control_radio',  methods=['GET', 'POST'])
@login_required
def control_radio():

    CMS_DICT = content()
    radio = CMS_DICT['radio']

    if request.form.get('rstart_all'):
        rstart_all()
    elif request.form.get('kill_all'):
        kill_all()
    elif request.form.get('renable_all'):
        renable_all()
    elif request.form.get('rcd disable_all'):
        rdisable_all()

    for item in radio:
        item[2](item[0], item[1], item[4])
        item[6](item[0])

    return render_template('control_radio.html',
                           title='Novus recording system',
                           hostname=get_hostname(),
                           radio=radio,
                           running=mp3_running,
                           rcount_enabled=rcount_enabled)


@app.route('/control_television',  methods=['GET', 'POST'])
@login_required
def control_television():

    CMS_DICT = content()
    tv = CMS_DICT['tv']

    if request.form.get('tstart_all'):
        tstart_all()
    elif request.form.get('kill_all'):
        kill_all()
    elif request.form.get('tenable_all'):
        tenable_all()
    elif request.form.get('tdisable_all'):
        tdisable_all()

    for item in tv:
        item[2](item[0], item[1])
        item[6](item[0])

    return render_template('control_television.html',
                           title='Novus recording system',
                           hostname=get_hostname(),
                           tv=tv,
                           running=mp4_running,
                           tcount_enabled=tcount_enabled)


@app.route('/player')
@login_required
def player():

    CMS_DICT = content()
    tv = CMS_DICT['tv']

    return render_template('player.html',
                           title='Novus recording system',
                           hostname=get_hostname(),
                           find_mp4=find_mp4, tv=tv)


@app.route('/stream/<name>')
@login_required
def stream(name):

    def generate():

        i = random.randint(100, 500)
        num = i / 100
        sleep(num)

        if 'test_pattern.jpg' not in name:

            with open('clips/' + name, 'rb') as f:
                while True:
                    yield f.read()

        else:
            with open('test_pattern.mp4', 'rb') as f:
                while True:
                    yield f.read()

    return Response(generate(), mimetype='video/mp4', direct_passthrough=True)


@app.route('/audio_player')
@login_required
def audio_player():

    CMS_DICT = content()
    radio = CMS_DICT['radio']

    return render_template('audio_player.html',
                           title='Novus recording system',
                           hostname=get_hostname(),
                           radio=radio
                           )


@app.route('/shell')
@login_required
def shell():
    return render_template('shell.html',
                           title='Novus recording system',
                           hostname=get_hostname())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001, threaded=True)

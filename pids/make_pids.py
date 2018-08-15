

def rmain():
    pass

def tmain():
    pass

def get_pid():
    pass


CMS_DICT = {
    'radio': [
        ['1FM', 'http://5.153.107.45:2016/mp3_ultra', rmain, get_pid],
        ['5FM', 'http://albert.antfarm.co.za:8000/5fm', rmain, get_pid],
        ['94_7_Highveld_Stereo', 'http://19113.live.streamtheworld.com:3690/FM947_SC', rmain, get_pid],
        ['94_5_KFM', 'http://19993.live.streamtheworld.com/KFM_SC', rmain, get_pid],
        ['2OceansVibe', 'http://playerservices.streamtheworld.com/api/livestream-redirect/OCEANSVIBE_SC', rmain,
         get_pid],
        ['567_CapeTalk', 'http://19373.live.streamtheworld.com:3690/CAPE_TALK_SC', rmain, get_pid],
        ['99FM', 'http://ice31.securenetsystems.net/99FM?type=mp3', rmain, get_pid],
        ['Algoa_FM', 'https://edge.iono.fm/xice/54_medium.aac?p=embed', rmain, get_pid],
        ['BayFM', 'http://85.25.18.48/;.mp3', rmain, get_pid],
        ['Cape_Pulpit', 'http://albert.antfarm.co.za:8000/RadioPulpit', rmain, get_pid],
        ['Capricorn', 'http://albert.antfarm.co.za:8000/CapricornFM', rmain, get_pid],
        ['ChaiFM', 'http://listenlive-c2p1.ndstream.net:8060/;', rmain, get_pid],
        ['Channel_Africa',
         'http://proradiocloud.antfarm.co.za/ant-lre-sabc/557f47f80b264cea8e88346a123eedcd/playlist.m3u8?sid=0e728a7b-2ce4-44ba-b1d1-b64610a10547',
         rmain, get_pid],
        ['Classic_FM', 'https://edge.iono.fm/xice/49_medium.aac?p=embed', rmain, get_pid],
        ['CliffCentral_com', 'http://edge.iono.fm/xice/cliffcentral_live_medium.mp3', rmain, get_pid],
        ['East_Coast_Radio', 'http://edge.iono.fm/xice/ecr_live_medium.mp3', rmain, get_pid],
        ['Eldos_FM', 'http://core2.netdynamix.co.za:8100/;', rmain, get_pid],
        ['Fine_Music_Radio', 'http://edge.iono.fm/xice/fmr_live_medium.mp3?p=embed', rmain, get_pid],
        ['Fresh_FM',
         'http://ample-zeno-02.radiojar.com/2b729cqx73duv?rj-ttl=5&rj-token=AAABZTMPpQtBNgSGaINlnak7_XktOhkAJPzuWahBJlaZ6r70oYUqJQ',
         rmain, get_pid],
        ['Gagasi_FM', 'http://capeant.antfarm.co.za:8000/gagasi', rmain, get_pid],
        ['Good_Hope_FM', 'http://radiostream.co.za:9104/;', rmain, get_pid],
        ['Groot_FM', 'http://grootfm.highquality.radiostream.co.za/', rmain, get_pid],
        ['Heart_104_9_FM', 'http://capeant.antfarm.co.za:9000/HeartFM', rmain, get_pid],
        ['Hot_91_9_FM', 'https://ice31.securenetsystems.net/HOT919?playSessionID=6BA86A5D-978A-CE95-E5FCD2BA152A9F00',
         rmain, get_pid],
        ['Ikwekwezi_FM',
         'http://proradiocloud.antfarm.co.za/ant-lre-sabc/ff6c43748de44108a31d127b4b205c12/playlist.m3u8?sid=ec9213ca-5fb1-46fc-aee4-010f51a7b9a1',
         rmain, get_pid],
        ['IMPACT_RADIO', 'http://zas1.ndx.co.za/proxy/impactradio?mp=/stream', rmain, get_pid],
        ['Jacaranda_FM', 'https://edge.iono.fm/xice/jacarandafm_live_medium.aac', rmain, get_pid],
        ['Jozi_FM', 'http://capeant.antfarm.co.za:8000/JoziFM', rmain, get_pid],
        ['Kaya_FM', 'http://iceant.antfarm.co.za:8000/Kaya_MP3', rmain, get_pid],
        ['Lesedi_FM',
         'http://proradiocloud.antfarm.co.za/ant-lre-sabc/273707ee34a94d87a51c4785b48256a5/playlist.m3u8?sid=3626cb83-cc20-446d-af4a-9bd9b2e85cd8',
         rmain, get_pid],
        ['Ligwalagwala_FM',
         'http://proradiocloud.antfarm.co.za/ant-lre-sabc/568fc5738cce4434aa6db69e928084be/playlist.m3u8?sid=d68ad834-f7c8-4054-91c8-04eb5fc5988d',
         rmain, get_pid],
        ['Lotus_FM', 'http://proradiocloud.antfarm.co.za/ant-lre-sabc/9d1c7019ff894e5191b954eff03d7c77/playlist.m3u8',
         rmain, get_pid],
        ['Metro_FM', 'http://server21a.oneradiohost.com/4rrv3hw6bq5tv', rmain, get_pid],
        ['Mix_93_8_FM', 'http://50.7.77.114:8007/;', rmain, get_pid],
        ['Motsweding_FM',
         'http://proradiocloud.antfarm.co.za/ant-lre-sabc/97f660b5d3c949e094ca1d8c983551d2/playlist.m3u8?sid=b2268fb7-3931-451d-bd85-d45061df1d14',
         rmain, get_pid],
        ['Munghana_FM',
         'http://proradiocloud.antfarm.co.za/ant-lre-sabc/14e03c487fa44d3686ff65f483373d62/playlist.m3u8?sid=2994f2bb-84ce-4b91-bcb3-0ba391f4e232',
         rmain, get_pid],
        ['OFM', 'http://edge.iono.fm/xice/ofm_live_medium.mp3', rmain, get_pid],
        ['Phalaphala_FM',
         'http://proradiocloud.antfarm.co.za/ant-lre-sabc/0e6fc9cfa7aa4264ad93f87dc4f75c3b/playlist.m3u8?sid=1449b747-5c87-44fc-b32e-30b2e645cc10',
         rmain, get_pid],
        ['Power_FM', 'http://albert.antfarm.co.za:8000/PowerFM64k_BKP', rmain, get_pid],
        ['PRETORIA_FM', 'http://capeant.antfarm.co.za:8000/ptafm', rmain, get_pid],
        ['Radio_2000',
         'http://proradiocloud.antfarm.co.za/ant-lre-sabc/a3d1e938cf9c49db874906a8138ecf10/playlist.m3u8?sid=42174fcb-c143-46be-afb6-aa6a051bb5f6',
         rmain, get_pid],
        ['Radio_aBr',
         'http://20873.live.streamtheworld.com/AFRICABUSINESSRADIO_S01.mp3?tdsdk=js-2.9&pname=TDSdk&pversion=2.9&banners=none&sbmid=5986bfc2-741c-4dd0-a045-4ed9c00754fd',
         rmain, get_pid],
        ['Radio_Sonder_Grense', 'http://albert.antfarm.co.za:8000/RSG', rmain, get_pid],
        ['Radio_Today', 'http://162.244.80.118:5350/radiotoday', rmain, get_pid],
        ['Radio_Tygerberg', 'http://radiotygerberg.highquality.radiostream.co.za/', rmain, get_pid],
        ['Radiowave', 'http://ice8.securenetsystems.net/967FM?playSessionID=6BF86BAD-EE45-8412-BAF6422EA13DEAA5', rmain,
         get_pid],
        ['Rise_FM', 'http://zas2.ndx.co.za/proxy/risefm?mp=/stream&1533914047229', rmain, get_pid],
        ['SAfm',
         'http://proradiocloud.antfarm.co.za/ant-lre-sabc/620e01258f5b49568546ff239ff2a32f/playlist.m3u8?sid=6b1940eb-8142-48c2-96a4-2833da32c842',
         rmain, get_pid],
        ['Smile_90_4_FM', 'http://edge.iono.fm/xice/smile_live_medium.mp3', rmain, get_pid],
        ['Talk_Radio_702', 'http://20133.live.streamtheworld.com/FM702_SC', rmain, get_pid],
        ['Thobela_FM',
         'http://proradiocloud.antfarm.co.za/ant-lre-sabc/58024f759ef343e5b43f99b0c55d84aa/playlist.m3u8?sid=f8ec6d59-1cc4-4b2a-9cad-3aa292d950b1',
         rmain, get_pid],
        ['TuksFM', 'https://edge.iono.fm/xice/tuksfm_live_medium.mp3', rmain, get_pid],
        ['UCT_Radio', 'https://edge.iono.fm/xice/uctradio_live_medium.aac?p=embed', rmain, get_pid],
        ['Ukhozi_FM',
         'http://proradiocloud.antfarm.co.za/ant-lre-sabc/c04e80a90111477a88867b697e2203c0/playlist.m3u8?sid=74b0f5a0-e224-40eb-b34d-e5c2a4eb4526',
         rmain, get_pid],
        ['Umhlobo_Wenene_FM',
         'http://proradiocloud.antfarm.co.za/ant-lre-sabc/7844ef4be8164a66a0e21bdfe374bff5/playlist.m3u8?sid=04003ca0-d6d5-4606-aecd-29b686b592da',
         rmain, get_pid],
        ['Voice_of_the_Cape', 'http://edge.iono.fm/xice/voc_live_high.mp3', rmain, get_pid],
        ['Voice_of_Wits', 'http://146.141.76.196:8080/stream/live.mp3', rmain, get_pid],
        ['Wild_Coast_FM', 'http://91.109.4.193:8010/;', rmain, get_pid],
        ['YFM',
         'http://node-05.strongradiohost.com/ahbatmbfpv5tv?rj-ttl=5&rj-token=AAABZSSHdcT8oxjvoPEluLP7TycxeODyiUX9Unko4spxzCwYx7nPVA',
         rmain, get_pid]
    ],
    'tv': [
        ['M_NET', 'rtp://@225.0.1.101:1100', tmain, get_pid],
        ['Vuzu', 'rtp://@225.0.1.103:1200', tmain, get_pid],
        ['kykNET', 'rtp://@225.0.1.116:1100', tmain, get_pid],
        ['SABC_News', 'rtp://@225.0.1.40:1200', tmain, get_pid],
        ['SABC1', 'rtp://@225.0.1.189:1100', tmain, get_pid],
        ['SABC2', 'rtp://@225.0.1.191:1200', tmain, get_pid],
        ['SABC3', 'rtp://@225.0.1.192:1100', tmain, get_pid],
        ['Soweto_TV', 'rtp://@225.0.1.207:1100', tmain, get_pid],
        ['SuperSport_1', 'rtp://@225.0.1.194:1100', tmain, get_pid],
        ['SuperSport_2', 'rtp://@225.0.1.200:1200', tmain, get_pid],
        ['SuperSport_3', 'rtp://@225.0.1.201:1100', tmain, get_pid],
        ['SuperSport_4', 'rtp://@225.0.1.202:1200', tmain, get_pid],
        ['SuperSport_5', 'rtp://@225.0.1.203:1100', tmain, get_pid],
        ['SuperSport_6', 'rtp://@225.0.1.204:1200', tmain, get_pid],
        ['SuperSport_7', 'rtp://@225.0.1.205:1100', tmain, get_pid],
        ['SuperSport_8', 'rtp://@225.0.1.206:1200', tmain, get_pid],
        ['SuperSport_Blitz', 'rtp://@225.0.1.42:1100', tmain, get_pid]

    ]
}

'''
for item in CMS_DICT['radio']:

    with open(item[0] + '.pid', 'w') as f:
        f.write('none')
'''

for item in CMS_DICT['tv']:

    with open(item[0] + '.pid', 'w') as f:
        f.write('none')
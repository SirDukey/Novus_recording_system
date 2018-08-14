from flask import Flask, request, render_template, redirect, url_for, Response, flash, send_file
from flask_simplelogin import SimpleLogin, login_required

from app_94_7 import main_94_7
from app_5FM import main_5FM
from app_1FM import main_1FM
from app_2OceansVibe import main_2OceansVibe
from app_567_CapeTalk import main_567_CapeTalk
from app_94_5_KFM import main_94_5_KFM
from app_99FM import main_99FM

from app_MNET import main_MNET
from app_VUZU import main_VUZU
from app_KYKNET import main_Kyk_Net

app = Flask(__name__)

app.config['SIMPLELOGIN_USERNAME'] = 'admin'
app.config['SIMPLELOGIN_PASSWORD'] = 'global01a'
SECRET_KEY = 'oV8rgcvFY1YcEWo7jXmoPQi5gaeX1J'
app.config['SECRET_KEY'] = SECRET_KEY

SimpleLogin(app)


@app.route('/login')
def login():

    return render_template('login.html', title='Novus recording system')


@app.route('/logout')
def logout():

    return render_template('login.html', title='Novus recording system')


@app.route('/')
@login_required
def index():

    return render_template('index.html', title='Novus recording system')


@app.route('/control_radio',  methods=['GET', 'POST'])
@login_required
def control_radio():

    '''define the file.pid of each channel'''
    Highveld_pid = open('pids/94_7_Highveld_Stereo.pid', 'r')
    Highveld_status = Highveld_pid.read()
    Highveld_pid.close()

    FiveFM_pid = open('pids/5FM.pid', 'r')
    FiveFM_status = FiveFM_pid.read()
    FiveFM_pid.close()

    OneFM_pid = open('pids/1FM.pid', 'r')
    OneFM_status = OneFM_pid.read()
    OneFM_pid.close()

    TWOOceansVibe_pid = open('pids/2OceansVibe.pid', 'r')
    TWOOceansVibe_status = TWOOceansVibe_pid.read()
    TWOOceansVibe_pid.close()

    Five67_CapeTalk_pid = open('pids/567_CapeTalk.pid', 'r')
    Five67_CapeTalk_status = Five67_CapeTalk_pid.read()
    Five67_CapeTalk_pid.close()

    Ninety4_5_KFM_pid = open('pids/94_5_KFM.pid', 'r')
    Ninety4_5_KFM_status = Ninety4_5_KFM_pid.read()
    Ninety4_5_KFM_pid.close()

    Ninety9FM_pid = open('pids/99FM.pid', 'r')
    Ninety9FM_status = Ninety9FM_pid.read()
    Ninety9FM_pid.close()

    main_94_7()
    main_1FM()
    main_5FM()
    main_2OceansVibe()
    main_567_CapeTalk()
    main_94_5_KFM()
    main_99FM()

    return render_template('control_radio.html', title='Novus recording system',
                           Highveld_status=Highveld_status,
                           FiveFM_status=FiveFM_status,
                           OneFM_status=OneFM_status,
                           TWOOceansVibe_status=TWOOceansVibe_status,
                           Five67_CapeTalk_status=Five67_CapeTalk_status,
                           Ninety4_5_KFM_status=Ninety4_5_KFM_status,
                           Ninety9FM_status=Ninety9FM_status)


@app.route('/control_television',  methods=['GET', 'POST'])
@login_required
def control_television():

    '''define the file.pid of each channel'''
    MNET_pid = open('pids/MNET.pid', 'r')
    MNET_status = MNET_pid.read()
    MNET_pid.close()

    VUZU_pid = open('pids/VUZU.pid', 'r')
    VUZU_status = VUZU_pid.read()
    VUZU_pid.close()

    Kyk_Net_pid = open('pids/Kyk_Net.pid', 'r')
    Kyk_Net_status = Kyk_Net_pid.read()
    Kyk_Net_pid.close()

    main_MNET()
    main_VUZU()
    main_Kyk_Net()

    return render_template('control_television.html', title='Novus recording system',
                           MNET_status=MNET_status,
                           VUZU_status=VUZU_status,
                           Kyk_Net_status=Kyk_Net_status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)

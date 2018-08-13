from flask import Flask, request, render_template, redirect, url_for, Response, flash, send_file
from flask_simplelogin import SimpleLogin, login_required
from app_94_7 import main_94_7
from app_5FM import main_5FM
from app_1FM import main_1FM

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


    main_94_7()
    main_1FM()
    main_5FM()

    return render_template('control_radio.html', title='Novus recording system',
                           Highveld_status=Highveld_status,
                           FiveFM_status=FiveFM_status,
                           OneFM_status=OneFM_status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)

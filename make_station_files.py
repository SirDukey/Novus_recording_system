from app import content

CMS_DICT = content()


def rmain():
    pass


def tmain():
    pass


def get_pid():
    pass


def get_auto():
    pass


def set_auto():
    pass


for item in CMS_DICT['radio']:

    with open('timestamps/' + item[0] + '.ts', 'w') as f:
        if f:
            print('file exists')
        else:
            f.write('disabled')


for item in CMS_DICT['tv']:

    with open('timestamps/' + item[0] + '.ts', 'w') as f:
        if f:
            print('file exists')
        else:
            f.write('disabled')
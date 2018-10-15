from app import content

CMS_DICT = content()
radio = CMS_DICT['radio']
tv = CMS_DICT['tv']


def get_list(station):
    counter = 0
    for item in station:
        counter += 1
        print(counter, item[0])


if __name__ == '__main__':
    get_list(tv)
    print()
    get_list(radio)
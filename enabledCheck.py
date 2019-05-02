from app import content

CMS = content()
tv = CMS['tv']
status = 2

for c in tv:
    c = c[0]
    with open('/Novus_recording_system/auto/{}.auto'.format(c), 'r') as f:
        if f.read() == 'disabled':
            status = 0
        else:
            status = 1

if __name__ == '__main__':
    print(status)

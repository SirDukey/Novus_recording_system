def tail():
    with open('logs/watcher.log', 'r') as f:
        ll = f.read()
        ls = sorted(set(ll.split('\n')))
        for i in ls:
            print(i)
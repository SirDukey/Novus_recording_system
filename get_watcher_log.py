def tail():
    with open('logs/watcher.log', 'r') as f:
        l = f.read()
        ll = sorted(set(l.split('\n')))
        for i in ll[-20:]:
            #print(i)
            return i

def watcher_log():
    with open('logs/watcher.log', 'r') as f:
        ll = sorted(set(f.read().split('\n')))
        return ll

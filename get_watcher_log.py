import subprocess as sp


def watcher_log():
    with open('logs/watcher.log', 'r') as f:
        ll = sorted(set(f.read().split('\n')))
        return ll


def clear_watcher_log():
    sp.Popen(['truncate', '-s0', 'logs/watcher.log'])
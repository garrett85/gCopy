import os

def init_files():
    # setup application files/directories
    if not os.path.exists(os.path.expanduser('~') + '/.gCopy/dump'):
        os.makedirs(os.path.expanduser('~') + '/.gCopy/dump')
    if not os.path.exists(os.path.expanduser('~') + '/.gCopy/configs'):
        os.makedirs(os.path.expanduser('~') + '/.gCopy/configs')
import os

def list_dirs(path):
    return [os.path.join(path, file) for file in os.listdir(path)]

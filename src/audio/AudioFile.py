import os

def get_filepath(filename):
    dir = os.path.dirname(__file__)
    return os.path.join(dir, '../../audio', filename)

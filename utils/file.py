import shutil
import os


def rm_rf(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        if os.path.exists(path):
            os.remove(path)

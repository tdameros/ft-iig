import shutil
import os
import subprocess

from utils.colors import print_warning, print_success


def rm_rf(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        if os.path.exists(path):
            os.remove(path)


def run_norminette(path):
    norminette = subprocess.run(["norminette"], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, cwd=path)
    if norminette.returncode == 1:
        print_warning("NORMINETTE ERROR !")
        print(norminette.stdout.decode())
    else:
        print_success("Norminette OK")

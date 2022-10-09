import subprocess
from pathlib import Path
from colors import print_success, print_warning, print_info
import os
from orchestrators.libft import run_tests_libft
from utils import print_ascii, clear_console

GOINFRE_PATH = Path.home() / "goinfre/"
PATH = GOINFRE_PATH / "ft_iig/"
PROJECTS = {
    "LIBFT": run_tests_libft,
}


def run_git_clone():
    global PATH

    subprocess.run(["rm", "-fr", PATH])
    subprocess.run(["clear"])
    print_ascii()
    url_or_path = input("Enter repository URL or project PATH :")
    if os.path.exists(url_or_path):
        PATH = Path(url_or_path)
        return
    clone_process = subprocess.Popen(
        ["git", "clone", url_or_path, "ft_iig"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=GOINFRE_PATH)
    clone_process.wait()
    while clone_process.returncode != 0:
        url_or_path = input("Enter repository URL or project PATH :")
        if os.path.exists(url_or_path):
            PATH = Path(url_or_path)
            return
        clone_process = subprocess.Popen(
            ["git", "clone", url_or_path, "ft_iig"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=GOINFRE_PATH)
        clone_process.wait()


def run_norminette():
    norminette = subprocess.Popen(["norminette"], stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE, cwd=PATH)
    norminette.wait()
    if norminette.returncode == 1:
        print_warning("NORMINETTE ERROR !")
        out, err = norminette.communicate()
        print(out.decode())
    else:
        print_success("Norminette OK")


def get_goinfre_dir():
    if not os.path.isdir(GOINFRE_PATH):
        print_warning("GOINFRE directory not found.")
        local_goinfre = Path.cwd() / "goinfre"
        rm = subprocess.Popen(["rm", "-rf", local_goinfre])
        rm.wait()
        os.mkdir(local_goinfre)
        print_info("GOINFRE directory create in the current path.")
        return local_goinfre
    return GOINFRE_PATH


if __name__ == "__main__":
    clear_console()
    print_ascii()
    GOINFRE_PATH = get_goinfre_dir()
    PATH = GOINFRE_PATH / "ft_iig"
    print('\n' + '\n'.join([f"* - {project}" for project in PROJECTS.keys()]) + '\n')
    select_project = input("Select your project (name) :")
    while select_project not in PROJECTS:
        select_project = input("[INVALID] Select your project (name) :")
    run_git_clone()
    run_norminette()
    PROJECTS.get(select_project)(PATH)

import subprocess
import os
import logging
from pathlib import Path

import tests.libft
import tests.get_next_line
from utils.file import rm_rf
from utils.display import print_ascii, clear_console
from utils.colors import print_info, print_warning, print_success
from utils.git import git_clone

GOINFRE_PATH = Path.home() / "goinfre/"
PATH = GOINFRE_PATH / "ft_iig/"
PROJECTS = {
    "libft": tests.libft.run_tests,
    "get_next_line": tests.get_next_line.run_tests,
}

logging.basicConfig(level=logging.WARNING, format='%(asctime)s : %(message)s')


def is_valid_rendering_type(url_or_path):
    global PATH

    if os.path.exists(url_or_path):
        PATH = Path(url_or_path)
        return True
    rm_rf(PATH)
    if git_clone(url_or_path, GOINFRE_PATH) == 0:
        return True
    return False


def choose_rendering_type():
    global PATH

    clear_console()
    print_ascii()
    url_or_path = input("Enter repository URL or project PATH: ")
    while not is_valid_rendering_type(url_or_path):
        url_or_path = input("[INVALID] Enter repository URL or project PATH: ")
    return url_or_path


def get_goinfre_dir():
    if not os.path.isdir(GOINFRE_PATH):
        print_warning("GOINFRE directory not found.")
        local_goinfre = Path.cwd() / "goinfre"
        rm_rf(local_goinfre)
        os.mkdir(local_goinfre)
        print_info("GOINFRE directory create in the current path.")
        return local_goinfre
    return GOINFRE_PATH


if __name__ == "__main__":
    clear_console()
    print_ascii()
    GOINFRE_PATH = get_goinfre_dir()
    PATH = GOINFRE_PATH / "ft_iig"
    print('\n' + '\n'.join(
        [f"* - {project.upper()}" for project in PROJECTS.keys()]) + '\n')
    select_project = input("Select your project (name) :").lower()
    while select_project not in PROJECTS:
        select_project = input("[INVALID] Select your project (name):").lower()
    url_or_path = choose_rendering_type()
    PROJECTS.get(select_project)(PATH)
    retry = input("\nDo you want to relaunch tests? [Y/n] ")
    while retry.lower() in ["yes", "y", " y", "y "]:
        is_valid_rendering_type(url_or_path)
        clear_console()
        print_ascii()
        PROJECTS.get(select_project)(PATH)
        retry = input("\nDo you want to relaunch tests? [Y/n] ")

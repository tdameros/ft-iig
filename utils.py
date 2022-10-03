from re import sub
import subprocess
from turtle import st
from colors import print_success, print_warning

def compile(path, out_name, *args):
    gcc = subprocess.Popen(["gcc", "-Wall", "-Werror", "-Wextra", *args, "-o", out_name], cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    gcc.wait()
    if (gcc.returncode != 0):
        return 0
    return 1

def compile_rush(path, out_name):
    files = subprocess.Popen(["find", ".", "-name","*.c"], cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    files.wait()
    out, err = files.communicate()
    files = out.decode().split("\n")
    gcc = subprocess.Popen(["gcc", *files, "-Wall", "-Werror", "-Wextra", "-o", out_name], cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    gcc.wait()
    if (gcc.returncode != 0):
        return 0
    return 1

def copy(path_dest, path_file):
    cp = subprocess.Popen(["cp", path_file, path_dest])
    cp.wait()
    if (cp.returncode != 0):
        return 0
    return 1

def assert_equal(stdout, expected: str):
    return stdout == expected

def inject_argv(path, out_name,*args):
    run = subprocess.Popen([f"./{out_name}", *args], cwd=path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        run.wait(timeout=3)
    except subprocess.TimeoutExpired:
        return 999, "Time Out"
    out, err = run.communicate()
    if run.returncode != 0:
        return run.returncode, err.decode()
    return run.returncode, out.decode()

def display_result(function_prototype, return_code, user_std, test_std, assert_equal, display_nbr):
    if return_code == 999:
        print_warning(f"""KO : {function_prototype} => {test_std} | Votre résultat => TIME OUT""")
        return
    elif return_code == -11:
        print_warning(f"""KO : {function_prototype} => {test_std} | Votre résultat => SEGMENTATION FAULT""")
        return 
    elif return_code == -10:
        print_warning(f"""KO : {function_prototype} => {test_std} | Votre résultat => BUS ERROR""")
    if assert_equal and display_nbr < 10:
        print_success(f"""OK : {function_prototype} => {test_std} | Votre résultat => {user_std}""")
    elif not assert_equal:
        print_warning(f"""KO : {function_prototype} => {test_std} | Votre résultat => {user_std}""")

def display_result_rush(function_prototype, return_code, user_std, test_std, assert_equal, display_nbr):
    if return_code == 999:
        print_warning(f"""KO : {function_prototype} => \n{test_std}| Votre résultat => TIME OUT""")
        return
    elif return_code == -11:
        print_warning(f"""KO : {function_prototype} => \n{test_std}| Votre résultat => SEGMENTATION FAULT""")
        return 
    elif return_code == -10:
        print_warning(f"""KO : {function_prototype} => \n{test_std}| Votre résultat => BUS ERROR""")
    if assert_equal and display_nbr < 10:
        print_success(f"""OK : {function_prototype} => \n{test_std}| Votre résultat => \n{user_std}""")
    elif not assert_equal:
        print_warning(f"""KO : {function_prototype} => \n{test_std}| Votre résultat => \n{user_std}""")

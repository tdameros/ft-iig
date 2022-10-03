from re import sub
import subprocess
from turtle import st

import colors
from colors import print_success, print_warning
from terminaltables import DoubleTable


def print_ascii():
    print("""
  _  _ ___    __  __             _ _            _   _       
 | || |__ \  |  \/  |           | (_)          | | | |      
 | || |_ ) | | \  / | ___  _   _| |_ _ __   ___| |_| |_ ___ 
 |__   _/ /  | |\/| |/ _ \| | | | | | '_ \ / _ \ __| __/ _ \\
    | |/ /_  | |  | | (_) | |_| | | | | | |  __/ |_| ||  __/
    |_|____| |_|  |_|\___/ \__,_|_|_|_| |_|\___|\__|\__\___|


    """)


def clear_console():
    subprocess.run(["clear"])


def compile(out_name, *files):
    gcc = subprocess.Popen(
        ["gcc", "-Wall", "-Werror", "-Wextra", *files, "-o", out_name],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    gcc.wait()
    if gcc.returncode != 0:
        return 0
    return 1


def get_function_prototype(function_name, args):
    format_args = []
    for index, arg in enumerate(args):
        if isinstance(arg, str) and len(arg) <= 1:
            format_args.append(f"'{arg}'")
        elif isinstance(arg, str):
            format_args.append(f'"{arg}"')
        else:
            format_args.append(str(arg))
    function_prototype = f"{function_name}({', '.join(format_args)})"
    return function_prototype


def assert_equal(stdout, expected: str):
    return stdout == expected


def inject_argv(path_bin, *args, timeout=3):
    run = subprocess.Popen([path_bin, *args],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        run.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        return 999, "Time Out"
    out, err = run.communicate()
    if run.returncode != 0:
        return run.returncode, err.decode()
    return run.returncode, out.decode()


def get_format_row(function_prototype, return_code, output, expected,
                   assert_equal):
    validity = "KO"
    print(f"OUTPUT : {output}")
    if return_code == 999:
        output = "Time Out"
    elif return_code == -11:
        output = "Segmentation Fault"
    elif return_code == -10:
        output = "Bus Error"
    elif assert_equal:
        validity = "OK"
    row = [function_prototype, output, expected, validity]
    for index_column, column in enumerate(row):
        if return_code == 998:
            row[index_column] = colors.get_info_message(column)
        elif not assert_equal:
            row[index_column] = colors.get_warning_messsage(column)
        else:
            row[index_column] = colors.get_success_message(column)
    return row


def print_table(title, rows):
    table_instance = DoubleTable(rows, title)
    print(table_instance.table)

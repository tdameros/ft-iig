import os
from pathlib import Path

from utils.file import run_norminette, rm_rf
from utils.display import print_table
from utils.colors import print_info, get_color_row
from utils.format import get_format_row, get_status
from utils.compilation import compile, inject_argv

PROJECT_NAME = "get_next_line"


def run_tests(path):
    run_norminette(path)
    print_info("Testing...")
    mandatory_results = mandatory_tests(path)
    bonus_results = bonus_tests(path)
    if isinstance(mandatory_results, list):
        print_table(f" {PROJECT_NAME.upper()} SUMMARY ", mandatory_results)
    if isinstance(bonus_results, list):
        print_table(f" {PROJECT_NAME.upper()} BONUS ", bonus_results)


def mandatory_tests(path):
    test_functions = [gnl_buff_size_1, gnl_buff_size_3, gnl_buff_size_9999,
                      gnl_buff_size_10000000, gnl_invalid_fd
                      ]
    rows = [["Buffer Size", "File", "Call", "Status"]]
    for function in test_functions:
        test_results = function(path)
        rows += test_results
    rm_rf(path / ".bin_tests")
    return rows


def bonus_tests(path):
    test_functions = [gnl_bonus_buff_size_1, gnl_bonus_buff_size_9999,
                      gnl_bonus_buff_size_10000000,
                      gnl_invalid_fd
                      ]
    rows = [["Buffer Size", "Files", "Total Call", "Status"]]
    for function in test_functions:
        test_results = function(path)
        rows += test_results
    rm_rf(path / ".bin_tests")
    return rows


def test_exercise(path, template: str, files: list, tests_data: dict):
    path_template = Path.cwd() / "templates" / PROJECT_NAME / template
    files = [path / file for file in files]
    path_bin_tests_dir = path / ".bin_tests"
    path_bin = path_bin_tests_dir / template[:-2]
    buffer_size = tests_data[0].get("buffer_size")

    if not os.path.exists(path_bin_tests_dir):
        os.mkdir(path_bin_tests_dir)
    if not compile(path_bin, path_template, *files,
                   options=[f"-I{path}", "-D", f"BUFFER_SIZE={buffer_size}"]):
        return [get_color_row(
            [buffer_size, "ERROR", "ERROR", "Does not compile (with falgs)."],
            "red")]
    test_results = []
    for test in tests_data:
        arg_files = [Path.cwd() / "templates" / PROJECT_NAME / arg_file for
                     arg_file in test.get("files")]
        test_output = inject_argv(path_bin, *arg_files, test.get("call"))
        if len(arg_files) == 1:
            assert_value = test_output[1] == get_expected_result(arg_files[0],
                                                                 int(test.get(
                                                                     "call")))
        else:
            assert_value = test_output[1] == get_expected_bonus_result(
                arg_files, int(test.get("call")))
        status, result = get_status(test_output[0], test_output[1],
                                    assert_value)
        if status == "OK":
            row = get_color_row(
                [buffer_size, " ".join(test.get("files")), test.get("call"),
                 status], "green")
        else:
            row = get_color_row(
                [buffer_size, " ".join(test.get("files")), test.get("call"),
                 result], "red")
        test_results.append(row)
        if test_output[0] == 999:
            return test_results
    return test_results


def get_expected_result(file, call):
    try:
        with open(file, "r") as file:
            lines = file.readlines()
            if call <= len(lines):
                return "".join(lines[:call])
            else:
                for _ in range(call - len(lines)):
                    lines.append("(null)")
                return "".join(lines)
    except FileNotFoundError:
        return "(null)"


def get_line(file, line):
    try:
        with open(file, "r") as file:
            lines = file.readlines()
            if line > len(lines) - 1:
                return "(null)"
            else:
                return lines[line]
    except FileNotFoundError:
        return "(null)"


def get_expected_bonus_result(files, call):
    result = []
    index_file = 0
    index_call = 0
    index_line = 0
    while index_call < call:
        result.append(get_line(files[index_file], index_line))
        index_file += 1
        index_call += 1
        if index_file == len(files):
            index_file = 0
            index_line += 1
    return "".join(result)


def gnl_buff_size_1(path):
    tests = [
        {"buffer_size": "1", "files": ["empty_file"], "call": "2"},
        {"buffer_size": "1", "files": ["empty_lines"], "call": "5"},
        {"buffer_size": "1", "files": ["null_end"], "call": "12"},
        {"buffer_size": "1", "files": ["one_line"], "call": "1"},
        {"buffer_size": "1", "files": ["simple_file"], "call": "10"},
        {"buffer_size": "1", "files": ["variable_line_sizes"], "call": "7"},
    ]
    return test_exercise(path, "get_next_line.c",
                         ["get_next_line.c", "get_next_line_utils.c"], tests)


def gnl_buff_size_3(path):
    tests = [
        {"buffer_size": "3", "files": ["empty_file"], "call": "3"},
        {"buffer_size": "3", "files": ["empty_lines"], "call": "6"},
        {"buffer_size": "3", "files": ["null_end"], "call": "10"},
        {"buffer_size": "3", "files": ["one_line"], "call": "2"},
        {"buffer_size": "3", "files": ["simple_file"], "call": "8"},
        {"buffer_size": "3", "files": ["variable_line_sizes"], "call": "7"},
    ]
    return test_exercise(path, "get_next_line.c",
                         ["get_next_line.c", "get_next_line_utils.c"], tests)


def gnl_buff_size_9999(path):
    tests = [
        {"buffer_size": "9999", "files": ["empty_file"], "call": "6"},
        {"buffer_size": "9999", "files": ["empty_lines"], "call": "1"},
        {"buffer_size": "9999", "files": ["null_end"], "call": "13"},
        {"buffer_size": "9999", "files": ["one_line"], "call": "2"},
        {"buffer_size": "9999", "files": ["simple_file"], "call": "10"},
        {"buffer_size": "9999", "files": ["variable_line_sizes"], "call": "7"},
    ]
    return test_exercise(path, "get_next_line.c",
                         ["get_next_line.c", "get_next_line_utils.c"], tests)


def gnl_buff_size_10000000(path):
    tests = [
        {"buffer_size": "10000000", "files": ["empty_file"], "call": "3"},
        {"buffer_size": "10000000", "files": ["empty_lines"], "call": "6"},
        {"buffer_size": "10000000", "files": ["null_end"], "call": "10"},
        {"buffer_size": "10000000", "files": ["one_line"], "call": "2"},
        {"buffer_size": "10000000", "files": ["simple_file"], "call": "8"},
        {"buffer_size": "10000000", "files": ["variable_line_sizes"],
         "call": "7"},
    ]
    return test_exercise(path, "get_next_line.c",
                         ["get_next_line.c", "get_next_line_utils.c"], tests)


def gnl_invalid_fd(path):
    tests = [
        {"buffer_size": "10", "files": ["invalid_fd"], "call": "1"},

    ]
    return test_exercise(path, "get_next_line.c",
                         ["get_next_line.c", "get_next_line_utils.c"], tests)


def gnl_bonus_buff_size_1(path):
    tests = [
        {"buffer_size": "1", "files": ["empty_file", "fd_bonus"], "call": "10"},
        {"buffer_size": "1", "files": ["fd_bonus", "fd_bonus3"], "call": "15"},
        {"buffer_size": "1", "files": ["fd_bonus", "fd_bonus5"], "call": "2"},
        {"buffer_size": "1",
         "files": ["fd_bonus", "fd_bonus2", "fd_bonus3", "fd_bonus4"],
         "call": "30"},
        {"buffer_size": "1",
         "files": ["fd_bonus", "fd_bonus2", "fd_bonus3", "fd_bonus5"],
         "call": "50"},
        {"buffer_size": "1",
         "files": ["fd_bonus", "fd_bonus2", "fd_bonus3", "fd_bonus4",
                   "fd_bonus5"], "call": "10"},
    ]
    return test_exercise(path, "get_next_line_bonus.c",
                         ["get_next_line_bonus.c",
                          "get_next_line_utils_bonus.c"], tests)


def gnl_bonus_buff_size_9999(path):
    tests = [
        {"buffer_size": "9999", "files": ["empty_file", "fd_bonus"],
         "call": "10"},
        {"buffer_size": "9999", "files": ["fd_bonus", "fd_bonus3"],
         "call": "15"},
        {"buffer_size": "9999", "files": ["fd_bonus", "fd_bonus5"],
         "call": "2"},
        {"buffer_size": "9999",
         "files": ["fd_bonus", "fd_bonus2", "fd_bonus3", "fd_bonus4"],
         "call": "30"},
        {"buffer_size": "9999",
         "files": ["fd_bonus", "fd_bonus2", "fd_bonus3", "fd_bonus5"],
         "call": "50"},
        {"buffer_size": "9999",
         "files": ["fd_bonus", "fd_bonus2", "fd_bonus3", "fd_bonus4",
                   "fd_bonus5"], "call": "10"},
    ]
    return test_exercise(path, "get_next_line_bonus.c",
                         ["get_next_line_bonus.c",
                          "get_next_line_utils_bonus.c"], tests)


def gnl_bonus_buff_size_10000000(path):
    tests = [
        {"buffer_size": "10000000", "files": ["empty_file", "fd_bonus"],
         "call": "10"},
        {"buffer_size": "10000000", "files": ["fd_bonus", "fd_bonus3"],
         "call": "15"},
        {"buffer_size": "10000000", "files": ["fd_bonus", "fd_bonus5"],
         "call": "2"},
        {"buffer_size": "10000000",
         "files": ["fd_bonus", "fd_bonus2", "fd_bonus3", "fd_bonus4"],
         "call": "30"},
        {"buffer_size": "10000000",
         "files": ["fd_bonus", "fd_bonus2", "fd_bonus3", "fd_bonus5"],
         "call": "50"},
        {"buffer_size": "10000000",
         "files": ["fd_bonus", "fd_bonus2", "fd_bonus3", "fd_bonus4",
                   "fd_bonus5"], "call": "10"},
    ]
    return test_exercise(path, "get_next_line_bonus.c",
                         ["get_next_line_bonus.c",
                          "get_next_line_utils_bonus.c"], tests)

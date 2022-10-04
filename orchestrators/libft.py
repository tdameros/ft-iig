from pathlib import Path
from utils import compile, get_function_prototype, inject_argv, assert_equal, \
    get_format_row, print_table, make_re
import os

PROJECT_NAME = "libft"


def run_tests_libft(path):
    test_functions = [ft_isalpha,
                      ft_isdigit,
                      ft_isalnum,
                      ft_isascii,
                      ft_isprint,
                      ft_strlen,
                      ft_memset,
                      ft_bzero]
    rows = [["Test", "Your Result", "Expected Result", "Status"]]
    print("Compile libft.a")
    if not make_re(path):
        print("libft.a does not compile")
        return
    for function in test_functions:
        test_results = function(path)
        rows += test_results
    print_table(f" {PROJECT_NAME.upper()} SUMMARY ", rows)


def test_exercise(path, template: str, lib: str, tests_data: dict):
    path_template = Path.cwd() / "templates" / PROJECT_NAME / template
    path_lib = path / lib
    path_bin_tests_dir = path / ".bin_tests"
    path_bin = path_bin_tests_dir / template[:-2]
    test_results = []
    if not os.path.exists(path_bin_tests_dir):
        os.mkdir(path_bin_tests_dir)
    if not os.path.exists(path_lib):
        row = get_format_row(template[:-2], 998, "File not found", lib, False)
        test_results.append(row)
        return test_results
    if not compile(path_bin, path_template, path_lib):
        row = get_format_row(template, 1, "Does not compile (with flags)", "",
                             False)
        test_results.append(row)
        return test_results
    for test in tests_data:
        function_prototype = get_function_prototype(template[:-2], test.get("args"))
        test_output = inject_argv(path_bin, *(test.get("args")))
        assert_value = assert_equal(test_output[1], test.get("expected"))
        row = get_format_row(function_prototype, test_output[0], test_output[1],
                             test.get("expected"), assert_value)
        test_results.append(row)
        if test_output[0] == 999:
            return test_results
    return test_results


def ft_isalpha(path):
    tests = [
        {"args": ["R"], "expected": "1"},
        {"args": ["a"], "expected": "1"},
        {"args": ["5"], "expected": "0"},
        {"args": [" "], "expected": "0"},
        {"args": ["@"], "expected": "0"},
        {"args": ["\t"], "expected": "0"},
        {"args": ["~"], "expected": "0"},
        {"args": ["z"], "expected": "1"},
        {"args": ["A"], "expected": "1"},
        {"args": ["\\"], "expected": "0"},
    ]
    return test_exercise(path, "ft_isalpha.c", "libft.a", tests)


def ft_isdigit(path):
    tests = [
        {"args": ["d"], "expected": "0"},
        {"args": ["9"], "expected": "1"},
        {"args": ["0"], "expected": "1"},
        {"args": ["1"], "expected": "1"},
        {"args": ["2"], "expected": "1"},
        {"args": ["3"], "expected": "1"},
        {"args": ["%"], "expected": "0"},
        {"args": ["\t"], "expected": "0"},
        {"args": ["\n"], "expected": "0"},
        {"args": ["@"], "expected": "0"},
        {"args": ["\\"], "expected": "0"},
    ]
    return test_exercise(path, "ft_isdigit.c", "libft.a", tests)


def ft_isalnum(path):
    tests = [
        {"args": ["d"], "expected": "1"},
        {"args": ["9"], "expected": "1"},
        {"args": ["0"], "expected": "1"},
        {"args": ["1"], "expected": "1"},
        {"args": ["a"], "expected": "1"},
        {"args": ["]"], "expected": "0"},
        {"args": ["%"], "expected": "0"},
        {"args": ["Z"], "expected": "1"},
        {"args": ["\n"], "expected": "0"},
        {"args": ["@"], "expected": "0"},
        {"args": ["\\"], "expected": "0"},
    ]
    return test_exercise(path, "ft_isalnum.c", "libft.a", tests)


def ft_isascii(path):
    tests = [
        {"args": [-6], "expected": "0"},
        {"args": [0], "expected": "1"},
        {"args": [1], "expected": "1"},
        {"args": [15], "expected": "1"},
        {"args": [127], "expected": "1"},
        {"args": [128], "expected": "0"},
        {"args": [2147483647], "expected": "0"},
        {"args": [-2147483648], "expected": "0"},
        {"args": [32], "expected": "1"},
        {"args": [63], "expected": "1"},
        {"args": [92], "expected": "1"},
    ]
    return test_exercise(path, "ft_isascii.c", "libft.a", tests)

def ft_isprint(path):
    tests = [
        {"args": [0], "expected": "0"},
        {"args": [7], "expected": "0"},
        {"args": [35], "expected": "1"},
        {"args": [-2], "expected": "0"},
        {"args": [2147483647], "expected": "0"},
        {"args": [-2147483648], "expected": "0"},
        {"args": [1], "expected": "0"},
        {"args": [32], "expected": "1"},
        {"args": [126], "expected": "1"},
        {"args": [127], "expected": "0"},
        {"args": [92], "expected": "1"},
    ]
    return test_exercise(path, "ft_isprint.c", "libft.a", tests)

def ft_strlen(path):
    tests = [
        {"args": ["42"], "expected": "2"},
        {"args": ["network"], "expected": "7"},
        {"args": ["moulinette"], "expected": "10"},
        {"args": [""], "expected": "0"},
        {"args": [" "], "expected": "1"},
        {"args": ["jesuisundev.com"], "expected": "15"},
        {"args": ["Arthur Dent"], "expected": "11"},
        {"args": ["Générateur d'Improbabilité Infinie"], "expected": "37"},
        {"args": ["H2G2"], "expected": "4"},
        {"args": ["forty two"], "expected": "9"},
    ]
    return test_exercise(path, "ft_strlen.c", "libft.a", tests)

def ft_memset(path):
    tests = [
        {"args": ["string", "abcd", 97, 4], "expected": "aaaa"},
        {"args": ["int", 7, 255, 1], "expected": "255"},
        {"args": ["int", 4, 255, 4], "expected": "-1"},
        {"args": ["int", 144, 225, 3], "expected": "14803425"},
        {"args": ["float", 3.2, 200, 4], "expected": "-411206.250000"},
        {"args": ["string", "sunny", 0, 1], "expected": ""},
        {"args": ["string", "42", 0, 0], "expected": "42"},
        {"args": ["int", 322222221, 200, 4], "expected": "-926365496"},
        {"args": ["int", 3222, 1, 4], "expected": "16843009"},
        {"args": ["float", 42.42, 1, 1], "expected": "42.419926"},
    ]
    return test_exercise(path, "ft_memset.c", "libft.a", tests)


def ft_bzero(path):
    tests = [
        {"args": ["string", "aaaa", 0], "expected": "97|97|97|97|"},
        {"args": ["string", "aaaa", 3], "expected": "0|0|0|97|"},
        {"args": ["string", "42school", 6], "expected": "0|0|0|0|0|0|111|108|"},
        {"args": ["int", 17566546, 2], "expected": "0|0|12|1|"},
        {"args": ["int", 106, 0], "expected": "106|0|0|0|"},
        {"args": ["float", 106.425741, 2], "expected": "0|0|-44|66|"},
        {"args": ["float", 42.42, 4], "expected": "0|0|0|0|"},
        {"args": ["float", 42.3698, 1], "expected": "0|122|41|66|"},
        {"args": ["int", -87, 2], "expected": "0|0|-1|-1|"},
        {"args": ["int", -300, 1], "expected": "0|-2|-1|-1|"},
    ]
    return test_exercise(path, "ft_bzero.c", "libft.a", tests)
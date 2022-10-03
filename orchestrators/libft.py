from pathlib import Path
from utils import compile, get_function_prototype, inject_argv, assert_equal, \
    get_format_row, print_table
import os

PROJECT_NAME = "libft"


def run_tests_libft(path):
    test_functions = [test_isalpha, test_test]
    rows = [["Test", "Your Result", "Expected Result", "Status"]]
    for function in test_functions:
        test_results = function(path)
        rows += test_results
    print_table(f" {PROJECT_NAME.upper()} SUMMARY ", rows)


def test_exercise(path, file_name: str, tests_data: dict):
    path_template = Path.cwd() / "templates" / PROJECT_NAME / file_name
    path_file = path / file_name
    path_bin_tests_dir = path / "bin_tests"
    path_bin = path_bin_tests_dir / file_name[:-2]
    test_results = []
    if not os.path.exists(path_bin_tests_dir):
        os.mkdir(path_bin_tests_dir)
    if not os.path.exists(path_file):
        row = get_format_row(file_name, 998, "File not found", "", False)
        test_results.append(row)
        return test_results
    if not compile(path_bin, path_template, path_file):
        row = get_format_row(file_name, 1, "Does not compile (with flags)", "",
                             False)
        test_results.append(row)
        return test_results
    for test in tests_data:
        function_prototype = get_function_prototype(file_name[:-2], test.get("args"))
        test_output = inject_argv(path_bin, *(test.get("args")))
        assert_value = assert_equal(test_output[1], test.get("expected"))
        row = get_format_row(function_prototype, test_output[0], test_output[1],
                             test.get("expected"), assert_value)
        test_results.append(row)
        if test_output[0] == 999:
            return test_results
    return test_results


def test_isalpha(path):
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
    return test_exercise(path, "ft_isalpha.c", tests)

def test_test(path):
    tests = [
        {"args": ["R"], "expected": "1"},
        {"args": ["a"], "expected": "2"},
        {"args": ["5"], "expected": "0"},
    ]
    return test_exercise(path, "ft_test.c", tests)

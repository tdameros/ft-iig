from pathlib import Path
from utils import compile, copy, inject_argv, assert_equal, display_result, compile_rush, display_result_rush
from colors import print_warning, print_success, print_info
import os
from test_math import get_printable_ascii
from random import randint

# TESTS = [
#     {"args": ["test", "test"], "expected": "0"},
#     {"args": ["test", "test"]},
# ]

def run_test_rush01(path):
    tests = [
        {"args": ["wfwefewfewf"], "expected": "Error\n"},
        {"args": ["3 1 2 2 1 3 2 2 2 2 3 1 3 2 1 2"], "expected": "1 4 3 2\n3 2 4 1\n2 3 1 4\n4 1 2 3\n"},
        {"args": ["4 3 2 1 1 2 2 2 4 3 2 1 1 2 2 2"], "expected": "1 2 3 4\n2 3 4 1\n3 4 1 2\n4 1 2 3\n"},
        {"args": ["2 1 2 4 2 4 2 1 2 1 3 3 3 3 2 1"], "expected": "3 4 2 1\n4 3 1 2\n1 2 4 3\n2 1 3 4\n"},
        {"args": ["1 2 4 2 4 2 1 2 1 2 2 3 2 1 2 3"], "expected": "Error\n"},
        {"args": ["4 3 1 2 1 2 2 2 3 3 2 1 2 1 3 3"], "expected": "1 2 4 3\n2 3 1 4\n3 4 2 1\n4 1 3 2\n"},
        {"args": ["1 3 3 2 3 2 1 3 1 4 2 3 2 1 2 2"], "expected": "4 1 2 3\n1 2 3 4\n3 4 1 2\n2 3 4 1\n"},
        {"args": ["2 1 2 4 2 4 2 1 2 1 3 3 3 3 2 10000"], "expected": "Error\n"},
        {"args": ["2 3 2 1 1 2 3 3 2 3 2 1 1 2 3 3"], "expected": "3 1 2 4\n1 2 4 3\n2 4 3 1\n4 3 1 2\n"},
        {"args": ["2 2 2 1 2 1 3 4 3 3 1 2 1 2 3 3"], "expected": "2 3 1 4\n1 2 4 3\n4 1 3 2\n3 4 2 1\n"},
        {"args": ["2 2 1 3 1 2 3 2 2 2 3 1 2 2 1 3"], "expected": "3 2 4 1\n1 4 2 3\n2 1 3 4\n4 3 1 2\n"},
    ]
    test_exercise(path, "rush01.c", "00", tests)

def test_exercise(path, user_file: str, exercise_number: str, tests_data: dict):
    print(f"## Exercice {exercise_number}")
    test_file = f"test_{user_file[3:]}"
    path_dest = path / f"ex{exercise_number}"
    if not os.path.isdir(path_dest):
        print_info(f"Le rush n'a pas de dossier ex00")
        return 1
    if not compile_rush(path_dest, "user_out"):
            print_warning(f"Le rush ne compile pas avec les flags.")
            return 1
    for i, test in enumerate(tests_data):
        function_prototype = test.get("args")[0]
        if test.get("expected") is not None:
            user_std = inject_argv(path_dest, "user_out", *(test.get("args")))
            assert_value = assert_equal(user_std[1], test.get("expected"))
            display_result_rush(function_prototype, user_std[0], user_std[1], test.get("expected"), assert_value, i)
        else:
            user_std = inject_argv(path_dest, "user_out", *(test.get("args")))
            test_std = inject_argv(path_dest, "test_out", *(test.get("args")))
            assert_value = assert_equal(user_std[1], test_std[1])
            display_result(function_prototype, user_std[0], user_std[1], test_std[1], assert_value, i)
        if user_std[0] == 999:
            return
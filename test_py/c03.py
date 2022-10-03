from pathlib import Path
from utils import compile, copy, inject_argv, assert_equal, display_result
from colors import print_warning, print_success, print_info
import os
from test_math import get_printable_ascii
from random import randint

NUMBER_RANDOM_TESTS = 100

# TESTS = [
#     {"args": ["test", "test"], "expected": "0"},
#     {"args": ["test", "test"]},
# ]

def run_test_c03(path):
    test_strcmp(path)
    test_strncmp(path)
    test_strcat(path)
    test_strncat(path)
    test_strstr(path)
    test_strlcat(path)
    


def test_exercise(path, user_file: str, exercise_number: str, tests_data: dict):
    print(f"## Exercice {exercise_number}")
    test_file = f"test_{user_file[3:]}"
    path_dest = path / f"ex{exercise_number}"
    path_src = Path.cwd() / "test_c/c03" / test_file
    path_random = Path.cwd() / "test_c/c03/" / user_file[3:]
    if not os.path.isdir(path_dest):
        print_info(f"L'exercice {user_file} n'a pas été rendu")
        return 1
    copy(path_dest, path_src)
    if not compile(path_dest, "user_out", user_file, test_file):
            print_warning(f"L'exercice {user_file} ne compile pas avec les flags.")
            return 1
    copy(path_dest, path_random)
    compile(path_dest, "test_out", user_file[3:])
    
    for i, test in enumerate(tests_data):
        function_prototype = f"""{user_file[:-2]}({", ".join(['"' + arg + '"' if isinstance(arg, str) else str(arg) for arg in test.get("args")])})"""
        if test.get("expected") is not None:
            user_std = inject_argv(path_dest, "user_out", *(test.get("args")))
            assert_value = assert_equal(user_std[1], test.get("expected"))
            display_result(function_prototype, user_std[0], user_std[1], test.get("expected"), assert_value, i)
        else:
            user_std = inject_argv(path_dest, "user_out", *(test.get("args")))
            test_std = inject_argv(path_dest, "test_out", *(test.get("args")))
            assert_value = assert_equal(user_std[1], test_std[1])
            display_result(function_prototype, user_std[0], user_std[1], test_std[1], assert_value, i)
        if user_std[0] == 999:
            return



def test_strcmp(path):
    tests = [{"args": ["", ""]}]
    for _ in range(NUMBER_RANDOM_TESTS):
        s1 = get_printable_ascii(randint(0, 20))
        s2 = get_printable_ascii(randint(0, 20))
        test = {"args": [s1, s2]}
        tests.append(test)
    test_exercise(path, "ft_strcmp.c", "00", tests)

def test_strncmp(path):
    tests = []
    for _ in range(NUMBER_RANDOM_TESTS):
        s1 = get_printable_ascii(randint(0, 20))
        s2 = get_printable_ascii(randint(0, 20))
        n = str(randint(0, 20))
        test = {"args": [s1, s2, n]}
        tests.append(test)
    test_exercise(path, "ft_strncmp.c", "01", tests)

def test_strcat(path):
    tests = []
    for _ in range(NUMBER_RANDOM_TESTS):
        s1 = get_printable_ascii(randint(0, 20))
        s2 = get_printable_ascii(randint(0, 20))
        test = {"args": [s1, s2]}
        tests.append(test)
    test_exercise(path, "ft_strcat.c", "02", tests)


def test_strncat(path):
    tests = []
    for _ in range(NUMBER_RANDOM_TESTS):
        s1 = get_printable_ascii(randint(0, 20))
        s2 = get_printable_ascii(randint(0, 20))
        n = str(randint(0, 20))
        test = {"args": [s1, s2, n]}
        tests.append(test)
    test_exercise(path, "ft_strncat.c", "03", tests)

def test_strstr(path):
    tests = [
        {"args": ["haystack", "haystack"], "expected": "haystack"},
        {"args": ["fffhaystackffffw", "haystack"], "expected": "haystackffffw"},
        {"args": ["aaabbccc", "bc"], "expected": "bccc"}
    ]
    for _ in range(NUMBER_RANDOM_TESTS):
        haystack = get_printable_ascii(randint(0, 20))
        needle = get_printable_ascii(randint(0, 5))
        test = {"args": [haystack, needle]}
        tests.append(test)
    test_exercise(path, "ft_strstr.c", "04", tests)

def test_strlcat(path):
    tests = []
    for _ in range(NUMBER_RANDOM_TESTS):
        dest = get_printable_ascii(randint(0, 20))
        src = get_printable_ascii(randint(0, 20))
        dest_size = str(randint(0, 90))
        test = {"args": [dest, src, dest_size]}
        tests.append(test)
    test_exercise(path, "ft_strlcat.c", "05", tests)
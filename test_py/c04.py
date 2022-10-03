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

def run_test_c04(path):
    test_strlen(path)
    test_putstr(path)
    test_putnbr(path)
    test_atoi(path)
    test_putnbr_base(path)
    test_atoi_base(path)

def test_exercise(path, user_file: str, exercise_number: str, tests_data: dict):
    print(f"## Exercice {exercise_number}")
    test_file = f"test_{user_file[3:]}"
    path_dest = path / f"ex{exercise_number}"
    path_src = Path.cwd() / "test_c/c04" / test_file
    path_random = Path.cwd() / "test_c/c04/" / user_file[3:]
    if not os.path.isdir(path_dest):
        print_info(f"L'exercice {user_file} n'a pas été rendu")
        return 1
    copy(path_dest, path_src)
    if not compile(path_dest, "user_out", user_file, test_file):
            print_warning(f"L'exercice {user_file} ne compile pas avec les flags.")
            return 1
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

def test_strlen(path):
    tests = []
    for _ in range(NUMBER_RANDOM_TESTS):
        s = get_printable_ascii(randint(0, 20))
        test = {"args": [s], "expected": str(len(s))}
        tests.append(test)
    test_exercise(path, "ft_strlen.c", "00", tests)

def test_putstr(path):
    tests = []
    for _ in range(NUMBER_RANDOM_TESTS):
        s = get_printable_ascii(randint(0, 20))
        test = {"args": [s], "expected": s}
        tests.append(test)
    test_exercise(path, "ft_putstr.c", "01", tests)

def test_putnbr(path):
    tests = []
    for _ in range(NUMBER_RANDOM_TESTS):
        n = str(randint(-2147483648, 2147483647))
        test = {"args": [n], "expected": n}
        tests.append(test)
    test_exercise(path, "ft_putnbr.c", "02", tests)

def test_atoi(path):
    tests = [
        {"args": ["--999"], "expected": "999"},
        {"args": [""], "expected": "0"},
        {"args": ["+954236"], "expected": "954236"},
        {"args": [" -+954fff236"], "expected": "-954"},
        {"args": [" -+955555554fff236"], "expected": "-955555554"},
        {"args": [" -+5fff236"], "expected": "-5"},
        {"args": [" -+0fff236"], "expected": "0"},
        {"args": [" -------------+5fff5"], "expected": "-5"},
        {"args": [" --------++----+55555555fff5"], "expected": "55555555"},
        {"args": [" 2147483647fff5"], "expected": "2147483647"},
        {"args": [" --2147483647fdasdasdff45"], "expected": "2147483647"},
        {"args": [" -2147483648ff45"], "expected": "-2147483648"},
        {"args": ["+0"], "expected": "0"},
        {"args": [" \t\t\t+0"], "expected": "0"},
        {"args": [" \t\t\t+5555"], "expected": "5555"},
    ]
    test_exercise(path, "ft_atoi.c", "03", tests)

def test_putnbr_base(path):
    tests = [
        {"args": ["255", "01"], "expected": "11111111"},
        {"args": ["-556564", "0123"], "expected": "-2013320110"},
        {"args": ["-55656455", "0123456789"], "expected": "-55656455"},
        {"args": ["-0", "0123456789ABC"], "expected": "0"},
        {"args": ["-25555", "0123456789ABC"], "expected": "-B82A"},
        {"args": ["2147483647", "0123456789ABC"], "expected": "282BA4AAA"},
        {"args": ["251", "wasd"], "expected": "ddsd"},
        {"args": ["251", "wa+"], "expected": ""},
        {"args": ["255", "waaaa"], "expected": ""},
        {"args": ["6464", "0"], "expected": ""},
    ]
    test_exercise(path, "ft_putnbr_base.c", "04", tests)

def test_atoi_base(path):
    tests = [
        {"args": ["AA", "0123456789A"], "expected": "120"},
        {"args": ["-9", "0123456789A"], "expected": "-9"},
        {"args": ["    -A9", "0123456789A"], "expected": "-119"},
        {"args": ["    -1111111111wefwf", "01"], "expected": "-1023"},
        {"args": ["    -11111154111wefewf", "012345678"], "expected": "372306414"},
        {"args": ["    -------11111154111wefewfwef555", "0123456789ABC"], "expected": "977035022"},
        {"args": ["    -------1", "01234567889ABC"], "expected": "0"},
        {"args": ["+4444", "0123+5"], "expected": "0"},
        {"args": ["", ""], "expected": "0"},
        {"args": ["-2147483648", "0123456789"], "expected": "-2147483648"},
    ]
    test_exercise(path, "ft_atoi_base.c", "05", tests)
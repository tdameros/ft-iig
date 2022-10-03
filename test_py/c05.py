from nis import match
from pathlib import Path
from pprint import pprint
from tkinter import N
from utils import compile, copy, inject_argv, assert_equal, display_result
from colors import print_warning, print_success, print_info
import os
from test_math import get_printable_ascii
from random import randint
from math import factorial, sqrt

NUMBER_RANDOM_TESTS = 100

# TESTS = [
#     {"args": ["test", "test"], "expected": "0"},
#     {"args": ["test", "test"]},
# ]

def run_test_c05(path):
    test_iterative_factorial(path)
    test_recursive_factorial(path)
    ft_iterative_power(path)
    ft_recursive_power(path)
    test_fibonacci(path)
    test_sqrt(path)
    test_is_prime(path)
    test_find_next_prime(path)

def test_exercise(path, user_file: str, exercise_number: str, tests_data: dict):
    print(f"## Exercice {exercise_number}")
    test_file = f"test_{user_file[3:]}"
    path_dest = path / f"ex{exercise_number}"
    path_src = Path.cwd() / "test_c/c05" / test_file
    path_random = Path.cwd() / "test_c/c05/" / user_file[3:]
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

def test_iterative_factorial(path):
    tests = []
    for _ in range(NUMBER_RANDOM_TESTS):
        n = randint(-5, 12)
        if (n < 0):
            result = 0
        else:
            result = factorial(n)
        test = {"args": [str(n)], "expected": str(result)}
        tests.append(test)
    test_exercise(path, "ft_iterative_factorial.c", "00", tests)

def test_recursive_factorial(path):
    tests = []
    for _ in range(NUMBER_RANDOM_TESTS):
        n = randint(-5, 12)
        if (n < 0):
            result = 0
        else:
            result = factorial(n)
        test = {"args": [str(n)], "expected": str(result)}
        tests.append(test)
    test_exercise(path, "ft_recursive_factorial.c", "01", tests)

def ft_iterative_power(path):
    tests = []
    for _ in range(NUMBER_RANDOM_TESTS):
        n = randint(-5, 9)
        power = randint(-5, 9)
        if (power < 0):
            result = 0
        else:
            result = n**power
        test = {"args": [str(n), str(power)], "expected": str(result)}
        tests.append(test)
    test_exercise(path, "ft_iterative_power.c", "02", tests)

def ft_recursive_power(path):
    tests = []
    for _ in range(NUMBER_RANDOM_TESTS):
        n = randint(-5, 9)
        power = randint(-5, 9)
        if (power < 0):
            result = 0
        else:
            result = n**power
        test = {"args": [str(n), str(power)], "expected": str(result)}
        tests.append(test)
    test_exercise(path, "ft_recursive_power.c", "03", tests)

def fibonacci(index):
    n1 = 0
    n2 = 1
    if index == 0:
        return n1
    elif index == 1:
        return n2
    next = 0
    for i in range(2, index+1):
        next = n1 + n2
        n1 = n2
        n2 = next
    return next


def test_fibonacci(path):
    tests = []
    for _ in range(50):
        n = randint(-5, 42)
        if (n < 0):
            result = -1
        else:
            result = fibonacci(n)
        test = {"args": [str(n)], "expected": str(result)}
        tests.append(test)
    test_exercise(path, "ft_fibonacci.c", "04", tests)

def ft_sqrt(nb):
    if nb <= 0:
        return 0
    root = 1
    while (root * root <= nb):
        if (root * root == nb):
            return root
        root += 1
    return 0

def test_sqrt(path):
    tests = []
    for _ in range(NUMBER_RANDOM_TESTS + 200):
        n = randint(-2147483648, 2147483647)
        if (n < 0):
            result = 0
        else:
            result = ft_sqrt(n)
        test = {"args": [str(n)], "expected": str(result)}
        tests.append(test)
    test_exercise(path, "ft_sqrt.c", "05", tests)

def is_prime(n):
    if n <= 1:
        return 0
    for i in range(2, int(sqrt(n) + 1)):
        if (n % i) == 0:
            return 0
    return 1

def test_is_prime(path):
    tests = [
        {"args": ["1000018381"], "expected": "1"}
    ]
    for _ in range(NUMBER_RANDOM_TESTS + 200):
        n = randint(-5, 1000018381)
        result = is_prime(n)
        test = {"args": [str(n)], "expected": str(result)}
        tests.append(test)
    test_exercise(path, "ft_is_prime.c", "06", tests)

def find_next_prime(n):
    while (not is_prime(n)):
        n += 1
    return n

def test_find_next_prime(path):
    tests = [
        {"args": ["1000018382"], "expected": "1000018391"}
    ]
    for _ in range(NUMBER_RANDOM_TESTS + 200):
        n = randint(-1000000, 1000018381)
        result = find_next_prime(n)
        test = {"args": [str(n)], "expected": str(result)}
        tests.append(test)
    test_exercise(path, "ft_find_next_prime.c", "07", tests)
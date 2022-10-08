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
                      ft_bzero,
                      ft_memcpy,
                      ft_memmove,
                      ft_strlcpy,
                      ft_strlcat,
                      ft_toupper,
                      ft_tolower,
                      ft_strchr,
                      ft_strrchr,
                      ft_strncmp,
                      ft_memchr,
                      ft_memcmp,
                      ft_strnstr,
                      ft_atoi,
                      ft_calloc,
                      ft_strdup,
                      ft_substr,
                      ft_strjoin,
                      ft_strtrim]
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
        {"args": ["string", "abcd", 97, 4], "expected": "97|97|97|97|"},
        {"args": ["int", 7, 255, 1], "expected": "255|0|0|0|"},
        {"args": ["int", 4, 255, 4], "expected": "255|255|255|255|"},
        {"args": ["int", 144, 225, 3], "expected": "225|225|225|0|"},
        {"args": ["float", 3.2, 200, 4], "expected": "200|200|200|200|"},
        {"args": ["string", "sunny", 0, 1], "expected": "0|117|110|110|121|"},
        {"args": ["string", "42", 0, 0], "expected": "52|50|"},
        {"args": ["int", 322222221, 200, 4], "expected": "200|200|200|200|"},
        {"args": ["int", 3222, 1, 4], "expected": "1|1|1|1|"},
        {"args": ["float", 42.42, 1, 1], "expected": "1|174|41|66|"},
    ]
    return test_exercise(path, "ft_memset.c", "libft.a", tests)


def ft_bzero(path):
    tests = [
        {"args": ["string", "aaaa", 0], "expected": "97|97|97|97|"},
        {"args": ["string", "aaaa", 3], "expected": "0|0|0|97|"},
        {"args": ["string", "42school", 6], "expected": "0|0|0|0|0|0|111|108|"},
        {"args": ["int", 17566546, 2], "expected": "0|0|12|1|"},
        {"args": ["int", 106, 0], "expected": "106|0|0|0|"},
        {"args": ["float", 106.425741, 2], "expected": "0|0|212|66|"},
        {"args": ["float", 42.42, 4], "expected": "0|0|0|0|"},
        {"args": ["float", 42.3698, 1], "expected": "0|122|41|66|"},
        {"args": ["int", -87, 2], "expected": "0|0|255|255|"},
        {"args": ["int", -300, 1], "expected": "0|254|255|255|"},
    ]
    return test_exercise(path, "ft_bzero.c", "libft.a", tests)

def ft_memcpy(path):
    tests = [
        {"args": ["string", "12345", "hello world", 5], "expected": "104|101|108|108|111|"},
        {"args": ["string", "12", "42", 2], "expected": "52|50|"},
        {"args": ["string", "12345", "network", 0], "expected": "49|50|51|52|53|"},
        {"args": ["int", "1234", 2546, 4], "expected": "242|9|0|0|"},
        {"args": ["int", "1234", 10000005, 4], "expected": "133|150|152|0|"},
        {"args": ["int", "1234", 42424242, 2], "expected": "178|87|0|0|"},
        {"args": ["float", "1234", 4.54223, 4], "expected": "243|89|145|64|"},
        {"args": ["float", "1234", 4521.32, 2], "expected": "143|74|154|68|"},
        {"args": ["float", "1234", 123.123, 0], "expected": "0|64|154|68|"},
        {"args": ["int", "1234", -2458, 4], "expected": "102|246|255|255|"},

    ]
    return test_exercise(path, "ft_memcpy.c", "libft.a", tests)


def ft_memmove(path):
    tests = [
        {"args": ["string", "src++", "hello ", 5], "expected": "104|101|108|108|111|0|"},
        {"args": ["string", "1234", "42", 2], "expected": "52|50|"},
        {"args": ["string", "12345", "coucou", 5], "expected": "99|111|117|99|111|0|"},
        {"args": ["string", "src++", "bidule", 5], "expected": "98|105|100|117|108|0|"},
        {"args": ["string", "src++", "clang", 0], "expected": "108|97|110|103|0|"},
        {"args": ["int", "src++", 145552, 4], "expected": "144|56|2|0|"},
        {"args": ["int", "src++", 123456777, 2], "expected": "9|205|7|0|"},
        {"args": ["int", "1234", 14524, 4], "expected": "188|56|0|0|"},
        {"args": ["float", "src++", 254.3241, 4], "expected": "248|82|126|67|"},
        {"args": ["float", "src++", 42.42424, 0], "expected": "178|41|66|0|"},
    ]
    return test_exercise(path, "ft_memmove.c", "libft.a", tests)


def ft_strlcpy(path):
    tests = [
        {"args": ["dest", "42", 4], "expected": "42|2"},
        {"args": ["dest", "hello", 5], "expected": "hell|5"},
        {"args": ["dest", "chifoumi", 10], "expected": "chifoumi|8"},
        {"args": ["dest", "Obig", 5], "expected": "Obig|4"},
        {"args": ["dest", "pool", 1], "expected": "|4"},
        {"args": ["dest", "formula1", 3], "expected": "fo|8"},
        {"args": ["dest", "orange", 7], "expected": "orange|6"},
    ]
    return test_exercise(path, "ft_strlcpy.c", "libft.a", tests)


def ft_strlcat(path):
    tests = [
        {"args": ["hello ", "world", 20], "expected": "hello world|11"},
        {"args": ["hello", "world", 6], "expected": "hello|10"},
        {"args": ["42", "network", 10], "expected": "42network|9"},
        {"args": ["Linus", "-Torvald", 10], "expected": "Linus-Tor|13"},
        {"args": ["tdameros", "@student", 15], "expected": "tdameros@stude|16"},
        {"args": ["bidule", "", 100], "expected": "bidule|6"},
        {"args": ["palpatine", " le mechant", 0], "expected": "palpatine|11"},
        {"args": ["JWT Token", " 123", 20], "expected": "JWT Token 123|13"},
        {"args": ["", "Django", 10], "expected": "Django|6"},
        {"args": ["", "Php Nulll", 5], "expected": "Php |9"},
    ]
    return test_exercise(path, "ft_strlcat.c", "libft.a", tests)


def ft_toupper(path):
    tests = [
        {"args": ["C"], "expected": "C"},
        {"args": ["4"], "expected": "4"},
        {"args": ["c"], "expected": "C"},
        {"args": ["a"], "expected": "A"},
        {"args": ["z"], "expected": "Z"},
        {"args": ["Z"], "expected": "Z"},
        {"args": ["A"], "expected": "A"},
        {"args": ["%"], "expected": "%"},
        {"args": ["{"], "expected": "{"},
        {"args": ["@"], "expected": "@"},
        {"args": ["."], "expected": "."},

    ]
    return test_exercise(path, "ft_toupper.c", "libft.a", tests)


def ft_tolower(path):
    tests = [
        {"args": ["C"], "expected": "c"},
        {"args": ["4"], "expected": "4"},
        {"args": ["c"], "expected": "c"},
        {"args": ["a"], "expected": "a"},
        {"args": ["z"], "expected": "z"},
        {"args": ["Z"], "expected": "z"},
        {"args": ["A"], "expected": "a"},
        {"args": ["%"], "expected": "%"},
        {"args": ["{"], "expected": "{"},
        {"args": ["@"], "expected": "@"},
        {"args": ["."], "expected": "."},

    ]
    return test_exercise(path, "ft_tolower.c", "libft.a", tests)

def ft_strchr(path):
    tests = [
        {"args": ["Hello World", "W"], "expected": "World"},
        {"args": ["Hello World", "w"], "expected": "(null)"},
        {"args": ["42 network", "4"], "expected": "42 network"},
        {"args": ["Libft.a", "."], "expected": ".a"},
        {"args": ["abcdeffff", "f"], "expected": "ffff"},
        {"args": ["aabbaaa", "b"], "expected": "bbaaa"},
        {"args": ["string_test", "_"], "expected": "_test"},
        {"args": ["test", "="], "expected": "(null)"},
        {"args": ["habitation", "b"], "expected": "bitation"},
        {"args": ["marvin bot", " "], "expected": " bot"},
        {"args": ["IFTTD", "\n"], "expected": "(null)"},

    ]
    return test_exercise(path, "ft_strchr.c", "libft.a", tests)


def ft_strrchr(path):
    tests = [
        {"args": ["Hello World", "W"], "expected": "World"},
        {"args": ["Hello World", "w"], "expected": "(null)"},
        {"args": ["42 network", "4"], "expected": "42 network"},
        {"args": [".Libft.a", "."], "expected": ".a"},
        {"args": ["abcdeffff", "f"], "expected": "f"},
        {"args": ["aabbaaa", "b"], "expected": "baaa"},
        {"args": ["st_ring_test", "_"], "expected": "_test"},
        {"args": ["test", "="], "expected": "(null)"},
        {"args": ["rrbbr", "r"], "expected": "r"},
        {"args": ["marvin bot", " "], "expected": " bot"},
        {"args": ["IFTTD", "\n"], "expected": "(null)"},

    ]
    return test_exercise(path, "ft_strrchr.c", "libft.a", tests)

def ft_strncmp(path):
    tests = [
        {"args": ["Hello", "Hello", 5], "expected": "0"},
        {"args": ["42", "24", 2], "expected": "1"},
        {"args": ["marvinbot", "marvintop", 6], "expected": "0"},
        {"args": ["mario", "luigi", 0], "expected": "0"},
        {"args": ["lionel", "messi", 3], "expected": "-1"},
        {"args": ["espace", "tabulation", 4], "expected": "-1"},
        {"args": ["", "", 1], "expected": "0"},
        {"args": ["1", "5", 1], "expected": "-1"},
        {"args": ["lundi", "mardi", 5], "expected": "-1"},
        {"args": ["ft_gnl", "ft_printf", 4], "expected": "-1"},
        {"args": ["bleu", "jaune", 2], "expected": "-1"},

    ]
    return test_exercise(path, "ft_strncmp.c", "libft.a", tests)

def ft_memchr(path):
    tests = [
        {"args": ["string", "hello", 111, 5], "expected": "valid return ptr"},
        {"args": ["string", "marvin", 118, 6], "expected": "valid return ptr"},
        {"args": ["string", "42 network", 1, 2], "expected": "valid return ptr"},
        {"args": ["string", "42", 50, 1], "expected": "valid return ptr"},
        {"args": ["int", 125, 125, 4], "expected": "valid return ptr"},
        {"args": ["int", 105542, 156, 4], "expected": "valid return ptr"},
        {"args": ["int", 2147483647, 255, 4], "expected": "valid return ptr"},
        {"args": ["float", 0, 0, 4], "expected": "valid return ptr"},
        {"args": ["float", 423.4222, 106, 2], "expected": "valid return ptr"},
        {"args": ["float", 54477.52555, 255, 4], "expected": "valid return ptr"},

    ]
    return test_exercise(path, "ft_memchr.c", "libft.a", tests)

def ft_memcmp(path):
    tests = [
        {"args": ["string", "hello", "hola", 5], "expected": "-1"},
        {"args": ["string", "marvin", "marvin", 6], "expected": "0"},
        {"args": ["string", "42 network", " le 101 ", 2], "expected": "1"},
        {"args": ["string", "42", "41", 1], "expected": "0"},
        {"args": ["int", 125, 125, 4], "expected": "0"},
        {"args": ["int", 105542, 156, 4], "expected": "-1"},
        {"args": ["int", 2147483647, 255, 4], "expected": "1"},
        {"args": ["float", 0, 0, 4], "expected": "0"},
        {"args": ["float", 4.42, -423.4222, 4], "expected": "1"},
        {"args": ["float", 54477.52555, 255, 4], "expected": "1"},

    ]
    return test_exercise(path, "ft_memcmp.c", "libft.a", tests)


def ft_strnstr(path):
    tests = [
        {"args": ["marvin", "vin", 6], "expected": "vin"},
        {"args": ["marvin", "vin", 3], "expected": "(null)"},
        {"args": ["", "test", 10], "expected": "(null)"},
        {"args": ["test", "", 4], "expected": "test"},
        {"args": ["aaaabbbb", "abb", 8], "expected": "abbbb"},
        {"args": ["formula1", "mmula", 3], "expected": "(null)"},
        {"args": ["abcdeabcde", "abcde", 5], "expected": "abcdeabcde"},
        {"args": ["haystackhay", "hay", 10], "expected": "haystackhay"},
        {"args": ["aaaaaaaaaaabaaaaabc", "abc", 19], "expected": "abc"},
        {"args": ["42424242", "43", 200000], "expected": "(null)"},

    ]
    return test_exercise(path, "ft_strnstr.c", "libft.a", tests)


def ft_atoi(path):
    tests = [
        {"args": ["\t585"], "expected": "585"},
        {"args": ["\n\t-5547"], "expected": "-5547"},
        {"args": ["test123"], "expected": "0"},
        {"args": ["\r\t-655222test"], "expected": "-655222"},
        {"args": ["-    6587"], "expected": "0"},
        {"args": ["--123"], "expected": "0"},
        {"args": ["+123"], "expected": "123"},
        {"args": ["+2147483647"], "expected": "2147483647"},
        {"args": ["-2147483648"], "expected": "-2147483648"},
        {"args": ["-2147483647"], "expected": "-2147483647"},
    ]
    return test_exercise(path, "ft_atoi.c", "libft.a", tests)


def ft_calloc(path):
    tests = [
        {"args": [4, 3], "expected": "0|0|0|0|0|0|0|0|0|0|0|0|"},
        {"args": [0, 10], "expected": ""},
        {"args": [42, 0], "expected": ""},
        {"args": [1, 1], "expected": "0|"},
        {"args": [2, 3], "expected": "0|0|0|0|0|0|"},
        {"args": [5, 1], "expected": "0|0|0|0|0|"},
        {"args": [3, 3], "expected": "0|0|0|0|0|0|0|0|0|"},
    ]
    return test_exercise(path, "ft_calloc.c", "libft.a", tests)


def ft_strdup(path):
    tests = [
        {"args": ["test"], "expected": "test"},
        {"args": [""], "expected": ""},
        {"args": ["42 network"], "expected": "42 network"},
        {"args": ["marvin"], "expected": "marvin"},
        {"args": ["Hello World"], "expected": "Hello World"},
        {"args": ["R2D2"], "expected": "R2D2"},
    ]
    return test_exercise(path, "ft_strdup.c", "libft.a", tests)


def ft_substr(path):
    tests = [
        {"args": ["test", 0, 3], "expected": "tes"},
        {"args": ["marvin", 3, 1], "expected": "v"},
        {"args": ["42", 1, 10], "expected": "2"},
        {"args": ["Hello World", 6, 5], "expected": "World"},
        {"args": ["", 0, 0], "expected": ""},
        {"args": ["   ", 2, 5], "expected": " "},
        {"args": ["pool", 2, 0], "expected": ""},
        {"args": ["suavemente", 1, 7], "expected": "uavemen"},
        {"args": ["ft_truc", 5, 2], "expected": "uc"},
        {"args": ["python", 0, 3], "expected": "pyt"},
        {"args": ["linus torvald", 0, 6], "expected": "linus "},
    ]
    return test_exercise(path, "ft_substr.c", "libft.a", tests)


def ft_strjoin(path):
    tests = [
        {"args": ["hello", " world"], "expected": "hello world"},
        {"args": ["42", "network"], "expected": "42network"},
        {"args": ["", "test"], "expected": "test"},
        {"args": ["bidule", ""], "expected": "bidule"},
        {"args": ["", ""], "expected": ""},
        {"args": ["str-", "join"], "expected": "str-join"},
        {"args": ["goodm", "orning"], "expected": "goodmorning"},
    ]
    return test_exercise(path, "ft_strjoin.c", "libft.a", tests)

def ft_strtrim(path):
    tests = [
        {"args": ["  test  ", " "], "expected": "test"},
        {"args": ["         ", " "], "expected": ""},
        {"args": ["  marvin bot   ", " "], "expected": "marvin bot"},
        {"args": [" z42 networkzzz z z ", " z"], "expected": "42 network"},
        {"args": ["abcdeeedbcatabcddecb", "abcde"], "expected": "t"},
        {"args": ["42", ""], "expected": "42"},
        {"args": ["hello world", " lw"], "expected": "hello world"},
        {"args": ["", ""], "expected": ""},
    ]
    return test_exercise(path, "ft_strtrim.c", "libft.a", tests)
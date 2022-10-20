from utils.colors import get_success_message, get_info_message, \
    get_warning_messsage


def get_format_row(function_prototype, return_code, output, expected,
                   assert_equal):
    validity = "KO"
    if return_code == 999:
        output = "Time Out"
    elif return_code == -11:
        output = "Segmentation Fault"
    elif return_code == -10:
        output = "Bus Error"
    elif assert_equal:
        validity = "OK"
    if "AddressSanitizer" in output:
        output = "AddressSanitizer"
        validity = "KO"
    if "LeakSanitizer" in output:
        output = "LeakSanitizer"
        validity = "KO"
    row = [function_prototype, output, expected, validity]
    for index_column, column in enumerate(row):
        if return_code == 998:
            row[index_column] = get_info_message(column)
        elif validity == "KO":
            row[index_column] = get_warning_messsage(column)
        else:
            row[index_column] = get_success_message(column)
    return row


def get_status(return_code, output, assert_equal):
    if return_code == 999:
        return "KO", "Time Out"
    elif return_code == -11:
        return "KO", "Segmentation Fault"
    elif return_code == -10:
        return "KO", "Bus Error"
    elif "LeakSanitizer" in output:
        return "KO", "LeakSanitizer"
    elif "AddressSanitizer" in output:
        return "KO", "AddressSanitizer"
    elif assert_equal:
        return "OK", output
    return "KO", "Wrong result"


def remove_ok_tests(test_results):
    return [test for test in test_results if
            test[3] != get_success_message("OK")]


def remove_special_char(message: str):
    specials = ["\a", "\b", "\t", "\n", "\v", "\f", "\r"]
    replacements = ["\\a", "\\b", "\\t", "\\n", "\\v", "\\f", "\\r"]
    for char, replacement in zip(specials, replacements):
        message = message.replace(char, replacement)
    return message


def get_function_prototype(function_name, args):
    format_args = []
    for index, arg in enumerate(args):
        if isinstance(arg, str) and len(arg) <= 1:
            arg = remove_special_char(arg)
            format_args.append(f"'{arg}'")
        elif isinstance(arg, str):
            arg = remove_special_char(arg)
            format_args.append(f'"{arg}"')
        else:
            format_args.append(str(arg))
    function_prototype = f"{function_name}({', '.join(format_args)})"
    return function_prototype

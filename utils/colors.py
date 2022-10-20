class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_warning(message: str):
    print(bcolors.FAIL + message + bcolors.ENDC)


def print_success(message: str):
    print(bcolors.OKGREEN + message + bcolors.ENDC)


def print_info(message: str):
    print(bcolors.OKCYAN + message + bcolors.ENDC)


def get_warning_messsage(message: str):
    return bcolors.FAIL + message + bcolors.ENDC


def get_success_message(message: str):
    return bcolors.OKGREEN + message + bcolors.ENDC


def get_info_message(message: str):
    return bcolors.OKCYAN + message + bcolors.ENDC


def remove_colors(message: str):
    colors = [bcolors.OKGREEN,
              bcolors.FAIL,
              bcolors.OKCYAN,
              bcolors.ENDC]
    for color in colors:
        message = message.replace(color, "")
    return message


def get_color_row(row, color):
    for index_column, column in enumerate(row):
        if color == "blue":
            row[index_column] = get_info_message(column)
        elif color == "red":
            row[index_column] = get_warning_messsage(column)
        elif color == "green":
            row[index_column] = get_success_message(column)
    return row
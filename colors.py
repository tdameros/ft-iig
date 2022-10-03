
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
    print(bcolors.WARNING + message + bcolors.ENDC)

def print_success(message: str):
    print(bcolors.OKGREEN + message + bcolors.ENDC)

def print_info(message: str):
    print(bcolors.OKCYAN + message + bcolors.ENDC)
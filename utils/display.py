import os

from utils.colors import remove_colors
from terminaltables.other_tables import DoubleTable


def clear_console():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def print_center(message):
    for row in message.split("\n"):
        row_without_colors = remove_colors(row)
        try:
            white_spaces = [" " for _ in range(
                os.get_terminal_size().columns // 2 - len(
                    row_without_colors) // 2)]
        except:
            print("Run the program in other terminal")
            exit(1)
        white_spaces = "".join(white_spaces)
        print(white_spaces + row)


def print_ascii():
    ascii = """

    ██╗  ██╗██████╗      ██████╗ ███████╗███╗   ██╗███████╗██████╗ █████╗  ████████╗ ██████╗ ██████╗ 
    ██║  ██║╚════██╗    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    ███████║ █████╔╝    ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
    ╚════██║██╔═══╝     ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
         ██║███████╗    ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
         ╚═╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

    """
    print_center(ascii)


def print_table(title, rows):
    table_instance = DoubleTable(rows, title)
    print_center(table_instance.table)
import random, string
from random import randint

def initialize_random(length, args):
    return ("".join([args[randint(0, len(args) - 1)] for _ in range(length)]))

def get_random_letter(length):
    return (initialize_random(length, string.ascii_letters))

def get_random_digits(length):
    return (initialize_random(length, string.digits))

def get_random_symbol(length):
    return (initialize_random(length, string.ponctuation))

def get_printable_ascii(length):
    return (initialize_random(length, string.printable[:95]))

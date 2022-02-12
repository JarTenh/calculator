import re


def add(num_1, num_2):
    return num_1 + num_2

def substract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    if num_2 == 0:
        raise ZeroDivisionError
    result = str(num_1 / num_2)
    if re.search(r".0$", result):
        return int(result[:-2])
    return num_1 / num_2

def to_power(num_1, num_2):
    return num_1 ** num_2

def square_root(num_1, _):
    result = str(num_1 ** 0.5)
    if re.search(r".0$", result):
        return int(result[:-2])
    return float(result)

func_map = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
    "^": to_power,
    "\u221A": square_root
}
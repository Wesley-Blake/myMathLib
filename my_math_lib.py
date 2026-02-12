def add(*args) -> int:
    result = 0
    for i in args:
        result += i
    return result
def sub(*args) -> int:
    result = 0
    for i in args:
        result -= i
    return result
def mult(*args) -> int:
    result = 0
    for i in args:
        result *= i
    return result
def divide(*args) -> int:
    result = ""
    for index, value in enumerate(args):
        if index == 0:
            result = value
            continue
        result /= value
    return result

#!/usr/bin/python3
def safe_print_division(a, b):
    devision = None
    try:
        devision = a / b
        return devision
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(devision))

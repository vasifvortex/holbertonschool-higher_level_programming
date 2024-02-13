#!/usr/bin/python3
"""Documentation"""


def read_file(filename=""):
    """Read the File"""
    with open(filename, mode="r", encoding="utf-8") as my_file:
        text = my_file.read()
        print(text, end="")
        my_file.close()

#!/usr/bin/python3
"""Doc"""


def write_file(filename="", text=""):
    """Write"""
    with open(filename, mode="w", encoding="utf-8") as f:
        len = f.write(text)
        f.close()
    return len

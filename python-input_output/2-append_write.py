#!/usr/bin/python3
"""Doc"""


def append_write(filename="", text=""):
    """Append"""
    with open(filename, mode="a", encoding="utf-8") as f:
        len = f.write(text)
        f.close()
    return len

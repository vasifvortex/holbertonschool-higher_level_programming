#!/usr/bin/python3
"""text indent"""


def text_indentation(text):
    """Indent text based on delimiters"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = text
    for delimiter in "?:.":
        lines = result.split(delimiter)
        result = (delimiter + "\n\n").join([line.strip() for line in lines])

    print(result)

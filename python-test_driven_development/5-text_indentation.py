#!/usr/bin/python3
"""text indent"""


def text_indentation(text):
    """text indent"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = text
    for delimiter in "?:.":
        result = (delimiter + "\n\n").join(
            [index.strip() for index in result.split(delimiter)])

    return result

if __name__ == "__main__":
    import doctest
    result = text_indentation("Holberton School")
    print("Actual stdout:", result)
    print("Actual stdout length:", len(result))
    doctest.testfile("tests/5-text_indentation.txt")

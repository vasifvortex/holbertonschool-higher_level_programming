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

    print("Actual stdout:", result)
    return result

if __name__ == "__main__":
    import doctest
    text = "Holberton School"
    print("Desired stdout:", text)
    print("Desired stdout length:", len(text))
    
    result = text_indentation(text)
    print("Actual stdout length:", len(result))

    doctest.testfile("tests/5-text_indentation.txt")

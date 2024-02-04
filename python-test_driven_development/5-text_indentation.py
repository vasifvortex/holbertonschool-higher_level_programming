#!/usr/bin/python3
"""text indent"""


def text_indentation(text):
    """text indent"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delimeter in "?:.":
         text =(delimeter + "\n\n").join([index.strip(" ") for index in text.split(delimeter)])
         print(text)
         return(text)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

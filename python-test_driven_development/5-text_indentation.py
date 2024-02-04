#!/usr/bin/python3
"""text indent"""


def text_indentation(text):
    """text indent"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    #for delimeter in "?:.":
     #   words = delimeter.join(index.strip(" ") for index in words.split(delimeter))
        #(delimeter + "\n\n").join([index.strip(" ") for index in words.split(delimeter)])
    temp = text.split(" ")[0]+" "+text.split(" ")[1]
    print(temp)
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

#!/usr/bin/python3
"""Doc"""


baseRec = __import__("9-rectangle").Rectangle


class Square(baseRec):
    """Square Class"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

#!/usr/bin/python3
"""documentation"""


class Square:
    """Square class with private attribute size"""
    def __init__(self, size=0) -> None:
        """Initialize Square with size attribute"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method return Size
        """
        return self.__size ** 2

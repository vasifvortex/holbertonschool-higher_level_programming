#!/usr/bin/python3                                                                                    """Documentation"""
"Documentation"


class Square:
    """Square Class"""
    def __init__(self, size=0) -> None:
        """
        Initializes a new Square instance.

        Args:
        size (int): The size of a side of the square.
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public instance method that return square area.
        """
        return self.__size**2

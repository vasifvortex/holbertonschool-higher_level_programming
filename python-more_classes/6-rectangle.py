!/usr/bin/python3
"""Documentation"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        Rectangle.number_of_instances += 1
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Find the Rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """find perimeter of Rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self) -> str:
        con = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(0, self.__height):
            con += "#" * self.__width
            con += "\n"
        con = con[0:-1]
        return con

    def __repr__(self) -> str:
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

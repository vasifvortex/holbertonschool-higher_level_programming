#!/usr/bin/python3
"""Doc"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        chosen = {}
        if attrs is not None and all(isinstance(s, str) for s in attrs):
            for key in attrs:
                if key in self.__dict__:
                    chosen.update({key: self.__dict__[key]})
            return chosen
        else:
            return self.__dict__

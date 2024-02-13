#!/usr/bin/python3
"""Doc"""


import json


def load_from_json_file(filename):
    """function that creates an Object"""
    with open(filename, mode="r") as f:
        return json.load(f)

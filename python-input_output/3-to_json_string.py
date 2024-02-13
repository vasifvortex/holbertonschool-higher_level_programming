#!/usr/bin/python3
"""Doc"""


import json


def to_json_string(my_obj):
    """to Json str"""
    json_object = json.dumps(my_obj)
    return json_object

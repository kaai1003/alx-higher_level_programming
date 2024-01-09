#!/usr/bin/python3
"""JSON repr Module"""

import json

def from_json_string(my_str):
    """return json representation"""

    return json.dumps(my_str)
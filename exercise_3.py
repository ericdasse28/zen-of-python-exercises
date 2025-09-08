"""Errors should never pass silently
Unless explicitly silenced

Make the following function robust:
1. Handle missing files
2. Handle invalid JSON
3. Log or raise meaningful errors
"""

import json


def load_json(path):
    with open(path) as f:
        return json.load(f)
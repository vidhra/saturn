# Placeholder for utility functions

import json


def print_json(data, indent=2):
    """Prints JSON data with indentation for readability."""
    print(json.dumps(data, indent=indent)) 
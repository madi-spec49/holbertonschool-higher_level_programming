#!/usr/bin/env python3
"""Basic serialization module that adds the functionality to serialize a
Python dictionary to a JSON file and deserialize the JSON file to recreate
the Python Dictionary."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): A Python Dictionary with data to serialize
        filename (str): The filename of the output JSON file.
                       If the output file already exists it should be replaced.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file to a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python Dictionary with the deserialized JSON data from the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
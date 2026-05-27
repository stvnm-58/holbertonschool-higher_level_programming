#!/usr/bin/env python3
"""Module for serializing and deserializing custom objects using pickle."""

import pickle


class CustomObject:
    """A custom class representing an individual profile."""

    def __init__(self, name, age, is_student):
        """Initialize the attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes with the exact requested format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a binary file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of CustomObject from a binary file."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (OSError, pickle.PickleError, AttributeError):
            return None

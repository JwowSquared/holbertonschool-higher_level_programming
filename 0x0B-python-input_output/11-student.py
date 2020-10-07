#!/usr/bin/python3
"""x"""
import json


class Student:
    """x"""
    def __init__(self, first_name, last_name, age):
        """x"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """x"""
        return self.__dict__

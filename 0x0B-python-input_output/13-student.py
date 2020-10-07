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

    def to_json(self, attrs=None):
        """x"""
        if type(attrs) is not list or len(attrs) < 1:
            return self.__dict__
        for e in attrs:
            if type(e) is not str:
                return self.__dict__
        out = {}
        for key in attrs:
            if key in self.__dict__:
                out.update({key: self.__dict__[key]})
        return out

    def reload_from_json(self, json):
        """x"""
        for k, v in json.items():
            setattr(self, k, v)

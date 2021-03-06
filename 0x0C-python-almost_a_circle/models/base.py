#!/usr/bin/python3
"""This module holds the Base class that Rectangle and Square inherit from"""
import json


class Base:
    """Base class that handles I/O and id"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a list of dictionaries to a string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """converts a string to a list of dictionaries"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """converts objects into JSON and saves it to a file"""
        out = "[]"
        if list_objs is not None:
            d = []
            for o in list_objs:
                d.append(o.to_dictionary())
            out = Base.to_json_string(d)
        with open(cls.__name__ + ".json", "w") as f:
            f.write(out)

    @classmethod
    def load_from_file(cls):
        """returns a list of objects converted from a JSON file"""
        out = []
        try:
            with open(cls.__name__ + ".json", "r") as f:
                d = cls.from_json_string(f.read())
            for i in d:
                out.append(cls.create(**i))
        except:
            pass
        return out

    @classmethod
    def create(cls, **dictionary):
        """creates instances of rectangles or squares from a dictionary"""
        out = cls(1, 1)
        out.update(x=0, y=0)
        out.update(**dictionary)
        return out

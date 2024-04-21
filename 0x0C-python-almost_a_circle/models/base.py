#!/usr/bin/python3
"""
Defines a base model class.
"""
import json
import csv
import turtle


class Base:
    """
    Represents the base class model.
    Attributes:
        __nb_objects(int): number of instantiated bases - private attribute.
        id(int): object id - public attribute.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string
        representation of a list of dictionaries.
        """
        if not list_dictionaries or list_dictionaries is None:
            return"[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string
        representation of list_objs to a file.
        """
        ldicts = []
        if list_objs is not None:
            for obj in list_objs:
                save_dict = obj.to_dictionary()
                ldicts.append(save_dict)
            ldicts = Base.to_json_string(ldicts)
        else:
            ldicts = str(ldicts)

        with open(f"{cls.__name__}.json", mode='w', encoding='utf-8') as f:
            f.write(ldicts)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list
        of the JSON string representation.
        """
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance
        with all attributes already set.
        """
        r = cls.__name__
        if cls.__name__ == "Reactangle":
            r = cls.__mro__[0](1, 2)
            r.update(**dictionary)
        elif cls.__name__ == "Square":
            r = cls.__mro__[0](2)
            r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """
        Class method that returns a list of instances.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                ldicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in ldicts]
        except IOError:
                return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        for shapes in list_rectangles:
            T = turtle.Turtle()
            T.pencolor("green")
            T.up()
            T.goto(shapes.x, shapes.y)
            T.down()
            T.forward(shapes.width)
            T.left(90)
            T.forward(shapes.height)
            T.left(90)
            T.forward(shapes.width)
            T.left(90)
            T.forward(shapes.height)
            sleep(0.5)
            T.clear()
        for shapes in list_squares:
            T = turtle.Turtle()
            T.pencolor("orange")
            T.up()
            T.goto(shapes.x, shapes.y)
            T.down()
            T.forward(shapes.width)
            T.left(90)
            T.forward(shapes.height)
            T.left(90)
            T.forward(shapes.width)
            T.left(90)
            T.forward(shapes.height)
            sleep(0.5)
            T.clear()
        turtle.done()

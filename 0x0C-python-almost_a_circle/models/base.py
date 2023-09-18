#!/usr/bin/python3
"""
This module defines the Base class.
"""

import json
import csv
import turtle


class Base:
    """
    Base class for managing the id attribute in all classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int, optional): Identifier for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            cls: The class itself.
            list_objs (list): A list of instances that inherit from Base.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as file:
            obj_dicts = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(obj_dicts)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries from a JSON string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: List of dictionaries parsed from the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with all attributes set based
        on the provided dictionary.

        Args:
            cls: The class itself.
            **dictionary: Dictionary containing attribute values.

        Returns:
            object: An instance of the class with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances based on the JSON file.

        Returns:
            list: List of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_str = file.read()
                obj_dicts = cls.from_json_string(json_str)
                return [cls.create(**obj) for obj in obj_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the CSV representation of list_objs to a file.

        Args:
            cls: The class itself.
            list_objs (list): A list of instances that inherit from Base.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y]
                    )
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances based on the CSV file.

        Returns:
            list: List of instances loaded from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                obj_list = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(
                            int(row[1]), int(row[2]), int(row[3]),
                            int(row[4]), int(row[0])
                        )
                    elif cls.__name__ == "Square":
                        obj = cls(
                            int(row[1]), int(row[2]), int(row[3]), int(row[0])
                        )
                    obj_list.append(obj)
                return obj_list
        except FileNotFoundError:
            return []
        
    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares using Turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.

        Returns:
            None
        """
        window = turtle.Screen()
        window.bgcolor("white")

        pen = turtle.Turtle()
        pen.shape("turtle")
        pen.speed(1)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.color("blue")
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)
            pen.penup()

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)
            pen.penup()

        window.exitonclick()

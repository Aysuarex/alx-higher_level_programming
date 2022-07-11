#!/usr/bin/python3
"""
Module base
"""
import json
import csv
import turtle
import random


class Base:
    """class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ check inputs """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ check inputs """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ check inputs """
        with open(cls.__name__ + ".json", mode="w") as j_file:
            if list_objs is not None:
                list_dict = [item.to_dictionary() for item in list_objs]
                j_file.write(cls.to_json_string(list_dict))
            else:
                j_file.write(cls.to_json_string([]))

    @staticmethod
    def from_json_string(json_string):
        """ check inputs """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ check inputs """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ check inputs """
        try:
            with open(cls.__name__ + ".json", encoding="utf-8") as j_file:
                list_file = cls.from_json_string(j_file.read())
                return [cls.create(**obj) for obj in list_file]

        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ check inputs """
        with open(cls.__name__ + ".csv", mode="w") as f_csv:
            if list_objs is not None:
                values = ['id', 'width', 'height', 'size', 'x', 'y']
                list_dict = [item.to_dictionary() for item in list_objs]
                values_header = filter(lambda y: y in list_dict[0], values)
                writer = csv.DictWriter(f_csv, fieldnames=list(values_header))
                writer.writeheader()
                for line in list_dict:
                    writer.writerow(line)

    @classmethod
    def load_from_file_csv(cls):
        """ check inputs """
        try:
            with open(cls.__name__ + ".csv") as j_file:
                reader = csv.DictReader(j_file)
                list_dicts = []
                for row in reader:
                    for keys in row:
                        row[keys] = int(row[keys])
                    list_dicts.append(row)
                list_objs = [cls.create(**obj) for obj in list_dicts]
                return list_objs

        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ check inputs """
        win = turtle.Screen()
        win.bgcolor("lightgreen")
        cursor = turtle.Turtle()
        win.colormode(255)
        cursor.pensize(3)

        for shape in list_rectangles:
            colors = (random.randint(1, 255), random.randint(1, 255),
                      random.randint(1, 255))
            cursor.pencolor(colors)
            cursor.up()
            cursor.setx(shape.x)
            cursor.sety(shape.y)
            cursor.down()
            for i in range(2):
                cursor.forward(shape.width)
                cursor.right(90)
                cursor.forward(shape.height)
                cursor.right(90)

        for shape in list_squares:
            colors = (random.randint(1, 255), random.randint(1, 255),
                      random.randint(1, 255))
            cursor.pencolor(colors)
            cursor.up()
            cursor.setx(shape.x)
            cursor.sety(shape.y)
            cursor.down()
            for i in range(4):
                cursor.forward(shape.size)
                cursor.right(90)

        win.exitonclick()

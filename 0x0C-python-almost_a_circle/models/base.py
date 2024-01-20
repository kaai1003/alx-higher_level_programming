#!/usr/bin/python3
"""Module Base Class"""
import json
import os
import sys
import csv


class Base:
    """Class Base

    Attributes:
        nb_objects (int) : private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id (int): base id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation
        Args:
            list_dictionaries : list ditionaries
        """
        if list_dictionaries:
            list_dict = []
            for dict in list_dictionaries:
                list_dict.append(dict)
            return json.dumps(list_dict)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file json repr

        Args:
            list_objs (object): list of objects
        """
        new_list = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for obj in list_objs:
                dict = obj.to_dictionary()
                new_list.append(dict)
        json_dict = cls.to_json_string(new_list)
        with open(filename, mode="w") as jsonfile:
            jsonfile.write(json_dict)

    @staticmethod
    def from_json_string(json_string):
        """load json string

        Args:
            json_string (list): list of json string
        """
        json_list = []
        if json_string:
            json_list = json.loads(json_string)
        return json_list

    @classmethod
    def create(cls, **dictionary):
        """create new instance based on dict

        Args:
            dictionary (dict): dictionary of attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances based on file
        """
        filename = cls.__name__ + ".json"
        list_inst = []
        if os.path.exists(filename):
            with open(filename, mode='r') as j:
                json_string = j.read()
                list_attr = cls.from_json_string(json_string)
                if list_attr:
                    for n in list_attr:
                        new_inst = cls.create(**n)
                        list_inst.append(new_inst)
        return list_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save object attributes to csv file

        Args:
            list_objs (object): list of class object
        """
        if cls.__name__ == "Rectangle":
            filename = "Rectangle.csv"
            obj_fields = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == "Square":
            filename = "Square.csv"
            obj_fields = ['id', 'size', 'x', 'y']
        with open(filename, mode='w') as csv_file:
            set_to_csv = csv.DictWriter(csv_file, fieldnames=obj_fields)
            set_to_csv.writeheader()
            if list_objs:
                for obj in list_objs:
                    obj_dict = obj.to_dictionary()
                    set_to_csv.writerow(obj_dict)

    @classmethod
    def load_from_file_csv(cls):
        """load attributes object from csv file"""
        filename = cls.__name__ + ".csv"
        list_obj = []
        if os.path.exists(filename):
            with open(filename, mode='r') as csv_file:
                obj_dict = csv.DictReader(csv_file, )
                for obj in obj_dict:
                    for key in obj:
                        obj[key] = int(obj[key])
                    new_obj = cls.create(**obj)
                    list_obj.append(new_obj)
        return list_obj

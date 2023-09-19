#!/usr/bin/python3
""" Unittest for Base """

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Unittest for Base
    """
    def test_id_int(self):
        """ Test integer id """
        b = Base(5)
        self.assertEqual(b.id, 5)
        b = Base(0)
        self.assertEqual(b.id, 0)
        b = Base(-3)
        self.assertEqual(b.id, -3)

    def test_id_incrementation(self):
        """ Test id incrementation """
        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(7)
        self.assertEqual(b.id, 7)
        b = Base(None)
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)

    def test_id_non_int(self):
        """ Test non integer id """
        b = Base("Hello")
        self.assertEqual(b.id, "Hello")
        b = Base('A')
        self.assertEqual(b.id, 'A')
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))
        b = Base({"id": 7, "name": "Betty"})
        self.assertEqual(b.id, {"id": 7, "name": "Betty"})
        b = Base(False)
        self.assertEqual(b.id, False)

    def test_id_error(self):
        """ Test error """
        with self.assertRaises(TypeError):
            b = Base(1, 2)
        with self.assertRaises(TypeError):
            b = Base(1, None)

    def test_rectangle_create(self):
        """ test rectangle creation """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_square_create(self):
        """ test square creation """
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_load_empty_file(self):
        """Tests for non existant and empty file"""
        if (os.path.exists("Rectangle.json") is True):
            os.remove("Rectangle.json")
        if (os.path.exists("Square.json") is True):
            os.remove("Square.json")
        if (os.path.exists("Base.json") is True):
            os.remove("Base.json")
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])
        os.mknod("Rectangle.json")
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])

    def test_load_rectangle(self):
        """Test for loading a list of rectangles"""
        rect_a = Rectangle(2, 4)
        rect_b = Rectangle(1, 1)
        rect_c = Rectangle(6, 6)
        my_list = [rect_a, rect_b, rect_c]
        Rectangle.save_to_file([rect_a, rect_b, rect_c])
        my_list_loaded = Rectangle.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(type(my_list_loaded[i]), type(my_list[i]))
            self.assertEqual(my_list[i].to_dictionary(),
                             my_list_loaded[i].to_dictionary())
        os.remove("Rectangle.json")

    def test_load_square(self):
        """ Test for loading a list of squares """
        rect_a = Square(2)
        rect_b = Square(1)
        rect_c = Square(6)
        my_list = [rect_a, rect_b, rect_c]
        Square.save_to_file([rect_a, rect_b, rect_c])
        my_list_loaded = Square.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(type(my_list_loaded[i]), type(my_list[i]))
            self.assertEqual(my_list[i].to_dictionary(),
                             my_list_loaded[i].to_dictionary())
        os.remove("Square.json")

    def test_extra_args(self):
        """Test calling the function with an additional argument"""
        with self.assertRaises(TypeError):
            Base.load_from_file("Hello")

    def test_creation_id(self):
        """
        Test value assignment
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(-5)
        b6 = Base(6.3)
        b7 = Base()
        b8 = Base(None)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, -5)
        self.assertEqual(b6.id, 6.3)
        self.assertEqual(b7.id, 4)
        self.assertEqual(b8.id, 5)

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

    def test_from_json_string(self):
        json_string = Base.from_json_string(None)
        self.assertEqual(json_string, [])


if __name__ == '__main__':
    unittest.main()

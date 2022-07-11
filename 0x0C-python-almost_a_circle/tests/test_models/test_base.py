#!/usr/bin/python3
""" doctest unittest """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import json
import pep8


class Testpep8(unittest.TestCase):
    def test_pep8(self):
        style = pep8.StyleGuide(quiet=True)
        file_rectagle = "models/rectangle.py"
        file_rectabgle_test = "tests/test_models/test_rectangle.py"
        file_base = "models/base.py"
        file_base_test = "tests/test_models/test_base.py"
        file_square = "models/square.py"
        file_square_test = "tests/test_models/test_square.py"
        check = style.check_files([file_rectagle, file_rectabgle_test,
                                  file_base, file_base_test, file_square,
                                  file_square_test])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestBase(unittest.TestCase):
    """ test """

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(-1)
        self.b4 = Base(12)
        self.b5 = Base("hola")
        self.b6 = Base(3.1)
        self.b7 = Base()

    def tearDown(self):
        pass

    def test_setid(self):
        self.assertEqual(self.b1.id, 7)

    def test_setid2(self):
        self.assertEqual(self.b2.id, 11)

    def test_setid3(self):
        self.assertEqual(self.b3.id, -1)

    def test_setid4(self):
        self.assertEqual(self.b4.id, 12)

    def test_setid5(self):
        self.assertEqual(self.b5.id, "hola")

    def test_setid6(self):
        self.assertEqual(self.b6.id, 3.1)

    def test_setid7(self):
        self.assertEqual(self.b7.id, 27)

    def test_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_json_string2(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        list_back = json.loads(json_dictionary)
        self.assertEqual(list_back, [dictionary])

if __name__ == '__main__':
    unittest.main()

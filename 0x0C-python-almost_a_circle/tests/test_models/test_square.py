#!/usr/bin/python3
"""
unittest
"""
from models.square import Square
import unittest
import sys
from io import StringIO


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.old_stdout = sys.stdout
        sys.stdout = self.mystdout = StringIO()

    def tearDown(self):
        sys.stdout = self.old_stdout

    def test_id_s(self):
        g1 = Square(7)
        self.assertEqual(g1.id, 135)

    def test_excep(self):
        with self.assertRaises(TypeError):
            Square("2")

    def test_excep2(self):
        with self.assertRaises(ValueError):
            r5 = Square(10)
            r5.width = - 10

    def test_excep3(self):
        with self.assertRaises(TypeError):
            r6 = Square(10, 2, 1)
            r6.x = {}

    def test_excep4(self):
        with self.assertRaises(ValueError):
            Square(10, 3, -1)

    def test_area(self):
        r7 = Square(3)
        self.assertEqual(r7.area(), 9)

    def test_display(self):
        r8 = Square(4)
        r8.display()
        self.assertEqual(self.mystdout.getvalue(), "####\n####\n####\n####\n")

    def test_display2(self):
        r8 = Square(1)
        r8.display()
        self.assertEqual(self.mystdout.getvalue(), "#\n")

    def test_display3(self):
        r8 = Square(3, 1, 1)
        r8.display()
        self.assertEqual(self.mystdout.getvalue(), "\n ###\n ###\n ###\n")

    def test_display4(self):
        r8 = Square(2, 1)
        r8.display()
        self.assertEqual(self.mystdout.getvalue(), " ##\n ##\n")

    def test_str(self):
        r8 = Square(4, 6, 1, 12)
        self.assertEqual(str(r8), "[Square] (12) 6/1 - 4")

    def test_str2(self):
        r9 = Square(5, 5, 1)
        self.assertEqual(str(r9), "[Square] ({:d}) 5/1 - 5".format(r9.id))

    def test_str3(self):
        r9 = Square(5, 5)
        self.assertEqual(str(r9), "[Square] ({:d}) 5/0 - 5".format(r9.id))

    def test_update(self):
        r10 = Square(10, 10, 10)
        self.assertEqual(str(r10), "[Square] ({:d}) 10/10 - 10".format(r10.id))

    def test_update2(self):
        r11 = Square(10, 10, 10)
        r11.update(89)
        self.assertEqual(str(r11), "[Square] (89) 10/10 - 10")

    def test_update3(self):
        r12 = Square(10, 10, 10, 10)
        r12.update(89, 2)
        self.assertEqual(str(r12), "[Square] (89) 10/10 - 2")

    def test_update4(self):
        r13 = Square(10, 10, 10, 10)
        r13.update(89, 2, 3)
        self.assertEqual(str(r13), "[Square] (89) 3/10 - 2")

    def test_update5(self):
        r14 = Square(10, 10, 10, 10)
        r14.update(89, 2, 3, 4)
        self.assertEqual(str(r14), "[Square] (89) 3/4 - 2")

    def test_update_args(self):
        r16 = Square(10, 10, 10)
        r16.update(size=1)
        self.assertEqual(str(r16), "[Square] ({:d}) 10/10 - 1".format(r16.id))

    def test_update_args2(self):
        r17 = Square(10, 10, 10)
        r17.update(size=1, x=2)
        self.assertEqual(str(r17), "[Square] ({:d}) 2/10 - 1".format(r17.id))

    def test_update_args3(self):
        r18 = Square(10, 10, 10, 10)
        r18.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(r18), "[Square] (89) 3/1 - 2")

    def test_update_args4(self):
        r17 = Square(10, 10, 10, 10)
        r17.update(x=1, size=2, y=3)
        self.assertEqual(str(r17), "[Square] ({:d}) 1/3 - 2".format(r17.id))

    def test_size(self):
        r18 = Square(5)
        r18.size = 10
        self.assertEqual(str(r18), "[Square] ({:d}) 0/0 - 10".format(r17.id))

    def test_size(self):
        with self.assertRaises(TypeError):
            r18 = Square(5)
            r18.size = "10"

    def test_to_dict(self):
        r1 = Square(10, 2, 1, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(type(r1_dictionary), dict)

    def test_to_dict2(self):
        r1 = Square(10, 2, 1, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})

    def test_to_dict3(self):
        r1 = Square(10, 2, 1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square(1, 1)
        r2.update(**r1_dictionary)
        self.assertFalse(r1 == r2)

if __name__ == '__main__':
    unittest.main()

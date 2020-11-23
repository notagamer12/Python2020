from points import *
import unittest

class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Point(1, 2)), "(1, 2)")
        self.assertEqual(repr(Point(1, 2)), "Point(1, 2)")

    def test_eq(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertTrue(Point(1, 2) != Point(3, 2))
        self.assertTrue(Point(1, 2) != Point(1, 3))
        self.assertTrue(Point(1, 2) != Point(4, 5))

    def test_ne(self):
        self.assertTrue(Point(1, 2) != Point(6, 7))
        self.assertTrue(Point(1, 2) != Point(1, 6))
        self.assertTrue(Point(1, 2) != Point(7, 2))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(2, 4), Point(3, 6))
        self.assertEqual(Point(1, 2) + Point(-3, -3), Point(-2, -1))
        self.assertEqual(Point(-1, -2) + Point(-3, -3), Point(-4, -5))

    def test_sub(self):
        self.assertEqual(Point(4, 2) - Point(2, 1), Point(2, 1))
        self.assertEqual(Point(2, 1) - Point(4, 2), Point(-2, -1))
        self.assertEqual(Point(4, 2) - Point(-2, -1), Point(6, 3))
        self.assertEqual(Point(-2, -1) - Point(-4, -2), Point(2, 1))

    def test_mul(self):
        self.assertEqual(Point(3, 2) * Point(4, 2), Point(12, 4))
        self.assertEqual(Point(-3, -2) * Point(4, -2), Point(-12, 4))
       

    def test_cross(self):
        self.assertEqual(Point(4, 2).cross(Point(6, 7)), 16)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)

    def tearDown(self): pass

if __name__ == "__main__":
    unittest.main()     # wszystkie testy

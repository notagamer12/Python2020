# Kod testujący moduł.

from times import *
import unittest


class TestTime(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Time(3661)), "01:01:01")
        self.assertEqual(repr(Time(3661)), "Time(3661)")

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))

    def test_cmp(self):
        self.assertTrue(Time(2) == Time(2))
        self.assertFalse(Time(2) == Time(3))
        self.assertTrue(Time(2) != Time(3))
        self.assertFalse(Time(2) != Time(2))
        self.assertTrue(Time(2) < Time(3))
        self.assertFalse(Time(4) < Time(3))
        self.assertTrue(Time(2) <= Time(3))
        self.assertFalse(Time(4) <= Time(3))
        self.assertTrue(Time(4) > Time(3))
        self.assertFalse(Time(2) > Time(3))
        self.assertTrue(Time(4) >= Time(3))
        self.assertFalse(Time(2) >= Time(3))

    def test_int(self):
        self.assertEqual(int(Time(60)), 60)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()  # wszystkie testy

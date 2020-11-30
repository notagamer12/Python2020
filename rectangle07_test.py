import unittest
from rectangles_07 import *

class TestRectangle(unittest.TestCase):
    
    def setUp(self): pass

    def test_print(self):      # test str() i repr()
        self.assertEqual(str(Rectangle(1, 2, 6, 4)), "[(1, 2), (6, 4)]")
        self.assertEqual(repr(Rectangle(1, 2, 6, 4)), "Rectangle(1, 2, 6, 4)")

    def test_cmp(self): #test __eq__ i __ne__
        self.assertTrue(Rectangle(1, 2, 6, 4) == Rectangle(1, 2, 6, 4))
        self.assertTrue(Rectangle(1, 2, 6, 4) != Rectangle(1, 2, 3, 4))
        
    def test_center(self):
        self.assertEqual(Rectangle(2, 2, 6, 4).center(), Point(4, 3))
        
    def test_move(self):
        self.assertEqual(Rectangle(1, 2, 6, 4).move(3, 4), Rectangle(4, 6, 9, 8))
        
    def test_intersection(self):
        #jest przecięcie
        self.assertEqual(Rectangle(1, 1, 6, 4).intersection(Rectangle(5, 2, 9, 5)), Rectangle(5, 2, 6, 4))
        #brak przecięcia
        self.assertEqual(Rectangle(1, 1, 6, 4).intersection(Rectangle(7, 2, 9, 5)), None)

    def test_cover(self):
        self.assertEqual(Rectangle(1, 1, 6, 4).cover(Rectangle(5, 2, 9, 5)), Rectangle(1, 1, 9, 5))

    def test_make4(self):
        self.assertEqual(Rectangle(5, 1, 9, 5).make4(), [Rectangle(5, 1, 7, 3), Rectangle(5, 3, 7, 5), Rectangle(7, 1, 9, 3), Rectangle(7, 3, 9, 5)])

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy


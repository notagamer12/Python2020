import unittest
from circles import *

class TestCircle(unittest.TestCase):
    
    def setUp(self): pass

    def test_repr(self):     
        self.assertEqual(repr(Circle(1, 2, 4)), "Circle(1, 2, 4)")

    def test_cmp(self):  #test __eq__ i __ne__
        self.assertTrue(Circle(1, 2, 4) == Circle(1, 2, 4))
        self.assertTrue(Circle(1, 2, 4) != Circle(1, 2, 3))
        
        
    def test_move(self):
        self.assertEqual(Circle(1, 2, 4).move(3, 4), Circle(4, 6, 4))
        

    def test_coverr(self):
        self.assertEqual(Circle(2, 2, 1).coverr(Circle(7, 5, 2)), Circle(5, 4, 5))


    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy


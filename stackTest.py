from stack import *
import unittest


class TestStack(unittest.TestCase):

    def setUp(self): pass
        

    def test_str(self):
        astack = Stack()
        for elem in [11, 12, 13, 14]:
            astack.push(elem)
        self.assertEqual(str(astack), '[11, 12, 13, 14, None, None, None, None, None, None]')

    def test_is_empty(self):
        astack = Stack()
        self.assertEqual(astack.is_empty(), True)

    def test_is_full(self):
        astack = Stack()
        self.assertEqual(astack.is_full(), False)

    def test_push(self):
        astack = Stack()
        with self.assertRaises(OverflowError):
            for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                astack.push(i)
        self.assertEqual(str(astack), "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")

    def test_pop(self):
        astack = Stack()
        with self.assertRaises(ValueError):
            astack.pop()
        for elem in [11, 12, 13, 14]:
            astack.push(elem)
        self.assertEqual(astack.pop(), 14)

    

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy

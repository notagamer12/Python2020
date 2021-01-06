from queues import *
import unittest


class TestQueue(unittest.TestCase):

    def setUp(self): pass
    
    
    def test_str(self):
        aqueue = Queues()
        for elem in [11, 12, 13, 14]:
            aqueue.put(elem)
        self.assertEqual(str(aqueue), '[11, 12, 13, 14, None, None]')
    
    
    def test_is_empty(self):
        aqueue = Queues()
        self.assertEqual(aqueue.is_empty(), True)
    
    def test_is_full(self):
        aqueue = Queues()
        self.assertEqual(aqueue.is_full(), False)
    
    def test_put(self):
        aqueue = Queues()
        with self.assertRaises(OverflowError):
            for i in [1, 2, 3, 4, 5, 6]:
                aqueue.put(i)
        self.assertEqual(str(aqueue), "[1, 2, 3, 4, 5, None]")
    
    def test_get(self):
        aqueue = Queues()
        with self.assertRaises(ValueError):
            aqueue.get()
        for i in [1, 2, 3, 4, 5]:
            aqueue.put(i)
        self.assertEqual(aqueue.get(), 1)
        self.assertEqual(str(aqueue), "[None, 2, 3, 4, 5, None]")

    
    
    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy

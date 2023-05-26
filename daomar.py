import unittest

def square(n):
    return n ** 2

class SquareTestCase(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(square(5), 25)
    
    def test_negative_number(self):
        self.assertEqual(square(-4), 16)
    
    def test_zero(self):
        self.assertEqual(square(0), 0)

if __name__ == '__main__':
    unittest.main()

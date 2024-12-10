import unittest

# Functions to test
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a % b

# Test class
class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(-1, -1), 0)
        self.assertEqual(sub(0, 5), -5)

    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 3), 0)

    def test_div(self):
        self.assertEqual(div(10, 3), 1)  # Remainder of 10 divided by 3
        self.assertEqual(div(4, 2), 0)   # Remainder of 4 divided by 2
        self.assertEqual(div(5, 5), 0)   # Remainder of 5 divided by 5

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)  # Testing division by zero for remainder

# Run the tests
if __name__ == '__main__':
    unittest.main()


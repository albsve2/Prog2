# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_multiply(self):
        print('\nTests multiply')
        self.assertEqual(multiply(2, 4), 8)
        self.assertEqual(multiply(5, 2), 10)
        self.assertEqual(multiply(1, 6), 6)
        self.assertEqual(multiply(9, 0), 0)


if __name__ == "__main__":
    unittest.main()

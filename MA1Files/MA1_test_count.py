# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_count(self):
        ''' Reasonable tests
        1. search empty lists
        2. count first, last and interior elements
        3. search for a list
        4. check that sublists on several levels are searched
        5. search non existing elements
        6. check that the list searched is not destroyed
        '''
        print('\nTests count')
        self.assertEqual(count(5, []), 0)  # empty list

        test_list = [1, 2, 3, 2, 4]
        self.assertEqual(count(1, test_list), 1)  # first element
        self.assertEqual(count(3, test_list), 1)  # interior element
        self.assertEqual(count(4, test_list), 1)  # last element

        self.assertEqual(count([1, 2, 3], [[2, 5, 3], [1, 2, 3], [[1, 2, 3], 1, 3]]), 2)  # search for list
        self.assertEqual(count(1, [1, [1, 2, 3, [1, 2, 3]]]), 3)  # sublist
        self.assertEqual(count(4, [2, 2, 3, 1, 3]), 0)  # non exsisting element

        # test for not destroyed list
        original_list = [1, 2, 3]
        count(1, original_list)
        self.assertEqual(original_list, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()

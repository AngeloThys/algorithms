# Binary search test cases
#
# Written by: Angelo Thys
import unittest
from binarySearch import binarySearch

class TestBinarySearch(unittest.TestCase):
    def test_binarySearch(self):
        self.assertEqual(binarySearch([1,2,3,4,5,6,7,8,9,10], 3), 2)
        self.assertEqual(binarySearch([1,2,3,4,5,6,7,8,9,10], 7), 6)
        self.assertEqual(binarySearch([1,2,3,4,5,6,7,8,9,10], 10), 9)
        self.assertEqual(binarySearch([1,2,3,4,5,6,7,8,9,10], 1), 0)
        self.assertEqual(binarySearch([1,2,3,4,5,6,7,8,9,10], 5), 4)
        self.assertEqual(binarySearch([1,2,3,4,5,6,7,8,9,10], 8), 7)
        self.assertEqual(binarySearch([1,2,3,4,5,6,7,8,9,10], 2), 1)
        self.assertEqual(binarySearch([1,2,3,4,5,6,7,8,9,10], 9), 8)
        self.assertEqual(binarySearch([1,2,3,4,5,6,7,8,9,10], 4), 3)
        self.assertEqual(binarySearch([1,2,3,4,5,6,7,8,9,10], 6), 5)

if __name__ == '__main__':
    unittest.main()

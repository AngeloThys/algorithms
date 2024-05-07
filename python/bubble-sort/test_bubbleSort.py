# Test cases for bubble sort algorithm
#
# Author: Angelo Thys
import unittest
from bubbleSort import bubbleSort

class TestBubbleSort(unittest.TestCase):
    array1 = [1, 2, 3, 4, 5]
    array2 = [5, 4, 3, 2, 1]
    array3 = [3, 1, 5, 2, 4]
    array4 = [2, 3, 1, 4, 5]

    def test_ordered(self):
        self.assertEqual(bubbleSort(self.array1), [1, 2, 3, 4, 5])

    def test_reversed(self):
        self.assertEqual(bubbleSort(self.array2), [1, 2, 3, 4, 5])

    def test_unordered_one(self):
        self.assertEqual(bubbleSort(self.array3), [1, 2, 3, 4, 5])

    def test_unordered_two(self):
        self.assertEqual(bubbleSort(self.array4), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()

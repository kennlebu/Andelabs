import unittest
from missing_number import MissingNumber

class MissingNumberTest(unittest.TestCase):
    """Test cases for the missing_number function"""

    # Tests for an empty list and returns 0 if it's empty
    def test_empty_list(self):
        self.assertEqual(0, MissingNumber.find_missing([], []),
                         msg='should return 0 for empty list')

    # Tests for same entries in the lists. Should return 0 if the entries are the same
    def test_same_entries(self):
        list1 = MissingNumber.find_missing([2], [2])
        list2 = MissingNumber.find_missing([4], [4])
        list3 = MissingNumber.find_missing([7], [7])
        self.assertListEqual([0, 0, 0],
                             [list1, list2, list3],
                             msg='should return 0 for lists with the same entries')

    # Tests whether the function returns the entry that is missing from one of the lists
    def test_missing_entries(self):
        list1 = MissingNumber.find_missing([1, 2], [1, 2, 5])
        list2 = MissingNumber.find_missing([4, 6, 8], [4, 6, 8, 10])
        list3 = MissingNumber.find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])
        self.assertListEqual([5, 10, 1],
                             [list1, list2, list3],
                             msg='should return the missing number for lists with similar entries and a missing number')

    # Testing whether the inputs are lists
    def test_invalid_input(self):
        self.assertEqual("Inputs must be lists", MissingNumber.find_missing('adc', 1), msg="Should return 'Inputs must be lists' for invalid inputs")

    # Testing for more than one missing number
    def test_more_missing_numbers(self):
        self.assertEqual("More than one missing number", MissingNumber.find_missing([1,2,3], [1,2,3,4,5]), msg="Should return 'More than one number missing' for more than one number missing")


if __name__ == '__main__':
    unittest.main()

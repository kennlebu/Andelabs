""" This function takes two lists as input, with one list
    having an extra entry not contained in the other list.
    The function returns the missing entry. """

class MissingNumber:
    @staticmethod
    def find_missing(list1, list2):
        if not isinstance(list1, list) or not isinstance(list1, list):
            return 'Inputs must be lists'
        if len(list1) == 0 and len(list2) == 0:
            return 0

        if len(list1) == len(list2):
            return 0

        for number in list2:
            if number not in list1:
                return number

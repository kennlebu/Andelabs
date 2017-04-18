"""Returns a list containing the lowest and highest number in a given list"""
"""or a list containing the length of the given list if the maximum and minimum are equal"""

class MaxMin:
    @staticmethod
    def find_max_min(nums):
        for i in range(len(nums)-1, 0, -1):
            maxpos = 0
            for j in range(1, i+1):
                if nums[j] > nums[maxpos]:
                    maxpos = j

            nums[i], nums[maxpos] = nums[maxpos], nums[i]

        return [len(nums)] if nums[0] == nums[-1] else [nums[0], nums[-1]]
            

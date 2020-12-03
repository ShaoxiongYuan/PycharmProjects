# Given an array of integers nums and an integer target, return indices of the two numbers such that
# they add up to target. You may assume that each input would have exactly one solution, and you may not
# use the same element twice. You can return the answer in any order.

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]


s = Solution()
print(s.twoSum([3, 3], 6))

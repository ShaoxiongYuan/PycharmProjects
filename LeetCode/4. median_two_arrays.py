# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = nums1 + nums2
        nums.sort()

        if len(nums) % 2 != 0:
            median = nums[(len(nums) - 1) // 2]
            return median

        else:
            median = float((nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2)
            return median

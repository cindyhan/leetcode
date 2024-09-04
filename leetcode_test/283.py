#! /usr/bin/python2.7
# -*- coding: utf8 -*-

"""
283.py
author: cindyhan 2024/9/3

"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        NO = 0
        index = 0
        nums_len = len(nums)
        for i in range(0, nums_len):
            if nums[index] == NO:
                nums.pop(index)
                nums.append(NO)
            else:
                index += 1

        return nums


obj = Solution()
nums1 = [0, 1, 0, 12, 3]
nums2 = [0]
nums3 = [0, 1]
nums4 = [0, 0, 1]
res1 = obj.moveZeroes(nums1)
res2 = obj.moveZeroes(nums2)
res3 = obj.moveZeroes(nums3)
res4 = obj.moveZeroes(nums4)
print(res1, res2, res3, res4)

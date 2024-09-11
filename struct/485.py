#! /usr/bin/python3.7
# -*- coding: utf8 -*-

"""
485.py
author: cindyhan 2024/9/3
485. 最大连续 1 的个数

"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0
        for i in nums:
            if i == 1:
                count +=1
                if result < count:
                    result = count
            else:
                count = 0


        return result


obj = Solution()
nums1 = [1, 1, 0, 1, 1, 1]
nums2 = [1, 0, 1, 1, 0, 1]
res1 = obj.findMaxConsecutiveOnes(nums1)
res2 = obj.findMaxConsecutiveOnes(nums2)
print(res1, res2)

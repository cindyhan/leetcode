#! /usr/bin/python3.7
# -*- coding: utf8 -*-

"""
217.py
author: cindyhan 2024/12/17

217. 存在重复元素
给定一个整数数组，判断是否存在重复元素。
如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
示例 1:
输入: [1,2,3,1]
输出: true
示例 2:
输入: [1,2,3,4]
输出: false
示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true    

"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set(nums)
        if len(nums_set) == len(nums):
            return False
        else:
            return True

    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_map = {}
        for i in nums:
            if i in nums_map:
                return True
            else:
                nums_map[i] = 1
        return False


nums = [1,2,3,1]
print(Solution().containsDuplicate(nums)) # True

nums = [1,2,3,4]
print(Solution().containsDuplicate(nums)) # False

nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate(nums)) # True
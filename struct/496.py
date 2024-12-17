#! /usr/bin/python3.7
# -*- coding: utf8 -*-

"""
496.py
author: cindyhan 2024/12/6
496. 下一个更大元素 I

思路：for nums1，for nums2，逐个比较大小
进阶：map[v] = k
如何应用栈？

"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        default_value = -1
        nums2_dict = {}
        num2_len= len(nums2)
        
        for k, v in enumerate(nums2):
            nums2_dict[v] = k
        for i in nums1:
            for j in range(nums2_dict[i]+1, num2_len):
                if nums2[j] > i:
                    res.append(nums2[j])
                    break
            else:
                res.append(default_value)
                
        return res


obj = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(obj.nextGreaterElement(nums1, nums2))

nums1 = [2,4]
nums2 = [1,2,3,4]
print(obj.nextGreaterElement(nums1, nums2))


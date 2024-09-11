#! /usr/bin/python3.7
# -*- coding: utf8 -*-

"""
27.py
author: cindyhan 2024/9/6
27. 移除元素
思路：手动移动指针

"""


class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    def removeElement(self, nums, val: int) -> int:
        index = 0
        n = len(nums)
        for _ in range(0, n):
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1

        k = len(nums)
        return k

    # 双指针解法
    def removeElement1(self, nums, val: int) -> int:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left


obj = Solution()
nums1 = [3, 2, 2, 3]
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
res1 = obj.removeElement(nums1, 3)
res2 = obj.removeElement(nums2, 2)
print(res1, res2)

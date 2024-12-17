#! /usr/bin/python3.7
# -*- coding: utf8 -*-

"""
389.py
author: cindyhan 2024/12/17

389. 找不同
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例 1:

输入: s = "abcd", t = "abcde"
输出: "e"
解释: 'e' 是那个被添加的字母。

示例 2:

输入: s = "", t = "y"
输出: "y"

说明:

s 和 t 长度都在 [1, 1000] 之间。
s 和 t 只包含小写字母。
"""


class Solution:

    # hash解法
    def findTheDifference(self, s: str, t: str) -> str:
        res = ''
        s_map = {}

        for char in s:
            s_map[char] = 1

        for char in t:
            if char not in s_map:
                res = char
                break

        return res

    # set解法
    def findTheDifference1(self, s: str, t: str) -> str:
        s_set = set(s)
        t_set = set(t)

        return t_set.difference(s_set).pop()


obj = Solution()
s = "abcd"
t = "abcde"
print(obj.findTheDifference(s, t))
print(obj.findTheDifference1(s, t))

s = ""
t = "y"
print(obj.findTheDifference(s, t))
print(obj.findTheDifference1(s, t))

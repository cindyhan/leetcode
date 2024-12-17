#! /usr/bin/python3.7
# -*- coding: utf8 -*-

"""
20.py
author: cindyhan 2024/9/13
20. 有效的括号

"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    tmp = stack.pop()
                    if c == ')':
                        if tmp != '(':
                            return False
                    if c == ']':
                        if tmp != '[':
                            return False
                    elif c == '}':
                        if tmp != '{':
                            return False

        if len(stack) == 0:
            return True
        else:
            return False


obj = Solution()
res1 = obj.isValid('()')
res2 = obj.isValid('()[]{}')
res3 = obj.isValid('(]')
res4 = obj.isValid('([])')
res5 = obj.isValid('[')
res6 = obj.isValid('){')
print(res1, res2, res3, res4, res5, res6)

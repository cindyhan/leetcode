#! /usr/bin/python3.7
# -*- coding: utf8 -*-

"""
206.py
author: cindyhan 2024/9/11
206. 反转链表

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next

        return pre


obj = Solution()
head = [1, 2, 3, 4, 5]
res1 = obj.reverseList(head)
print(res1, res1)

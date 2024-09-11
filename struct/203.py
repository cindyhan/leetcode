#! /usr/bin/python3.7
# -*- coding: utf8 -*-

"""
203.py
author: cindyhan 2024/9/6
203. 移除链表元素

"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # 可以是任意值，因为用不到
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next

    def removeElements1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # 可以是任意值，因为用不到
        dummy.next = head
        current = dummy
        while head:
            if head.val == val:
                current.next = head.next
            else:
                current = current.next
            head = head.next

        return dummy.next


obj = Solution()
nums1 = [1, 2, 6, 3, 4, 5, 6]
nums2 = [7, 7, 7, 7]
res1 = obj.removeElements(nums1, 6)
res2 = obj.removeElements(nums2, 7)
print(res1, res2)

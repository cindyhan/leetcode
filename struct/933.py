#! /usr/bin/python3.7
# -*- coding: utf8 -*-

"""
933.py
author: cindyhan 2024/9/13
933. 最近的请求次数

"""
from cytoolz.itertoolz import deque


class RecentCounter:

    def __init__(self):
        self.ping_list = deque()
        self.err_code = -1
        self.past_time = 3000

    def ping(self, t: int) -> int:
        if len(self.ping_list) > 0:
            if t <= self.ping_list[-1]:  # 0队首，-1队尾
                return self.err_code
        self.ping_list.append(t)
        while len(self.ping_list) > 0 and t - self.ping_list[0] > self.past_time:
            self.ping_list.popleft()

        return len(self.ping_list)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
res1 = obj.ping(1)
print(res1)
res2 = obj.ping(100)
print(res2)
res3 = obj.ping(3001)
print(res3)
res4 = obj.ping(3002)
print(res4)

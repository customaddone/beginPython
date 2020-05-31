def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

num = []
for i in range(100):
    if i < 50:
        num.append(i)
    else:
        num.append(100 - i)

left, right = 0, len(num) - 1
while abs(right - left) > 3:
    mid1 = (right * 2 + left) // 3 + 1
    mid2 = (right + left * 2) // 3
    # 最小値を求める場合は矢印逆になる
    if num[mid1] <= num[mid2]:
        right = mid1
    else:
        left = mid2
print(right)
print(left)

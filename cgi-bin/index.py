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
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

# LRLRRL
#    ↑
# 反転させると
# LLLRLL
#  ↑↑  ↑
# また反転させると
# LLLLLL
#  ↑↑↑↑↑

# 反転させると最大2人まで幸福な人を増やせる
N, K = getNM()
s = input()
cnt = 0
for i in range(N - 1):
    if s[i] == s[i + 1]:
        cnt += 1
print(min(cnt + 2 * K, N - 1))

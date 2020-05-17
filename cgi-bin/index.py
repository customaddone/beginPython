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

H, N = getNM()
magic = []
for i in range(N):
    a, b = getNM()
    # AがATC,BがMP
    magic.append([a, b])

dp = [float('inf')] * (H + 1)
dp[0] = 0
# HP = iを削るための最小MP
for i in range(1, H + 1):
    for j in magic:
        if i < j[0]:
            dp[i] = min(dp[i], j[1])
        else:
            dp[i] = min(dp[i], dp[i - j[0]] + j[1])
print(dp[-1])

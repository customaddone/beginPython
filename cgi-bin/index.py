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
import fractions
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

from itertools import permutations
from math import factorial, hypot

H, N = 9999, 10
magic = [
[540,7550],
[691,9680],
[700,9790],
[510,7150],
[415,5818],
[551,7712],
[587,8227],
[619,8671],
[588,8228],
[176,2461]
]

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

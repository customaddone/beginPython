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

N = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]

W = 5

dp = [[0] * (W + 1) for i in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(W + 1):
        dp[i + 1][j] = dp[i][j]
        for r in range(N):
            if w[r] <= j:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w[r]] + v[r])
print(dp[N][W])

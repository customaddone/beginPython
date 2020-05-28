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

def rec_memo(i, j):
    if dp[i][j]:
        return dp[i][j]
    if i == N:
        res = 0
    else:
        res = rec_memo(i + 1, j)
        for r in range(N):
            # ここ「以下」になることに気をつける
            if w[r] <= j:
                res = max(res, rec_memo(i + 1, j - w[r]) + v[r])
    dp[i][j] = max(dp[i][j], res)
    return res
print(rec_memo(0, W))

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

S = list(map(int, list(input())))
N = len(S)

dp = [[-1] * (N + 1) for i in range(N + 1)]

def rec(l, r):
    if dp[l][r] != -1:
        return dp[l][r]
    if abs(l - r) <= 1:
        return 0

    res = 0
    if S[l] != S[r - 1] and rec(l + 1, r - 1) == r - l - 2:
        res = r - l
    for i in range(l + 1, r):
        res = max(res, rec(l, i) + rec(i, r))
    dp[l][r] = res
    return res
print(rec(0, N))

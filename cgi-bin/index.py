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

def part_sum(a,A):
    p = 10 ** 9 + 7
    N = len(a)
    dp = [[0] * (A + 1) for i in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(A + 1):
            if a[i] <= j:
                dp[i + 1][j] = dp[i][j - a[i]] + dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j]
    return dp[N][A]

a = [1, 3, 5, 7, 9]
A = 10
print(part_sum(a, A))

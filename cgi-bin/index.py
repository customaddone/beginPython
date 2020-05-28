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

# 例えばジャンケンで３回同じ手を出さない場合の通り
# N = 3のときは3 ** 3 - 3 = 24通り
N = 5
dp = [[[0] * 3 for i in range(3)] for j in range(N)]
for i in range(3):
    dp[0][i][i - 1] = 1

for i in range(1, N):
    for l in range(3):
        for m in range(3):
            for n in range(3):
                if l == m and m == n:
                    continue
                dp[i][l][m] += dp[i - 1][m][n]
print(dp)

from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
sys.setrecursionlimit(1000000)
INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# 累積和

"""
配列Aに
A[0] += a1
A[1] += a2... と左から順に足していく場合、
区間[l, r)(ただしr - 1 <= 足した場所)をimosによりO(1)で計算できる
A = [0] + A 1-index化しimos[r] - imos[l]でできる
"""

A = [1, 2, 3, 4, 5]
A = [0] + A
for i in range(1, N + 1):
    A[i + 1] += A[i]

# for i in range(N)
i = 0
A[i + 1] += 3
A[i + 1] += A[i]
l, r = 0, 1 # [0, 1)
print(A[r] - A[l])

from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product
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
INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

N = getN()
N *= 2
A = getList()
dp = [[float('inf')] * (N + 1) for i in range(N + 1)]

# [j, j + i)の区間を全て消すための最小費用
for i in range(0, N + 1, 2): # 区間の幅
    for j in range(N - i + 1): # lの場所
        if i == 0:
            dp[j][j + i] = 0
            continue
        # 端の二つ(j, j + i - 1)を消すコスト + [j + 1, j + i - 1)を消すコスト（計算済み）
        dp[j][j + i] = abs(A[j + i - 1] - A[j]) + dp[j + 1][j + i - 1]
        # 区間を2つに分割して最小値を探す操作
        for k in range(j, j + i, 2):
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k][j + i])

print(dp[0][N])

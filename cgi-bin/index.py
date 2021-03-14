from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right

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

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# mod付き行列累乗
def array_cnt(ar1, ar2, m):
    h = len(ar1)
    w = len(ar2[0])
    row = ar1
    col = []
    for j in range(w):
        opt = []
        for i in range(len(ar2)):
            opt.append(ar2[i][j])
        col.append(opt)

    res = [[[0, 0] for i in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            cnt = 0
            for x, y in zip(row[i], col[j]):
                cnt += x * y
            res[i][j] = cnt
            res[i][j] %= m
    return res

"""
Aは非常に大きいLもでかい
mod算を使うのは難しい
O(N ** 2)ならギリギリ
貪欲は
r = len(a)とすると
a1 % B
a1 *= (10 ** r)
a1 + a1をL - 1回繰り返す

now = 0
for a, l in Q:
    r = len(str(a))
    for i in range(l):
        now *= (10 ** r)
        now += a
        now %= B

123
123123
1231234
12312344
231234449

Lが大きい　ダブリングしたいが
now はせいぜい10 ** 9 + 7
2個先、4個先の変換
写像Tはどのようなものか
"""

N = getN()
Q = [getList() for i in range(N)]
B = getN()

res = [[0, 1]]
for a, l in Q:
    r = len(str(a))
    # 行列累乗
    logk = l.bit_length()
    dp = [[[0] * 2 for i in range(2)] for j in range(logk)]
    dp[0] = [[10 ** r, 0], [a, 1]]
    for i in range(1, logk):
        dp[i] = array_cnt(dp[i - 1], dp[i - 1], B)

    for i in range(logk):
        if l & (1 << i):
            res = array_cnt(res, dp[i], B)

print(res[0][0])

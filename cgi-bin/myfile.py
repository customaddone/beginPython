from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
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

"""
数学問題でーす
どちらかが累計でN回勝てば良い　遷移を考える N^2解から考える
高橋くんが1回勝って終わる確率
答えは整数 / 整数になるらしい

高橋くんがN回勝って終わる時
青木くんはN - 1回以下の任意の整数回勝って終わっている
青木くんが勝つ確率をb回で固定して足し合わせ
引き分けは無限回あって良い
青木くんがN回勝って終わるのは逆になる
２つは独立事象か？

N+b+cCc * N+bCb * (A / 100)^N * (B / 100)^b * (C / 100)^c

期待値を計算
dp[1][0] = A / 100 * (dp[0][0] + 1) + C / 100 * (dp[1][0] + 1)
dp[i][j] = A / 100 * (dp[i - 1][j] + 1) + B / 100 * (dp[i][j - 1] + 1) + C / 100 * (dp[i][j])
(100 - C)dp[i][j] = A * (dp[i - 1][j] + 1) + B * (dp[i][j - 1] + 1)

合計でN回勝つ期待値でdpとるか
dp[i]: どちらかがN回勝って終わっている
i+1だと？

"""

N, A, B, C = getNM()
dp = [[0] * (N + 1) for i in range(N + 1)]

for i in range(N):
    for j in range(N):
        if i == j == 0:
            continue

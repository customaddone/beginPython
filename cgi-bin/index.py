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

# ARC060 E 高橋君とホテル

"""
クエリがたくさん
それぞれlogNで処理しろ
愚直な方法は
方向は逆にしても同じ結果
要するにオーバーしてもいい

最大N - 1回飛べる
"""

N = getN()
A = getList()
D = getN()
Q = getN()
que = [getList() for i in range(Q)]

dest = [0] * N
r = 0
# 一回でどこまで飛べるか
for l in range(N):
    while r < N and A[r] - A[l] <= D:
        r += 1
    dest[l] = r - 1

logn = N.bit_length()
# 2 ** N回飛んでどこまで行けるか
doubling = [[0] * N for i in range(logn)]
doubling[0] = dest

for i in range(1, logn):
    for j in range(N):
        # 前回の時点ですでに欄外に飛んでる場合
        if doubling[i - 1][j] == N:
            doubling[i][j] = N
        # それ以外はダブリング
        else:
            doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

# ギリギリ超えないところを探す
for a, b in que:
    if a > b:
        a, b = b, a
    a -= 1
    b -= 1
    # 計算
    cnt = 0
    now = a
    for j in range(logn - 1, -1, -1):
        # ゴールまで辿りつく前まで進む
        if doubling[j][now] < b:
            cnt += 1 << j
            now = doubling[j][now]

    # 限界まで近づいた後 +1する
    print(cnt + 1)

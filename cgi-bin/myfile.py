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
文字列dp
ランレングス圧縮
26^N個あるがそれらは等価
ぶった切ると2増える　置き換えた分は絶対偶数になる
他の文字に変えるのは25通り　長さが変わる
同じ文字は1通り　長さは変わらない
"""

N, P = getNM()
# 長さは2Nまで
prev = [0] * (N + 1)
# 長さ1が26個
prev[1] = 26
for _ in range(N - 1):
    next = [0] * (N + 1)
    for i in range(N, -1, -1):
        # 変わる
        if i < N:
            next[i + 1] += prev[i] * 25
            next[i + 1] %= P
        # 変わらない
        next[i] += prev[i]
        next[i] %= P
    print(prev, next)
    prev = next

ans = 0
for i in range(N + 1):
    if i * 2 <= N:
        ans += prev[i]
        ans %= P
    print(ans)

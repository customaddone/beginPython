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

L = []
bi = [[0] * 70 for i in range(N - 1)]
for i in range(N - 1):
    u, v, w = getNM()
    L.append([u - 1, v - 1])
    for j in range(70):
        bi[i][j] = w % 2
        w //= 2
    E[u - 1].append(v - 1)
    E[v - 1].append(u - 1)

size = [0] * N
par = [0] * N
def dfs(u, p):
    res = 1
    par[u] = p
    for v in E[u]:
        if v != p:
            res += dfs(v, u)

    size[u] = res
    return res

dfs(0, -1)
for i in range(N - 1):
    u, p = L[i]
    # 逆なら 前に子要素uが来るように
    if par[p] == u:
        L[i][0] = p
        L[i][1] = u

po = [1]
for i in range(70):
    po.append((po[-1] * 2) % mod)

# 各辺について探索
ans = 0
for u, _ in L:
    way = size[u] * (N - size[u])
    print(u, _, way)

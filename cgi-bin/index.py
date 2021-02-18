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

N, X = getNM()
X -= 1
H = getList() # フラグが立っている部分だけ
dist =[[] for _ in range(N)]
for i in range(N - 1):
    a, b = getNM()
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

# 地点vのans
def dfs(par, v):
    res = 0
    for i in dist[v]:
        if i == par:
            continue
        # 子要素iのans
        opt = dfs(v, i)
        if opt > 0: # 宝石があるルートの帰り道
            # もしiの部分木に宝石があれば親→子 + opt + 子→親の経路を通らないといけない
            res += opt + 2
        elif H[i]:
            # もしiの部分木の中でiにのみ宝石がある場合にはopt = 0だが,
            # iの宝石を回収するために親→子 + 子→親の経路を通らないといけない
            res += 2

    return res

print(dfs(-1, X))

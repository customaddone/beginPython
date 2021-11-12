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

# ルートの決定方法はいじれる
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if x > y: # よりrootのインデックスが小さい方が親
            x, y = y, x
        # if self.parents[x] > self.parents[y]:
            # x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

"""
無効グラフ
この辺の全てに方向付けをする
sccを考える
明らかに無理な場合を消すには？

森を一つずつ調べていく
頂点数が1ならスキップ
辺の数 != 頂点の数 ならアウト

ループは必ず1個ある　まず木を流す
ループについては順流か逆流かしかできない
ループの大きさを探す

使われなかった辺を探す
"""

N, M = getNM()
C = [0] * N
edges = []
E = [[] for i in range(N)]
U = UnionFind(N)
for _ in range(M):
    u, v = getNM()
    # 小細工
    if u > v:
        u, v = v, u
    U.union(u - 1, v - 1)
    E[u - 1].append(v - 1)
    E[v - 1].append(u - 1)
    edges.append([u - 1, v - 1])

# 親頂点
r = [[] for i in range(N)]
# どのグループにどの辺が使われるか
E_r = [[] for i in range(N)]
for i in range(N):
    r[U.find(i)].append(i)
for i in range(M):
    E_r[U.find(edges[i][0])].append(i)
print(r, E_r)

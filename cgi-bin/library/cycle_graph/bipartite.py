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

input = sys.stdin.readline
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

N = 5
#es = [[1,2,3],[0,2],[0,1],[0,4],[3]] # False
dist = [
[1, 3],
[0, 2],
[1, 3],
[0, 2, 4],
[3]
] # True

#n個の頂点の色を初期化。0:未着色、1:黒、-1:白
colors = [0] * N

#頂点vをcolor(1 or -1)で塗り、再帰的に矛盾がないか調べる。矛盾があればFalse
def dfs(v, color):
    #今いる点を着色
    colors[v] = color
    #今の頂点から行けるところをチェック
    for to in dist[v]:
        #同じ色が隣接してしまったらFalse
        if colors[to] == color:
            return False
        #未着色の頂点があったら反転した色を指定し、再帰的に調べる
        if colors[to] == 0 and not dfs(to, -color):
            return False
    #調べ終わったら矛盾がないのでTrue
    return True

#2部グラフならTrue, そうでなければFalse
def is_bipartite():
    return dfs(0,1) # 頂点0を黒(1)で塗ってDFS開始

print(is_bipartite())

# 1 - indexで
def bipartite(N, M, edges):
    g = defaultdict(list)
    for a, b in edges:
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    color = [0] * N
    dq = deque([(0, 1)])

    while dq:
        v, c = dq.popleft()
        color[v] = c
        c *= -1
        for nv in g[v]: # 頂点vの各childを調べる
            if color[nv] == 0: # もし未探索なら
                dq.append((nv, c))
            if color[nv] == -c: # もしcolor[nv]がvの色を反転させたものでなければ
                dq = []
                return False, color

    return True, color

color = [0] * N
def bipartite(N, sta, edges):
    # 外部に置く 1, -1: 探索済み 0: 未探索
    global color
    dq = deque([(sta, 1)])
    # 今回塗ったやつ
    colored = set()
    while dq:
        v, c = dq.popleft()
        color[v] = c
        colored.add(v)
        c *= -1
        for nv in edges[v]:
            if color[nv] == 0:
                dq.append((nv, c))
            if color[nv] == -c:
                dq = []
                return (False, set())
    return (True, colored)

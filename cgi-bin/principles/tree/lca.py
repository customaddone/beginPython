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
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
木のu - v間パスの長さについてはlogNで求められる
dist[u]: 頂点0 - u間のパスの長さ　を求めておくと
d = dist[u] + dist[v] - 2 * dist[lca.get(u, v)]
"""

lca = LCA(E)
rel = lca.get(u, v)
d1 = dist[u] + dist[v] - 2 * dist[rel]

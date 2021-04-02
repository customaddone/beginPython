from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
import random
import string
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

sys.setrecursionlimit(1000000000)
mod = 998244353
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

"""
構築問題
整数の差がちょうど1
実験してみる
6 - ? - 8の場合　可能 7
6 - ? - 9の場合　不可能

距離がi離れた頂点について差がi以内であることが必要
6 - ? - 8
      - 4 できない
6 - ? - 7
      - 5 できる
6 - ? - 5
      - 4 できる
?の子の差が2以内である必要がある
upperとunderを書き込んでいく？　なんか戦略があるはず

一番大きい頂点からやっていこうか
隣の頂点は１小さい数の方が便利
7 6 7 6...としていくか

部分木をボトムアップ
"""

N = getN()
E = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = getNM()
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)


def parents(n, sta, dist):
    pos = deque([sta])
    ignore = [0] * n
    path = [0] * n # 親要素
    path[sta] = -1
    d = [[] for i in range(n)] # 有向辺

    while pos:
        u = pos.popleft()
        ignore[u] = 1

        for i in dist[u]:
            if ignore[i] != 1:
                path[i] = u
                d[u].append(i)
                pos.append(i)

    return path

D = parents(N, 0, E)

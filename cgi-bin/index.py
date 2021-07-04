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
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
S, T = 0, 2
[0, 1, 2, 1]
[2, 1, 0, 1]
最短距離で移動する通りの数はわかる
[1, 3, 1, 1, 1, 1, 2, 1]
[1, 1, 1, 3, 1, 1, 1, 2]
もちろん対称になる

N^2通りから条件を満たすものを探す
同じルートを選択してはいけない　他には？
同時に同じパスを使用してはいけない

別々なルートを2つ選択する方法
最短距離 // 2になるまでは適当に進んでいい
"""

N, M = getNM()
S, T = getNM()
S -= 1
T -= 1
E = [[] for i in range(N)]
for _ in range(M):
    u, v, d = getNM()
    E[u - 1].append([v - 1, d])
    E[v - 1].append([u - 1, d])

def dij(start, edges):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        d, now = heappop(pq)
        if (d > dist[now]):
            continue
        for i in edges[now]:
            if dist[i[0]] > dist[now] + i[1]:
                dist[i[0]] = dist[now] + i[1]
                heappush(pq, (dist[i[0]], i[0]))
    return dist

d1 = dij(S, E)
d2 = dij(T, E)

def counter(sta, E, d):
    pos = deque([sta])
    ignore = [0] * N
    cnt = [0] * N
    cnt[sta] = 1

    while len(pos) > 0:
        u = pos.popleft()
        if ignore[u] == 0:
            ignore[u] = 1
            # d[i] == d[u] + 1を満たすuの子ノード全てに
            # 「スタートからuまでの通りの数」をプラス（他のルートからも来る）
            for i in E[u]:
                if d[i[0]] == d[u] + i[1]:
                    cnt[i[0]] += cnt[u]
                    pos.append(i[0])
    return cnt

# 各頂点への最短経路の本数
w1, w2 = counter(S, E, d1), counter(T, E, d2)
distance = d1[T]

color = [-1] * N
cnt = 0
for i in range(N):
    # Sからの距離が最短経路 // 2未満
    if d1[i] <= (distance - 1) // 2:
        color[i] = 0
    if d2[i] <= (distance - 1) // 2:
        color[i] = 1
    # 最短距離がちょうどdis // 2の場合は頂点上で出会う

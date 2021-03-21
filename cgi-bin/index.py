from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
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
遠方に行くには金貨をどこかで補充しないと
変形ダイクストラ　銀貨をA枚持ってた時の最短距離
銀貨何枚を持っていれば何分でどこにいけるかはわかる
ルート上のどこかで金を交換すればいい　交換分数のみが重要
"""

# 最短経路へのパス付きダイクストラ
# 運賃s以内でいけるか
def dij(start, edges, s):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start, s)] # 銀S枚を持ってスタート
    parent = [-1] * N
    cost = [float('inf')] * N
    cost[0] = 0

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        di, now, sil = heappop(pq)
        if (di > dist[now]):
            continue
        for v, c, d in edges[now]:
            if dist[v] > dist[now] + d and sil >= c:
                dist[v] = dist[now] + d
                parent[v] = now
                cost[v] = s - sil + c
                heappush(pq, (dist[v], v, sil - c))

    return dist, cost

N, M, S = getNM()
road = [[] for i in range(N)]
for i in range(M):
    u, v, a, b = getNM()
    road[u - 1].append([v - 1, a, b])
    road[v - 1].append([u - 1, a, b])
exc = [getList() for i in range(N)]

# iスタート、銀貨がj枚でどこにいけるか
table = [[] for i in range(N)]
for i in range(N):
    for j in range(5001):
        table[i].append(dij(i, road, j)[0])

ans = [float('inf')] * N
cost = dij(0, road, S)[1]
print(cost)
# 点iで金を補充して点jまで行くことを考える
# 中継地点
for i in range(N):
    c, d = exc[i]
    # 中継地点スタートの時銀貨s枚
    for s in range(5001):
        # s - S + cost[i]枚足らないのだから
        add = ((max(s + cost[i] - S, 0) + c - 1) // c) * d
        # ゴール地点
        for j in range(N):
            if ans[j] > table[0][S][i] + add + table[i][s][j]:
                print(table[0][S][i], add, table[i][s][j], i, j, s)
            ans[j] = min(ans[j], table[0][S][i] + add + table[i][s][j])
print(ans)

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
# sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

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

"""
どのタイミングで出発すればいいか
混雑度は線形
拡張ダイクストラでやる
何秒か待って出発する
ダメならtを進めればいい
時刻Tが一定なので...
現在の時刻で通過できる場合と出来ない場合を考える
現在通過出来ない場合は次t = Di + T - Kの時に通過できる
"""

N, M, T, K = getNM()
E = [[] for i in range(N)]
for i in range(M):
    a, b, c, d = getNM()
    E[a - 1].append([b - 1, c, d])
    E[b - 1].append([a - 1, c, d])

def dij(start, edges):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        now, u = heappop(pq)
        if (now > dist[u]):
            continue
        for v, c, d in edges[u]:
            dep = dist[u] # 現在時刻を記録
            # 現在時刻で通過できない場合は出発時刻をを上書き
            if d - abs(T - now) >= K:
                dep = d + T - K
            if dist[v] > dep + c:
                dist[v] = dep + c
                heappush(pq, (dist[v], v))
    return dist

print(dij(0, E))

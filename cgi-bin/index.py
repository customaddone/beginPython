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

class MinCostFlow:
    # 最小費用流(ベルマンフォード版、負コストに対応可)

    INF = 10 ** 18

    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap, cost):
        G = self.G
        G[fr].append([to, cap, cost, len(G[to])])
        G[to].append([fr, 0, -cost, len(G[fr])-1])

    def flow(self, s, t, f):

        N = self.N; G = self.G
        INF = MinCostFlow.INF

        res = 0
        prv_v = [0] * N
        prv_e = [0] * N

        while f:
            dist = [INF] * N
            dist[s] = 0
            update = True

            while update:
                update = False
                for v in range(N):
                    if dist[v] == INF:
                        continue
                    for i, (to, cap, cost, _) in enumerate(G[v]):
                        if cap > 0 and dist[to] > dist[v] + cost:
                            dist[to] = dist[v] + cost
                            prv_v[to] = v; prv_e[to] = i
                            update = True

            # 流れない場合
            if dist[t] == INF:
                return float('inf')

            d = f; v = t
            while v != s:
                d = min(d, G[prv_v[v]][prv_e[v]][1])
                v = prv_v[v]
            f -= d
            res += d * dist[t]
            v = t
            while v != s:
                e = G[prv_v[v]][prv_e[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prv_v[v]
        return res

N, M, Q = getNM()
C = [getList() for i in range(N)]
B = getList()
que = []
for i in range(Q):
    l, r = getNM()
    que.append([l - 1, r - 1])

for l, r in que:
    mcf = MinCostFlow(N + M + 2)
    # C: 0 ~ N - 1, B, N ~ N + M - 1
    # start: N + M, end: N + M + 1
    for i in range(N):
        # 始点 ~ Ci
        mcf.add_edge(N + M, i, 1, 0)
        for j in range(M):
            # Ci ~ Bi
            if not l <= j <= r and C[i][0] <= B[j]:
                mcf.add_edge(i, N + j, 1, -C[i][1])
    # B ~ 終点
    for j in range(M):
        mcf.add_edge(N + j, N + M + 1, 1, 0)

    ans = 0
    # 一個ずつ流してみる
    for i in range(N):
        res = -mcf.flow(N + M, N + M + 1, 1)
        if res != -INF:
            ans += res
        else:
            break

    print(ans)

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
sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

T = getN()
for _ in range(T):
    _ = input()
    N, M = getNM()
    dis1 = [float('inf')] * N
    dis1[0] = 0
    E = [[] for i in range(N)]
    for _ in range(M):
        u, v = getNM()
        E[u - 1].append(v - 1)

    # 距離の計測
    q = deque([0])
    # トポソ順
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in E[u]:
            if dis1[v] > dis1[u] + 1:
                dis1[v] = dis1[u] + 1
                q.append(v)

    dis2 = [float('inf')] * N
    # 葉から探索
    while order:
        u = order.pop()
        for v in E[u]:
            # 逆行
            if dis1[v] <= dis1[u]:
                dis2[u] = min(dis2[u], dis1[v])
            else:
                dis2[u] = min(dis2[u], dis2[v])

    print(*[min(dis1[i], dis2[i]) for i in range(N)])

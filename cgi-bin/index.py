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

"""
bulletっぽさある
一個以上含むやつを作れるか
連結していれば作れる

魔法石の最小値
なんでK少ないの　Kから任意の２つを選んで直径にする
巡回したいけど無理ですか？
"""

N, M = getNM()
E = [[] for i in range(N)]
for i in range(M):
    a, b = getNM()
    E[a - 1].append([b - 1, 1])
    E[b - 1].append([a - 1, 1])
K = getN()
C = [i - 1 for i in getList()]
set_c = set(C)

def distance(n, edges, sta):
    ignore = [float('inf')] * N
    ignore[sta] = 0
    pos = deque([sta])

    while len(pos) > 0:
        u = pos.popleft()
        for i in edges[u]:
            if ignore[i[0]] == float('inf'):
                ignore[i[0]] = ignore[u] + i[1]
                pos.append(i[0])
    return ignore

G = []
for i in range(K):
    g = []
    opt = distance(N, E, C[i])
    for j in range(N):
        if j in set_c:
            g.append(opt[j])
    G.append(g)

if sum(G[0]) == float('inf'):
    print(-1)
    exit()

def counter(sta, K, G):
    # dp[bit][i]これまでに踏んだ場所がbitであり、現在の場所がiである
    dp = [[float('inf')] * K for i in range(1 << K)]
    for i in range(K):
        dp[1 << i][i] = 0

    for bit in range(1, 1 << K):
        if not bit:
            continue
        # s:現在の場所
        for s in range(K):
            # sを踏んだことになっていなければ飛ばす
            if not bit & (1 << s):
                continue
            # t:次の場所
            for t in range(K):
                # tを過去踏んでいない and s → tへのエッジがある
                if (bit & (1 << t)) == 0:
                    dp[bit|(1 << t)][t] = min(dp[bit|(1 << t)][t], dp[bit][s] + G[s][t])

    return min(dp[-1])

print(counter(0, K, G) + 1)

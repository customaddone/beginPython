def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
import heapq
import math
from fractions import gcd
import random
import string
import copy
from itertools import combinations, permutations, product
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

"""
eye lid
4
lie
die
did
dye
"""

s1, s2 = input().split(' ')
N = getN()
S = set()

S.add(s1)
S.add(s2)

for i in range(N):
    S.add(input())

if s1 == s2:
    print(0)
    print(s1)
    print(s2)
    exit()

S = list(S)
N = len(S)

def judge(s1, s2):
    cnt = 0
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            cnt += 1
    if cnt <= 1:
        return True
    else:
        return False

# 行き先と距離記録
dist = [[] for i in range(N)]
d = [[float('inf')] * N for i in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if judge(S[i], S[j]):
            dist[i].append(j)
            dist[j].append(i)
            d[i][j] = 1
            d[j][i] = 1

# start goal位置探索
sta = 0
end = 0
for i in range(N):
    if S[i] == s1:
        sta = i
        break
for i in range(N):
    if S[i] == s2:
        end = i
        break

# ダイクストラ
def dij(start, edges):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        di, now = heapq.heappop(pq)
        if (di > dist[now]):
            continue
        for i in edges[now]:
            if dist[i] > dist[now] + d[i][now]:
                dist[i] = dist[now] + d[i][now]
                heapq.heappush(pq, (dist[i], i))
    return dist

distance = dij(sta, dist)
if distance[end] == float('inf'):
    print(-1)
    exit()

# sta起点の最短経路を通る木生成
def router(n, sta):
    pos = deque([sta])
    ignore = [0] * n
    path = [0] * n
    ignore[sta] = 0
    path[sta] = -1

    while pos:
        u = pos.popleft()

        for i in dist[u]:
            if ignore[i] != 1 and distance[i] == ignore[u] + d[i][u]:
                path[i] = u
                ignore[i] = ignore[u] + d[i][u]
                pos.append(i)

    return path

path = router(N, sta)
ans = [S[end]]
now = end
while True:
    now = path[now]
    ans.append(S[now])
    if now == sta:
        break

print(len(ans) - 2)
for i in range(len(ans)):
    print(ans[-i - 1])

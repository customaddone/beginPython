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
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

N, M = getNM()
query = [getList() for i in range(M)]
K = getN()
question = [getList() for i in range(K)]

dist = [[float('inf')] * N for i in range(N)]
for i in range(N):
    dist[i][i] = 0
for i in range(M):
    a, b, c = query[i]
    dist[a - 1][b - 1] = c
    dist[b - 1][a - 1] = c

def warshall_floyd(dist):
    for k in range(N):
        # i:start j:goal k:中間地点でループ回す
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# まず一回回す
warshall_floyd(dist)

# 距離の方を更新していけばO(K * N ** 2)で済む
for x, y, z in question:
    x -= 1
    y -= 1
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][x] + z + dist[y][j], dist[i][y] + z + dist[x][j])
    res = 0
    for i in range(N):
        for j in range(i + 1, N):
            res += dist[i][j]
    print(res)

"""
第７回日本情報オリンピック 予選
F - 船旅 
0:いくつかの船舶を乗り継いで，出発地と目的地を結ぶ航路の中で，もっとも安価な運賃を計算し，客に伝える
1:島と島の間を結ぶ新しい船舶が，運航を開始する

①ワーシャルフロイドする
②1でエッジを追加し、ワーシャルフロイドを更新する 0で答える
　ワーシャルフロイドの更新を最小限にするには？
　→
　新しい航路がc ~ dまでで運賃がeだとすると
　任意の区間i ~ jについて運賃
  1:i ~ j
  2:i ~ c + c ~ d(e円) + d ~ j
  3:j ~ c + c ~ d(e円) + d ~ i
  を比べる
"""

N, K = getNM()
query = [getList() for i in range(K)]

# 距離の表
dist = [[float('inf')] * N for i in range(N)]
for i in range(N):
    dist[i][i] = 0

for q in query:
    # queryに答える
    if q[0] == 0:
        _, a, b = q
        a -= 1
        b -= 1
        if dist[a][b] == float('inf'):
            print(-1)
        else:
            print(dist[a][b])
    # ワーシャルフロイドの更新
    else:
        _, c, d, e = q
        c -= 1
        d -= 1
        dist[c][d] = min(dist[c][d], e)
        dist[d][c] = min(dist[d][c], e)

        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][c] + e + dist[d][j], dist[i][d] + e + dist[c][j])

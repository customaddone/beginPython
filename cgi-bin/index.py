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
from math import sqrt
from fractions import gcd
import random
import string
import copy
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

N, M, P = getNM()
que = [getList() for i in range(M)]

edges = []
for a, b, c in que:
    # 次の点に行った時に獲得できる点 - 支払うコインP
    # 重みが負になることもある　→　ベルマンフォード
    edges.append([a - 1, b - 1, c - P])

# どのようにNに到達すればいいか
# 最長距離を求める


# after contest
# 1 → 2 1
# 2 → 3 1
# 3 → 2 1
# 3 → 4 1
# 1 → 4 100000の場合
# 2 ~ 3間でループがあるため値を無限に増やせるが、N - 1のループでは検出できない
# 1 → 4 100000 が十分大きいため
def bellman(edges, num_v):
    dist = [-float('inf') for i in range(num_v)]
    dist[0] = 0

    # 一回目のループ
    for i in range(N - 1):
        for edge in edges:
            if dist[edge[1]] < dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]

    # 負閉路検出
    nega = [0] * N
    for i in range(N):
        for edge in edges:
            # rootの頂点が既に更新されている（ループ検出）されていたなら
            # 行先にも無条件で「更新される」フラグを立てる
            if nega[edge[0]] == 1:
                nega[edge[1]] = 1
            if dist[edge[1]] < dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                nega[edge[1]] = 1

    if nega[N - 1]:
        print('-1')
        exit()

    return dist

ans = bellman(edges, N)[N - 1]
if ans <= 0:
    print(0)
else:
    print(ans)

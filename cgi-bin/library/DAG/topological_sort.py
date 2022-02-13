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

# DAGのグラフについてトポロジカルソートすればdpができる
# ソートができ、その種類が複数ある場合はどれか1つが出る
N = 8

dist = [
[1, 6],
[2, 5],
[3, 1],
[3, 2],
[4, 1],
[4, 6],
[5, 1],
[6, 7],
[7, 8]
]

# 1-index
def topological(n, dist):
    in_cnt = defaultdict(int)
    outs = defaultdict(list)

    for a, b in dist:
        in_cnt[b - 1] += 1
        outs[a - 1].append(b - 1)

    res = []
    queue = deque([i for i in range(n) if in_cnt[i] == 0])

    while len(queue) != 0:
        v = queue.popleft()
        res.append(v)
        for v2 in outs[v]:
            in_cnt[v2] -= 1
            if in_cnt[v2] == 0:
                queue.append(v2)

    return res

# 0-index
def topological(n, dist):
    in_cnt = defaultdict(int)
    outs = defaultdict(list)

    for a, b in dist:
        in_cnt[b] += 1
        outs[a].append(b)

    res = []
    queue = deque([i for i in range(n) if in_cnt[i] == 0])

    while len(queue) != 0:
        v = queue.popleft()
        res.append(v)
        for v2 in outs[v]:
            in_cnt[v2] -= 1
            if in_cnt[v2] == 0:
                queue.append(v2)

    return res

# [2, 3, 1, 4, 0, 5, 6, 7]
# queryに閉路ができる道を追加するとバグってlen = 8未満の配列を返す
print(topological(N, ab))

# degは入次数を記録したもの
def topological(graph, deg):
    start = []
    n = len(deg)
    for i in range(n):
        if deg[i] == 0: #入次数がないものがスタート
            start.append(i)
    topo = []
    while start:
        v = start.pop()
        topo.append(v)
        for u in graph[v]:
            deg[u] -= 1
            if deg[u] == 0:
                start.append(u)
    #トポロジカルソートできない場合は配列がnよりも短くなる。
    return topo

# トポロジカルソートの種類の数
N, M = 3, 2
query = [
[2, 1],
[2, 3]
]

X = [0] * N
for i in range(M):
    x, y = query[i]
    # xにある矢印を集計
    X[x - 1] |= 1 << (y - 1)

DP = [0] * (1 << N)
DP[0] = 1

# jの左に置くものとしてどのような組み合わせがあるか
for bit in range(1, 1 << N):
    for j in range(N):
        # j番目が含まれる場合において
        if bit & (1 << j):
            if not (X[j] & (bit ^ (1 << j))):
                # 上のbitまで運送してってdp[-1]で集計
                DP[bit] += DP[bit ^ (1 << j)]
print(DP)

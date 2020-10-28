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

# https://qiita.com/Morifolium/items/6c8f0a188af2f9620db2
N = 8

ab = [
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
"""
for _ in range(N + M - 1):
    ab.append(tuple(map(int, input().split())))
"""

def topological(n, dist):
    in_cnt = defaultdict(int)
    outs = defaultdict(list)

    for a, b in ab:
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

# [2, 3, 1, 4, 0, 5, 6, 7]
# queryに閉路ができる道を追加するとバグってlen = 8未満の配列を返す
print(topological(N, ab))

# ABC041 D - 徒競走
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

# 全国統一プログラミング王決定戦予選 D - Restore the Tree

"""
元のN頂点N - 1辺の根付き有向辺グラフ + 新たにM本の有向辺
元の木は一意に定まることが示せる。

邪魔なM本を消せ
木にするためには
ループを消す
B側に根以外の各頂点がN - 1個あるようにすればいい
他には？
適当に辺を選んでいくが、最終的に連結である必要がある

6 3
2 1
2 3
4 1
4 2
6 1
2 6
4 6
6 5の場合

1: [2, 1], [4, 1], [6, 1]
2: [4, 2]
3: [6, 3]
4: [] 親になるものがすぐわかることもある
5: [6, 5]
6: [2, 6], [4, 6]

切り離しても連結のママのものは？
MのA,Bについて、Bは元の根付き木に置けるAの子孫である
親方向へは伸びない
なのでトポソする
"""

N, M = getNM()
dist = [getList() for i in range(N + M - 1)]
edges = [[] for i in range(N)] # 親要素の候補
for a, b in dist:
    edges[b - 1].append(a - 1)

# トポソする
# 順番が求まる
res = topological(N, dist)

ans = [-1] * N
ans[res[0]] = 0
depth = [-1] * N
depth[res[0]] = 0

# 追加のM辺はショートカットになるので
# 元の根付き木は辺のうち深さが最も深くなるもの

for i in res[1:]: # 二番手以降について調べる
    parent = 0
    dep_opt = 0
    for j in edges[i]: # iの各親について深さを調べる
        if depth[j] + 1 > dep_opt: # 更新できるなら
            parent = j
            dep_opt = depth[j] + 1
    ans[i] = parent + 1
    depth[i] = dep_opt

for i in ans:
    print(i)

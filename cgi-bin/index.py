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
mod = 998244353

#############
# Main Code #
#############

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parents[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

# ABC002 派閥
# 条件
# n人の国会議員の集合A{A1, A2... An}の任意の二人i, jについて
# (i, j)がqueryに含まれる

# この人数nの最大値を求める

# 集合Aの取り方は？
# N <= 12なのでbit全探索で全ての集合について条件を満たすか判定できる
N, M = getNM()
mem = set()
for i in range(M):
    a, b = getNM()
    mem.add((a - 1, b - 1))

ans = 0
for bit in range(1 << N):
    # 任意のi, jについてqueryに含まれているか判定
    flag = True
    for i in range(N):
        for j in range(i + 1, N):
            # 適当に選んだ２人がbitの中に含まれていれば
            if bit & (1 << i) and bit & (1 << j):
                if not (i, j) in mem:
                    flag = False
    # もし集合bitが条件を満たすなら人数を調べる
    if flag:
        opt = bin(bit).count('1')
        ans = max(ans, opt)
print(ans)

# ABC040 D - 道路の老朽化対策について
# 人によって通れる橋が限定される場合がある
# クエリソートしてUnion Find

N, M = getNM()
bridge = [getList() for i in range(M)]
Q = getN()
resident = []
for i in range(Q):
    a, b = getNM()
    resident.append([a, b, i])

bridge.sort(reverse = True, key = lambda i:i[2])
resident.sort(reverse = True, key = lambda i:i[1])

U = UnionFind(N)

ans = []
index = 0
for i in range(Q):
    # 建築年が新しい順に橋をかけていく
    for j in range(index, M):
        if bridge[j][2] > resident[i][1]:
            a, b, c = bridge[j]
            U.union(a - 1, b - 1)
        else:
            index = j
            break
    # U.sizeで判定
    ans.append([resident[i][2], U.size(resident[i][0] - 1)])

# 国民を登場順にソート
ans.sort(key = lambda i: i[0])
for i in ans:
    print(i[1])

# ABC097 D - Equals
# 同じ島のところにしか飛べない
N, M = getNM()
# 1 ~ 5の並び替え
# これを1, 2, 3, 4, 5にしたい
P = getList()
# Pのうちのペア
query = []
for i in range(M):
    a, b = getNM()
    query.append([a, b])

U = UnionFind(N)
for i in range(M):
    a, b = query[i]
    U.union(a - 1, b - 1)

cnt = 0
for i in range(N):
    if U.same(P[i] - 1, i):
        cnt += 1

print(cnt)

# ABC120 D - Decayed Bridges
# クエリソート
N, M = getNM()
query = [getNM() for i in range(M)]

U = UnionFind(N)
now = cmb_list[N]
ans = [now]

for i in range(M - 1, 0, -1):
    a, b = query[i]
    size_a = 0
    size_b = 0
    if not U.same(a - 1, b - 1):
        size_a = U.size(a - 1)
        size_b = U.size(b - 1)

        U.union(a - 1, b - 1)
        size_after = U.size(a - 1)

        now -= (cmb_list[size_after] - cmb_list[size_a] - cmb_list[size_b])
    else:
        U.union(a - 1, b - 1)
    ans.append(now)

for i in range(M - 1, -1, -1):
    print(ans[i])

# ABC126 E - 1 or 2
# カードN枚
# 各カードには1か2が書かれている
N, M = getNM()
# A1 + A2 + 1は偶数
query = []

for i in range(M):
    a, b, c = getNM()
    query.append([a, b, c])

U = UnionFind(N)
for i in query:
    U.union(i[0] - 1, i[1] - 1)

print(U.group_count())

# ABC157 D - Friend Suggestions
N, M, K = getNM()
F = [getList() for i in range(M)]
B = [getList() for i in range(K)]

# 友人候補の数を答える
# 各人につきO(1)で答える

# 集合の足し引きで答える
# U.same(a) = {aと友人関係にあるもの、aとブロック関係、その他}
# U.same(a) - aと友人関係にあるもの - aとブロック関係が答え
# まずUnionfind

U = UnionFind(N)
for a, b in F:
    U.union(a - 1, b - 1)

# U.same(i)の人数を答える
ans = [0] * N
for i in range(N):
    ans[i] = U.size(i)

# U.same内のaと友人関係にあるもの, aとブロック関係にあるものを引く
# 同じグループ内にいる時だけ関係する
for a, b in F:
    if U.same(a - 1, b - 1):
        ans[a - 1] -= 1
        ans[b - 1] -= 1

for c, d in B:
    if U.same(c - 1, d - 1):
        ans[c - 1] -= 1
        ans[d - 1] -= 1

ans = [i - 1 for i in ans] # 自身を引く
print(*ans)

# 各1 ~ Nに交易所を立てるのを0~Nにエッジを貼るのに見立てる
N, M = getNM()
edges = []
for i in range(N):
    c = getN()
    edges.append((c, 0, i + 1))
for i in range(M):
    s, t, w = getNM()
    edges.append((w, s, t))
edges.sort()

def kruskal(n, edges):
    U = UnionFind(n)
    res = 0
    for e in edges:
        w, s, t = e
        if not U.same(s, t):
            res += w
            U.union(s, t)
    return res
print(kruskal(N + 1, edges))

# 駐車場
N, M, S = getNM()
S -= 1
dist = [[] for i in range(N)]
for i in range(M):
    v1, v2 = getNM()
    v1 -= 1
    v2 -= 1
    v1, v2 = min(v1, v2), max(v1, v2)
    dist[v1].append(v2)

U = UnionFind(N)

ans = []
for i in range(N - 1, -1, -1):
    # 地点iに車を駐める場合、一端がiの道は使えない
    # → iに車を停める以前であれば,一端がiの道を使える
    for j in dist[i]:
        U.union(i, j)
    if U.same(i, S):
        ans.append(i + 1)
ans.sort()
for i in ans:
    print(i)

# ABC065 built?
# xでソート、yでソートし、それぞれ
# abs(a - b)とabs(c - d)のエッジをそれぞれ加える
# どちらか短い方が使われる
N = getN()
query = []
for i in range(N):
    a, b = getNM()
    query.append([a, b, i])

q_a = sorted(query, key = lambda i: i[0])
q_b = sorted(query, key = lambda i: i[1])
edges = []

a1 = q_a[0]
b1 = q_b[0]
for i in range(1, N):
    a2 = q_a[i]
    b2 = q_b[i]
    edges.append([abs(a1[0] - a2[0]), a1[2], a2[2]])
    edges.append([abs(b1[1] - b2[1]), b1[2], b2[2]])
    a1, b1 = a2, b2
edges.sort()

def kruskal(n, edges):
    U = UnionFind(n)
    res = 0
    for e in edges:
        w, s, t = e
        if not U.same(s, t):
            res += w
            U.union(s, t)
        if U.size(0) == N:
            break
    return res
print(kruskal(N, edges))

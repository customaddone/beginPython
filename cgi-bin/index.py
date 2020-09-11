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

N = getN()

L = [[] for i in range(N)]
for i in range(N - 1):
    a, b = getNM()
    L[a - 1].append(b - 1)
    L[b - 1].append(a - 1)

U = 2 * 10 ** 5

# 逆元事前処理ver
# nが小さい場合に
lim = 2 * 10 ** 5
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, lim + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    # 累計
    factinv.append((factinv[-1] * inv[-1]) % mod)

def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod

# 親i、根jの部分木のサイズ、通りの数
memo=[[[0, 0]for i in range(N)]for j in range(N)]

def dp(r, v):
    if memo[r][v] != [0,0]:
        return memo[r][v]

    # 子ノードの部分木の大きさについてレコードする
    ll = []
    res = 1
    size = 0

    for i in L[v]:
        if i != r:
            p, q = dp(v, i)
            size += p # 子ノードの部分木のサイズを足す
            ll.append(p)
            res = res * q % mod # 子ノードの通りの数をかける

    t = size
    # 通りの数を計算する
    for i in ll:
        # 全体のうちどの場所にいるか
        # ○○1○○1○1○ →
        # ○2●○2●○●○ → ...
        res = res * cmb(t, i) % mod
        t -= i

    memo[r][v] = [size + 1, res]

    return size + 1, res

ans = 0
for i in range(N):
    ans = (ans + dp(i, i)[1]) % mod
print((ans * pow(2, mod - 2, mod)) % mod)

"""
edges = [[] for i in range(N + 1)]
for _ in range(N - 1):
    a, b = getNM()
    edges[a].append(b)
    edges[b].append(a)

D = [[-1] * (N + 1) for _ in range(N + 1)] # 通りの数
S = [[0] * (N + 1) for _ in range(N + 1)] # 親iの根jの部分木のサイズ
ans = 0

def f(i, j):
    if D[i][j] == -1:
        D[i][j] = 0

    for k in edges[j]:
        if k != i:
            f(j, k) # 木を探索
            S[i][j] += S[j][k] # 各子ノードの部分木のサイズを足す

    S[i][j] += 1 # 自身
    R = math.factorial(S[i][j] - 1)

    for k in edges[j]:
        if k != i:
            R *= D[j][k] // math.factorial(S[j][k])
    D[i][j] = R

    return D[i][j]

for i in range(1, N + 1):
    a += f(0, i)
    print(S)

# a ~ bを先に書き始める場合についてa ~ bを縮約して求められるが
# a, bを計算して // 2もできる
print((a // 2) % (10 ** 9 + 7))
"""

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

# mod不使用ver
def cmb_1(n, r):
    r = min(n - r, r)
    if (r < 0) or (n < r):
        return 0

    if r == 0:
        return 1

    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

# 10
print(cmb_1(5, 3))

# mod使用ver
# nが大きい場合に
def cmb_2(x,y):
    r = 1
    for i in range(1, y + 1):
        r = (r * (x - i + 1) * pow(i, mod - 2, mod)) % mod
    return r

# 10
print(cmb_2(5, 3))

# 逆元事前処理ver
# nが小さい場合に
lim = 10 ** 6 + 1
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

    if r == 0:
        return 1
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod
# 120
print(cmb(10, 3))

# 重複組み合わせ
# 10個のものから重複を許して3つとる
print(cmb_1(10 + 3 - 1, 3))

# modが素数じゃない時
def cmb_compose(n, k, mod):
    dp = [[0] * (k + 1) for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        dp[i][0] = 1
        for j in range(1, k + 1):
            # nCk = n - 1Ck - 1 + n - 1Ck
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod

    return dp[n][k]

print(cmb_compose(10, 3, 50))

A, B, C = 144949225, 545897619, 393065978

# kCc / k+1Cc = k - c + 1 / k + 1
# k+1Cc+1 / kCc = k + 1 / c + 1
# Xを10 ** 9 + 7 - 2乗すると逆元が求まる
x = (C * pow(A, mod - 2, mod)) % mod
y = (B * pow(A, mod - 2, mod)) % mod

n = (x + y - 2 * x * y) * pow(x * y - x - y, mod - 2, mod)
k = (y - x * y) * pow(x * y - x - y, mod - 2, mod)
print((n - k) % mod, k % mod)


# 再帰で組み合わせ
N = 4
L = [1, 1]
root = 5

# root ** Nでループ
def four_pow(i, array):
    global cnt
    if i == N:
        print(array)
        return
    for j in range(root):
        new_array = array + [j]
        four_pow(i + 1, new_array)
# four_pow(0, [])

# 組み合わせ
def comb_pow(i, array):
    global cnt
    if i == N:
        print(array)
        return
    # ここの4を変えてrootを変更
    last = -1
    if len(array) > 0:
        last = array[-1]

    for j in range(last + 1, root):
        new_array = array + [j]
        comb_pow(i + 1, new_array)
#comb_pow(0, [])

# 1スタート
def comb_pow_2(i, array):
    global cnt
    if i == N:
        print(array)
        return
    # ここの4を変えてrootを変更
    last = 0
    if len(array) > 0:
        last = array[-1]

    for j in range(last + 1, root + 1):
        new_array = array + [j]
        comb_pow_2(i + 1, new_array)
# comb_pow_2(0, [])

# 重複組み合わせ
def rep_comb_pow(i, array):
    global cnt
    if i == N:
        print(array)
        return
    # ここの4を変えてrootを変更
    last = 0
    if len(array) > 0:
        last = array[-1]

    for j in range(last, root):
        new_array = array + [j]
        rep_comb_pow(i + 1, new_array)
# rep_comb_pow(0, [])

N = 2
root = 5

# 1スタート
def rep_comb_pow_2(i, array):
    global cnt
    if i == N:
        print(array)
        return

    last = 0
    if len(array) > 0:
        last = array[-1]

    for j in range(last + 1, root + 1):
        new_array = array + [j]
        rep_comb_pow_2(i + 1, new_array)
# rep_comb_pow_2(0, [])

N, K = 10, 5

c1 = cmb(N, K)

# 完全順列（モンモール数）
dp = [0] * (K + 1)
dp[2] = 1
for i in range(3, K + 1):
    dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % mod
c2 = dp[K]

ans = c1 * c2 % mod
print(ans)

# ABC154F many many paths
# 経路組み合わせ

### ここ注意 ###
lim = 2 * (10 ** 6) + 7
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

    if r == 0:
        return 1

    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod

"""
g(r,c) を 0 ≤ i ≤ r かつ 0 ≤ j ≤ c を満たす全ての整数の組 (i,j) に対する f(i,j) の総和とする。
ここでf(r + 1, c) = f(r, c) + f(r, c - 1)...f(r, 0)
f(r, c)からr方向へ1つ（一通り）
f(r, c - 1)からr方向へ1つ, c方向に1つ（一通り）
...

つまりf(r2 + 1, c2) = f(r2, c) + f(r2, c - 1) + ... f(r2, 0)
これをf(0, c2)からf(r2 + 1, c2)まで求めればg(r2, c2)が求まる
"""
r1, c1, r2, c2 = 1, 1, 2, 2

ans = 0
for i in range(r1, r2 + 1):
    ans = (ans + cmb(c2 + i + 1, i + 1) - cmb(c1 + i, i + 1)) % mod
print(ans)

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

# 逆元事前処理ver
# nが小さい場合に
lim = 10 ** 6 + 1
fact = [1, 1]
factinv = [1, 1] # 1/n!(mod n)
inv = [0, 1] # 1/n (mod n)

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
# 120
print(cmb(10, 3))

# mod使用ver
# nが大きい場合に
def cmb_2(x, y):
    r = 1
    for i in range(1, y + 1):
        r = (r * (x - i + 1) * inv[i]) % mod
    return r

# 10
print(cmb_2(5, 3))

lim = 10 ** 6 + 1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, lim + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    # 累計
    factinv.append((factinv[-1] * inv[-1]) % mod)

# 階乗
def factorial(n, r):
    if (r < 0) or (n < r):
        return 0
    return fact[n] * factinv[n - r] % mod

# print(factorial(5, 3))

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

mod = [0]
pw = 1
# c = 1817181712114なら
# 4, 14, 114, 2114のmodでのあまりを出す
for c in input()[::-1]:
    mod.append((int(c) * pw + mod[-1]) % 2019)
    pw = pw * 10 % 2019
from collections import *

print(sum(v * (v - 1) // 2 for v in Counter(mod).values()))

# F - Knapsack for All Segments
# mod Pの計算

N, P = getNM()
C = input()[::-1]

if P == 2:
    ans = 0
    for i in range(N):
        if int(C[i]) % 2 == 0:
            ans += N - i
    print(ans)

elif P == 5:
    ans = 0
    for i in range(N):
        if int(C[i]) == 0 or int(C[i]) == 5:
            ans += N - i
    print(ans)

else:
    mod = [0]
    pw = 1 # 10 ** iをPで割った時の余り
    for c in C:
        mod.append((int(c) * pw + mod[-1]) % P)
        pw = pw * 10 % P # 10 ** iをPで割った時の余りから10 ** (i + 1)をPで割った時の余りを求める

    print(sum(v * (v - 1) // 2 for v in Counter(mod).values()))

# ABC149 F - Surrounded Nodes
# 特殊なmodでの出力方法
# 逆元の出し方
# xz ≡ y(mod 10 ** 9 + 7)を満たすような　の問題で使う

N = getN()
E = [[] for i in range(N)]
for i in range(N - 1):
    s, t = getNM()
    E[s - 1].append(t - 1)
    E[t - 1].append(s - 1)

ans = 0

# 2^(N - 1) - 1 - (2^(ciの大きさ) - 1の合計)
# を求めていく
def dfs(u, par):
    global ans
    res = 1
    add = pow(2, N - 1, mod) - 1
    for v in E[u]:
        if v != par:
            size_c = dfs(v, u)
            # 2^(ciの大きさ) - 1
            add -= (pow(2, size_c, mod) - 1)
            add %= mod
            res += size_c
    # 最後に親方向に行く部分木の分を引く
    add -= (pow(2, N - res, mod) - 1)
    add %= mod
    ans += add
    ans %= mod

    return res

dfs(0, -1) # 実行
deno = pow(2, N, mod)
# denoの逆元の出し方（pythonでしかできません）
print((ans * pow(deno, -1, mod)) % mod)
# pypyでもできる
print((ans * pow(deno, mod - 2, mod)) % mod)

# M-SOLUTION プロコン　C - Best-of-(2n-1)
# 分子分母が巨大な場合

lim = 10 ** 6 + 1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, lim + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod

N, A, B, C = getNM()
a_pow = [1] * (10 ** 6 + 1)
b_pow = [1] * (10 ** 6 + 1)
for i in range(1, 10 ** 6 + 1):
    a_pow[i] = (a_pow[i - 1] * A) % mod
    b_pow[i] = (b_pow[i - 1] * B) % mod

ans = 0

for i in range(N):
    prob = ((cmb(N + i - 1, i) * a_pow[N - 1] * b_pow[i]) * A) % mod
    prob *= pow(A + B, N - i - 1, mod)
    prob %= mod

    exp = 100 * (N + i)
    ans += prob * exp
    ans %= mod

for i in range(N):
    prob = ((cmb(N + i - 1, i) * a_pow[i] * b_pow[N - 1]) * B) % mod
    prob *= pow(A + B, N - i - 1, mod)
    prob %= mod

    exp = 100 * (N + i)
    ans += prob * exp
    ans %= mod

# この問題は 15625000000000 / 100000000000000 とかをmodで表すことになる問題
# 巨大数の場合は、まず分子分母をそれぞれmodして計算すればできる
# 分母の逆元の計算はこうやる
deno = (pow(A + B, 2 * N, mod)) % mod
print((ans * pow(deno, mod - 2, mod)) % mod)

# エクサウィザーズ2019 E - Black or White
# 冪乗の逆元を求める

B, W = getNM()
b_dep, w_dep = 0, 0
b_sto, w_sto = 0, 0

### 前処置部分 #############################
bi = [1] * (10 ** 6) # 冪乗のmod
bi_pow = [1] * (10 ** 6) # 冪乗の逆元のmod
rev = pow(2, mod - 2, mod)
for i in range(1, 10 ** 6):
    bi[i] = (bi[i - 1] * 2) % mod
    bi_pow[i] = (bi_pow[i - 1] * rev) % mod # 2^0, 2^1, 2^2...の逆元を前計算
###########################################

for i in range(B + W):
    b_dep = (cmb(i, B) + b_sto) % mod
    b_sto = (b_sto + b_dep) % mod
    w_dep = (cmb(i, W) + w_sto) % mod
    w_sto = (w_sto + w_dep) % mod

    # 冪乗の逆元のmodをこのように使える
    print(((bi[i] + w_dep - b_dep) * bi_pow[i + 1]) % mod)

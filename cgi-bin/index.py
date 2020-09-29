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

# ABC008 C - コイン
n = getN()
c = getArray(n)
sumans = 0

for i in c:
    lista = [j for j in c if i % j == 0]
    count = len(lista)
    sumans += math.ceil(count / 2) / count
print(sumans)

# ABC011 D - 大ジャンプ
def cmb_1(n, r):
    r = min(n - r, r)
    if (r < 0) or (n < r):
        return 0

    if n == 0:
        return 1

    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

N, D = getNM()
X, Y = getNM()
X = abs(X)
Y = abs(Y)

# X軸に平行に正の向きに飛ぶ回数はx_time + α回
# X軸に平行に負の向きに飛ぶ回数はα回
x_time = X // D
y_time = Y // D

if X % D != 0 or Y % D != 0 or N < x_time + y_time:
    print(0)
    exit()

N_a = N - (x_time + y_time)
if N_a % 2 != 0:
    print(0)
    exit()
N_a //= 2

ans = 0
for i in range(N_a + 1):
    ans += cmb_1(N, x_time + i) * cmb_1(N - (x_time + i), i) * cmb_1(N - (x_time + 2 * i), y_time + N_a - i)
print(ans / (4 ** N))

# ABC024 D - 動的計画法
A, B, C = getArray(3)

# kCc / k+1Cc = k - c + 1 / k + 1
# k+1Cc+1 / kCc = k + 1 / c + 1
# Xを10 ** 9 + 7 - 2乗すると逆元が求まる
x = (C * pow(A, mod - 2, mod)) % mod
y = (B * pow(A, mod - 2, mod)) % mod

n = (x + y - 2 * x * y) * pow(x * y - x - y, mod - 2, mod)
k = (y - x * y) * pow(x * y - x - y, mod - 2, mod)
print((n - k) % mod, k % mod)

# ABC058 D - いろはちゃんとマス目
# 総計する
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
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod

H, W, A, B = getNM()

mother = cmb((H - 1) + (W - 1), (W - 1))

goban = cmb((H - A) + (B - 1), B - 1)
togoal = cmb((A - 1) + (W - B - 1), (W - B - 1))

for i in range(A):
    row = H - A + i
    col = B - 1
    row_left = A - 1 - i
    col_left = W - B - 1
    mother -= cmb(row + col, row) * cmb(row_left + col_left, row_left)
    mother %= mod
print(mother)

# ABC057 D - Maximum Average Sets
N, A, B = getNM()
V = sorted(getList(), reverse = True)

# 1行目の答え　上からA個
print(sum(V[:A]) / A)

# Vの各要素の数を数える
dict = defaultdict(int)
for i in range(N):
    dict[V[i]] += 1

r = A
n = 0
for i in dict.items():
    print(i)
    if r - i[1] >= 0:
        r -= i[1]
    else:
        n = i[1] # A個まで残りr個であり、そこには要素i[j]がn個入れられる
        break

ans = 0
# V[0] == V[A - 1]ならA個を超えても平均値が下がらない
# 残りr個(合計でA個)決める、残りr + 1個(合計でA + 1個)決める...合計でB個決める
if r > 0 and V[0] == V[A - 1]:
    for i in range(r, B + 1):
        ans += cmb_1(n, i)
else:
    ans += cmb_1(n, r) # A個まであとr個残っており、n個のうちr個選ぶ

print(ans)

# ABC066 D - 11
# 普通にやれば(cmb(N + 1, i)だが、今回ダブりがある
# 29 19 ~ 19 31 9の場合
# [29]のうちいくつか + １番目の19 + [31, 9]のうちいくつかと
# [29]のうちいくつか + ２番目の19 + [31, 9]のうちいくつかはダブル
# i個要素を選ぶとすると、19を選び、外側の要素からi - 1個選ぶ全通りについてダブルので１回引く
N = getN()
A = getList()

lista = [0] * (max(A) + 1)
double = 0
# ダブり位置1を決める
dou_ind_2 = 0
for i in range(N + 1):
    if lista[A[i]] > 0:
        double = A[i]
        dou_ind_2 = i
        break
    lista[A[i]] += 1
# ダブり位置2を決める
dou_ind_1 = 0
for i in range(N + 1):
    if A[i] == double:
        dou_ind_1 = i
        break

outer = dou_ind_1 + (N - dou_ind_2)

for i in range(1, N + 2):
    if i == 1:
        print(N)
        continue
    print((cmb(N + 1, i) - cmb(outer, i - 1)) % mod)

# ABC105 D - Candy Distribution
# M人に配る mod M
N, M = getNM()
A = getList()

alta = []
for i in A:
    alta.append(i % M)

imos = [0]
for i in range(N):
    imos.append((alta[i] + imos[i]) % M)

ans = 0
for i in Counter(imos).values():
    ans += cmb_1(i, 2)
print(ans)

# ABC136 E - Max GCD
N, K = getNM()
A = getList()

# 操作後のAの要素全てが因数にkを持つ

# 好きな回数操作を行えるとすると、Aの要素全てに因数kを持たせることができるか？
# 操作前と操作後とではAの総和は変わらない → A = akとするとa個のkをN個の要素に配分する
# ことでAの要素全てに因数kを持たせることができる。
# 好きな回数操作を行える、操作後のAの全ての要素を割り切る正の整数は、sum(A)の約数になる

def make_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            # √nで無い数についてもう一個プラス
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

# K回以下の操作の条件付きでも題意を満たすか
# alta % kをし、あまりが小さい順にソートする
# 前からi番目までをプラス、i + 1番目以降をマイナスにする
# どちらか大きい方がK以下なら条件を満たす

def judger(x):
    alta = [i % x for i in A]
    alta.sort()
    alta_b = [x - i for i in alta]
    # 前からi番目までプラスにする
    imos_f = copy.deepcopy(alta)
    # 前からi + 1番目以降をマイナスにする
    imos_b = copy.deepcopy(alta_b)

    for i in range(N - 1):
        imos_f[i + 1] += imos_f[i]
        imos_b[-i - 2] += imos_b[-i - 1]

    # 全部マイナス、全部プラスの場合
    imos_f.insert(0, 0)
    imos_b.append(0)

    ans = float('inf')
    for i in range(N + 1):
        ans = min(ans, max(imos_f[i], imos_b[i]))

    return ans

for i in make_divisors(sum(A))[::-1]:
    if judger(i) <= K:
        print(i)

# ABC154 F - Many Many Paths
"""
g(r,c) を 0 ≤ i ≤ r かつ 0 ≤ j ≤ c を満たす全ての整数の組 (i,j) に対する f(i,j) の総和とする。
ここでf(r + 1, c) = f(r, c) + f(r, c - 1)...f(r, 0)
f(r, c)からr方向へ1つ（一通り）
f(r, c - 1)からr方向へ1つ, c方向に1つ（一通り）
...
つまりf(r2 + 1, c2) = f(r2, c) + f(r2, c - 1) + ... f(r2, 0)
これをf(0, c2)からf(r2 + 1, c2)まで求めればg(r2, c2)が求まる
"""
r1, c1, r2, c2 = getNM()

ans = 0
for i in range(r1, r2 + 1):
    ans = (ans + cmb(c2 + i + 1, i + 1) - cmb(c1 + i, i + 1)) % mod
print(ans)

# ABC171 F - Strivore
"""
dp[i][j]を
「i文字目まででj回Sの文字を使ったか」とする

K = 5
S = 'oof'
dp = [[0] * (len(S) + 1) for i in range(K + len(S) + 1)]
dp[0][0] = 1

for i in range(1, K + len(S) + 1):
    for j in range(len(S) + 1):
        if j < len(S):
            dp[i][j] += dp[i - 1][j] * 25
        else:
            dp[i][j] += dp[i - 1][j] * 26 # j回使い切るともうSは関係なくなるので *= 26になる
        if j >= 1:
            dp[i][j] += dp[i - 1][j - 1]

l_s = len(S)
どのタイミングで「この先ずっと*= 26」になるか
後ろからi文字目にSを使い切る: pow(25, K - k, mod) * cmb(N + K - k - 1, N - 1) * pow(26, k, mod)
...
"""

K = getN()
S = input()
N = len(S)

ans = 0
# l_s + i文字目に文字を使い切る
# 次から *= 26
for k in range(K + 1):
    # 逆からやってる
    ans += cmb(N + K - k - 1, N - 1) * pow(26, k, mod) * pow(25, K - k, mod) % mod
    ans %= mod

print(ans)

# ARC023 C - タコヤ木
N = getN()
A = getList()

def cmb(x,y):
    r = 1
    for i in range(1, y + 1):
        r = (r * (x - i + 1) * pow(i, mod - 2, mod)) % mod
    return r

now = A[0]
cnt = 0
ans = 1
for i in range(1, N):
    if A[i] > -1:
        if cnt > 0:
            ans *= cmb(A[i] - now + cnt, cnt)
            ans %= mod
            now = A[i]
            cnt = 0
        else:
            now = A[i]
    else:
        cnt += 1
print(ans)

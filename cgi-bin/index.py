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

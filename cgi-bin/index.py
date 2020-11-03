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
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod
# 120
print(cmb(10, 3))

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

# ABC008 C - コイン

n = getN()
c = getArray(n)
sumans = 0

for i in c:
    lista = [j for j in c if i % j == 0]
    count = len(lista)
    sumans += math.ceil(count / 2) / count
print(sumans)

# 第6回 ドワンゴからの挑戦状 予選 B - Fusing Slimes

"""
操作をN - 1回行う
1 ~ N - 1のどれかを右隣のスライムの位置まで移動させる　そして消す
その通りは(N - 1)!通りあるがそれの総和を求めよ
考え方を変えてみるか

3
1 2 3　の場合

  2 3 →    3 1 + 1移動
1   3 →    3 1 + 2移動 答えは5

1の移動する距離 + 2の移動する距離 +...
1が移動する距離の通りは？
1 2 3 4 の場合 3! = 6通り
距離1: 1番目に1が選択される 2! = 2, 3 → 1 3通り
2が選択されない状態で1が選ばれる
距離2: 2 → 1 1通り
距離3: 3 → 2 → 1, 2 → 3 → 1

距離1:
1 2この順番は確定
残りの3については○ 1 ○ 2 ○　の3箇所のどこかに置く

距離2:
同様に○ 1 ○ 3 ○ だが
○ 1 2 3 ○ と ○ 1 ○ 3 2　はダブりがあるので引く

(既に置いたものの順列) 1 (target) その他についてはこれの間に自由に置いて良い
startが2の場合は1がどの時点で選ばれても強制でその他にしても問題ない
N <= 10 ** 5
うまくまとめる

case1
start1: 1
next1: 2
と
case2
start2: 2
next2: 3
はそれぞれ

○ start ○ next ○　になるので通りの数は同じ
つまり同じ距離のindexを移動する場合は通りの数が同じ　その通りの数は距離をiとすると
n = (i - 1)! + 2 既に置いたものの順列 + start + next + 1
r = (N - 1) - (i + 1) の nPr i <= N - 2
距離N - 1は(N - 2)!

同じ距離のindexを移動する場合は通りの数が同じ
o = (既に置いたもの(i - 1) + 自身)とすると
o + 1に残りのもの - 1を置いていく
(i - 1)! * (N - 2) // oが N-1Po+1が通りの数

N個目がゴールであるものは別にする

まとめて計算するのには変わりはない
1 2 3 4の時
3 が 4に飛ぶ確率 1
2 が 4に飛ぶ確率　先に3が選ばれないといけない 1 / 2
1 が 4に飛ぶ確率　先に2, 3が選ばれないといけない 1 / 3 * 1 / 2 * 2!
...
1 が xに飛ぶ確率　先に2, 3...x - 1が選ばれないと 1 / (x - 1) * (1 / (x - 2)... * (x - 2)!)消える
これに(n - 1)!をかける

各区間についてどのスライムが通過するかをまとめる
"""

N = getN()
X = getList()
MOD = 10 ** 9 + 7

S = 0
res = 0
F = 1
# 小さいスケールのものから考える
for i in range(1, N): # 区間0 ~ 1, 1 ~ 2...を通過するか
    S += pow(i, MOD - 2, MOD) # 1, 1 / 2, 1 / 3...をその都度足していく
    res += (X[i] - X[i - 1]) * S # S = 1 + 1 / 2 + 1 / 3...
                                 # これは1: i - 1がi - 1 ~ iを通過する確率、 i - 2が...
    res %= MOD
    F *= i # 最終的に(N - 1)!になる
    F %= MOD
print(res * F % MOD)

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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# 行列掛け算

N = 10
logk = N.bit_length()

# [Fi+2, Fi+1] = [[1, 1], [1, 0]][Fi+1, Fi]
# 一般項が出ない漸化式は行列の形に落とし込める
dp = [[[0, 0] for i in range(2)] for i in range(logk)]
dp[0] = [[1, 1], [1, 0]]

# 行列掛け算 O(n3)かかる
def array_cnt(ar1, ar2):
    h = len(ar1)
    w = len(ar2[0])
    row = ar1
    col = []
    for j in range(w):
        opt = []
        for i in range(len(ar2)):
            opt.append(ar2[i][j])
        col.append(opt)

    res = [[[0, 0] for i in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            cnt = 0
            for x, y in zip(row[i], col[j]):
                cnt += x * y
            res[i][j] = cnt
    return res

for i in range(1, logk):
    dp[i] = array_cnt(dp[i - 1], dp[i - 1])

# 行列の単位元
ans = [[1, 0], [0, 1]]
for i in range(logk):
    if N & (1 << i):
        ans = array_cnt(ans, dp[i])

# AND XORの半環の性質を使う
# 掛け合わせするCが固定なので行列累乗できるのん
# ANDを掛け算、XORを足し算だと思え

K, M = getNM()
A = getList()
C = getList()

if M <= K:
    print(A[M - 1])
    exit()

# 行列累乗
# res: 横 mat: 縦
k = M - K
logk = k.bit_length()
dp = [[[0] * K for j in range(K)] for i in range(logk)]
# 初項を書き込む
for i in range(K - 1):
    dp[0][K - i - 2][i] = 2 ** 32 - 1
for i in range(K):
    dp[0][i][-1] = C[i]

def array_cnt(ar1, ar2):
    h = len(ar1)
    w = len(ar2[0])
    row = ar1
    col = []
    for j in range(w):
        opt = []
        for i in range(len(ar2)):
            opt.append(ar2[i][j])
        col.append(opt)

    res = [[[0, 0] for i in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            cnt = 0
            for x, y in zip(row[i], col[j][::-1]): # 計算は逆になる
                # (整数) +, *
                # (整数) ^, &
                # (整数) max, +
                # (行列) +, *
                # は半環の性質をもつため行列累乗できる
                cnt ^= x & y # ここを変更
            res[i][j] = cnt
    return res

for i in range(1, logk):
    dp[i] = array_cnt(dp[i - 1], dp[i - 1])

ans = [A]
for i in range(logk):
    if k & (1 << i):
        ans = array_cnt(ans, dp[i])

print(ans[0][-1])

# mod付き行列累乗
def array_cnt(ar1, ar2, m):
    h = len(ar1)
    w = len(ar2[0])
    row = ar1
    col = []
    for j in range(w):
        opt = []
        for i in range(len(ar2)):
            opt.append(ar2[i][j])
        col.append(opt)

    res = [[[0, 0] for i in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            cnt = 0
            for x, y in zip(row[i], col[j]):
                cnt += x * y
            res[i][j] = cnt
            res[i][j] %= m
    return res

# rank数を求める
# ZONeコン F-出会いと別れ

"""
Aに含まれないものの集合をBとする
a xor b になるようなab間に辺を張った時にN頂点は連結になるか？

連結になる = 任意の点からいくつか通って他の任意の場所に行けるか
つまり0から始めて0 ~ N - 1のどこにでも行ける
a xor b = Bとなるなら a xor B = bとなり
0 xor B1 = (0 ~ N - 1のどれか)になる　これを繰り返すと
0から任意の場所に行けるということに　N個の線型独立したbit棒があればいい

集合B内でxorを繰り返して任意の数字を作るには、N個の線型独立したベクトルがあればいい
"""

N, M = getNM()
A = set(getList())
B = [i for i in range(1, N) if not i in A]

# Bの値をbit表記にした時の線形独立な要素を求める
def rank(array):
    base = [] # 元の数字
    elim = [] # 消す用

    # Bの小さい順に全て試す
    for x in array:
        y = x
        for b in elim:
            # 小さい数字を使ってフラグを消していく
            # 立っているフラグが消えるならy ^ bが選ばれる
            y = min(y, y ^ b)
        # 最上位のフラグが残ってるなら xをbaseとして利用できる
        if y:
            base.append(x)
            elim.append(y)

    return base

base = rank(B)

def lg(x):
    return x.bit_length() - 1

# 線型独立したベクトルの本数がNのbitlength(rank)に満たない場合
if len(base) != lg(N):
    exit(print(-1))

# 0から順に繋いでいく　飛ぶ順に
xor = 0
for x in range(1, N):
    print(xor, end=' ')
    # base[i]: 2 ** iを担当するx
    xor ^= base[lg(x & -x)] # x & -x: xの一番下のフラグ # lg(x & -x): そのインデックス
    print(xor)

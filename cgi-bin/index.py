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

"""
# 一個飛ばしでボールを置く通りの数
def counter(n, s):
    # dp[i][j][k]: i個目まで進めた時にj個まで置いている通りの数
    dp = [[[0, 0] for _ in range(s + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1

    for i in range(1, n + 1):
        for j in range(s + 1):
            # ボールを置かない
            dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1])
            # ボールを置く
            # 前でボールを置いていない場合のみ置ける
            dp[i][j][1] = dp[i - 1][j - 1][0]
    return sum(dp[n][j])
"""

freq = getList()
freq = [f for f in freq if f > 0]

N = len(freq)
S = sum(freq)

"""
既存の文字列のどこに新しい文字を挿入するか、という思考をする。
同じ文字が隣り合っている箇所に挿入するのか否か？　
#dp[i][j] -> i種類目の文字まで見る。同じ文字が隣り合っている箇所がj箇所存在する。
何分割するか？　同じ文字が隣り合っている箇所のうち、何か所に挿入するか？
分割数の上限は、既存の文字列の長さ+1 か　文字の長さ
同じ文字が隣り合っている箇所のうち、何か所に挿入するかの上限は、同じ文字が隣り合っている箇所か分割数
何分割するか、どこで分割するか、同じ文字がとなり合う箇所に何か所に挿入するか、どこに挿入するか
"""

dp = [[0] * S for _ in range(N)]

f = freq[0] # １番目の文字が何個あるか
dp[0][f - 1] = 1 # 1番目の文字を入れた後、同じ文字が隣り合ってる場所が(１番目の文字の個数 - 1)個ある

memo = [[0] * 12 for _ in range(261)]

# 逆元事前処理ver
# nが小さい場合に
lim = 10 ** 5 + 1
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

s = 0
for i in range(N - 1):
    # i + 1についてレコードしていく
    s += freq[i] # i番目までの文字の個数の総数
    f = freq[i + 1] # i + 1番目の文字の個数

    # j: 隣合う箇所(0個 ~ 260個ある)
    for j in range(S):
        # d:分割数の個数
        # ただし分割数の上限はこれまで出てきた文字の個数 + 1個まで
        # これまで出てきた文字: ?
        # ○?○?○○
        for d in range(1, min(f, s + 1) + 1):
            # k:隣り合う箇所をいくつ潰すか
            # ただし潰す個数の上限は分割dの個数
            for k in range(min(j, d) + 1):
                # d - kがs - jを上回るケースがあるので排除する
                if d - k <= s + 1 - j:
                    # 分割したd個のうちk個を使ってj個の隣り合う箇所のうちk個潰す
                    # dp[i + 1][j + (f - d) - k]:j個の隣り合う箇所のうちk個潰す、ただし新しく追加した文字が内包する
                    # 隣り合う個数の数(f - d)を足す

                    # cmb(j, k):j個の隣り合う箇所のうちk個潰す地点を決める
                    # cmb(f - 1, d - 1): f - 1個の分割ポイントのうちd - 1個に仕切りを置く　これによりd個に分割できる
                    # cmb(s + 1 - j, d - k):隣合わない部分 + 1に余ったd - kを入れる
                    dp[i + 1][j + (f - d) - k] += dp[i][j] * cmb(j, k) * cmb(f - 1, d - 1) * cmb(s + 1 - j, d - k)

print(dp[-1][0] % mod)

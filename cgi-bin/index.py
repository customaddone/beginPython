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
import heapq
from math import sqrt
from fractions import gcd
import random
import string
import copy
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

N = 2
# N個のブロックが並んでいます
# 赤、青、緑、黄色の４色ある
# 赤色で塗られたものと緑色で塗られたブロックが共に偶数個になる通りは?
# dp数え上げorグルーピング掛け算

# 小さいものからやって行こう
# N = 1の時
# 全通りは4 ** 1通り(赤、青、緑、黄色)
# ansは青、黄色の時の２通り
# N = 2のとき
# 全通りは4 ** 2通り
# 赤赤、赤青、赤緑、赤黄 1つ
# 青赤、青青、青緑、青黄 2つ
# 緑赤、緑青、緑緑、緑黄 2つ
# 黄赤、黄青、黄緑、黄黄 1つ
# N = 3のとき
# 赤、青、緑、黄について上のもの + ３つ目の色でそれぞれ16通りずつある

# dp[i][0] 赤:偶数 緑:偶数
# dp[i][1] 赤:奇数 緑:偶数
# dp[i][2] 赤:偶数 緑:奇数
# dp[i][3] 赤:奇数 緑:奇数

# 漸化式なので行列累乗で解ける

N = 27
logk = N.bit_length()

# 行列式にすると
# [dp[i][0], dp[i][1], dp[i][2], dp[i][3]] =
# [[2, 1, 1, 0], [1, 2, 0, 1], [1, 0, 2, 1], [0, 1, 1, 2]][dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i - 1][3]]
dp = [[[0, 0, 0, 0] for i in range(4)] for i in range(logk)]
dp[0] = [[2, 1, 1, 0], [1, 2, 0, 1], [1, 0, 2, 1], [0, 1, 1, 2]]

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

ans = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
for i in range(logk):
    if N & (1 << i):
        ans = array_cnt(ans, dp[i])

print(array_cnt(ans, [[1, 0, 0, 0]])[0][0])

"""
for i in range(1, N):
    dp[i][0] += (2 * dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2])
    dp[i][1] += (dp[i - 1][0] + 2 * dp[i - 1][1] + dp[i - 1][3])
    dp[i][2] += (dp[i - 1][0] + 2 * dp[i - 1][2] + dp[i - 1][3])
    dp[i][3] += (dp[i - 1][1] + dp[i - 1][2] + 2 * dp[i - 1][3])
print(dp[-1])
"""

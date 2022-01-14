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

# ABC154 E - Almost Everywhere Zero
N = '9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999'
K = 3
L = len(N)

def judge(a):
    return a != 0

# N以下の数字で条件を満たす桁がk個のもの
def digit_dp(n, k):
    l = len(n)

    dp = [[[0] * (k + 1) for _ in range(2)] for i in range(l + 1)]
    dp[0][0][0] = 1

    for i in range(l):
        d = int(n[i])

        for j in range(2):
            for d_j in range(10 if j else d + 1):
                for k_j in range(k + 1):
                    if judge(d_j):
                        if k_j + 1 <= k:
                            dp[i + 1][j | (d_j < d)][k_j + 1] += dp[i][j][k_j]
                    else:
                        dp[i + 1][j | (d_j < d)][k_j] += dp[i][j][k_j]

    return dp

dp = digit_dp(N, K)
print(dp[L][0][K] + dp[L][1][K])

# ABC029 D - 1
N = '999999999'
L = len(N)

def judge_2(a):
    return a == 1

# N以下の数字の中で「1が書いてある桁がk個ある数字」がいくつあるか
# 上のものと関数の中身自体は変えていない
def digit_dp_2(n, k):
    l = len(n)

    dp = [[[0] * (k + 1) for _ in range(2)] for i in range(l + 1)]
    dp[0][0][0] = 1

    for i in range(l):
        d = int(n[i])

        for j in range(2):
            for d_j in range(10 if j else d + 1):
                for k_j in range(k + 1):
                    if judge_2(d_j):
                        if k_j + 1 <= k:
                            dp[i + 1][j | (d_j < d)][k_j + 1] += dp[i][j][k_j]
                    else:
                        dp[i + 1][j | (d_j < d)][k_j] += dp[i][j][k_j]

    return dp

dp = digit_dp_2(N, L)

ans = 0
for j in range(L + 1):
    # dp[l]について各j(1のカウント)の通りの数 * j
    ans += (dp[L][0][j] + dp[L][1][j]) * j
print(ans)

A, B = 1, 1000000000000000000

# 4, 9の個数については求めない簡易版
def judge_3(a):
    return a in [4, 9]

def digit_dp(n):
    l = len(n)

    dp = [[[0] * 2 for _ in range(2)] for i in range(l + 1)]
    dp[0][0][0] = 1

    for i in range(l):
        d = int(n[i])

        for j in range(2):
            for d_j in range(10 if j else d + 1):
                # 0:4,9が含まれない　1:4,9が含まれる
                for k_j in range(2):
                    if k_j == 0 and judge_3(d_j):
                        dp[i + 1][j | (d_j < d)][k_j + 1] += dp[i][j][k_j]
                    else:
                        dp[i + 1][j | (d_j < d)][k_j] += dp[i][j][k_j]
    return dp[l][0][1] + dp[l][1][1]

print(digit_dp(str(B)) - digit_dp(str(A - 1)))

# ABC129 E - Sum Equals Xor
# 通りの数を求める

L = '1111111111111111111'

def digit_dp_3(n):
    l = len(n)

    dp = [[[0] * 2 for _ in range(2)] for i in range(l + 1)]
    dp[0][0][0] = 1

    for i in range(l):
        d = int(n[i])

        # Lになる可能性があるかないか
        for j in range(2):
            # 次の桁が0か1か
            for d_j in range(2 if j else d + 1):
                if d_j == 0:
                    dp[i + 1][j | (d_j < d)][d_j] += (dp[i][j][0] + dp[i][j][1])
                    dp[i + 1][j | (d_j < d)][d_j] %= mod
                else:
                    dp[i + 1][j | (d_j < d)][d_j] += 2 * (dp[i][j][0] + dp[i][j][1])
                    dp[i + 1][j | (d_j < d)][d_j] %= mod

    return sum(dp[-1][0]) + sum(dp[-1][1])

print(digit_dp_3(L) % mod)

# No.1811 EQUIV Ten
# 桁 + 耳dp

"""
Nがくそでか　bitで考える　桁dp?
x // 2^k あるbit以下を切り捨て　後ろ4つが 1010
つまり　1010を持つ数がいくつあるか　桁dp
'', '1', '10', '101', '1010' の5つ
耳桁dp
"""

S = '1' * getN()
if S == '':
    print(0)
    exit()

N = len(S)
# 次にあるべき数字
jud = [1, 0, 1, 0, inf]
# dp[i][j][k]: iまで進んで最大値になる可能性がある(0)/ない(1), 状態はk
dp = [[[0] * 5 for _ in range(2)] for i in range(N + 1)]
dp[0][0][0] = 1

for i in range(N):
    d = int(S[i])
    # Lになる可能性があるかないか
    # ある→ある
    for j in range(2):
        # 次の桁は何にする　あるの場合はd以下　ないの場合は0, 1
        for d_j in range(2 if j else d + 1):
            # 状態1~4
            for k in range(4):
                # 次に進める
                if d_j == jud[k]:
                    dp[i + 1][j | (d_j < d)][k + 1] += dp[i][j][k]
                    dp[i + 1][j | (d_j < d)][k + 1] %= mod
                # 進めない
                else:
                    # 次が0なら状態0, 1なら状態1
                    dp[i + 1][j | (d_j < d)][(d_j == 1)] += dp[i][j][k]
                    dp[i + 1][j | (d_j < d)][(d_j == 1)] %= mod
            # 状態5
            dp[i + 1][j | (d_j < d)][4] += dp[i][j][4]
            dp[i + 1][j | (d_j < d)][4] %= mod

print((dp[i + 1][0][-1] + dp[i + 1][1][-1]) % mod)

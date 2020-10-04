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

# JOI11予選 F - ジグザグ数 (Zig-Zag Numbers)

# 桁dpかヒープキューか
# A以上B以下 :0 ~ Aと0 ~ B両方出す
# Mの倍数を出そう

# 多分桁dp
A = input()
B = input()
M = getN()

# prev[j][z][l_d][m]: 前回z(増加/減少/前なし)して最後尾がl_dでmの倍数のもの
def digit_dp(x):
    n = len(x)
    prev = [[[[0] * M for _ in range(10)] for i in range(3)] for i in range(2)]
    prev[0][2][0][0] = 1

    for i in range(n):
        d = int(x[i])
        next = [[[[0] * M for _ in range(10)] for i in range(3)] for i in range(2)]
        for j in range(2):
            for l_d in range(10): # prevの最後尾
                for d_j in range(10 if j else d + 1): # nextの最後尾
                    for m in range(M): # mod Mのもの
                        if d_j == 0 and d_j == 0: # 前なしなら無条件で足す
                            next[j | (d_j < d)][2][d_j][(m * 10 + d_j) % M] += prev[j][2][l_d][m]
                        else: # 前なしなら無条件で足す
                            next[j | (d_j < d)][0][d_j][(m * 10 + d_j) % M] += prev[j][2][l_d][m]
                            next[j | (d_j < d)][1][d_j][(m * 10 + d_j) % M] += prev[j][2][l_d][m]
                        if d_j > l_d: # 0:増加 1:減少
                            # (m(prevのm) * 10 + d_j) % M
                            next[j | (d_j < d)][0][d_j][(m * 10 + d_j) % M] += prev[j][1][l_d][m]
                        elif d_j < l_d:
                            next[j | (d_j < d)][1][d_j][(m * 10 + d_j) % M] += prev[j][0][l_d][m]

                        for z in range(3):
                            next[j | (d_j < d)][z][d_j][(m * 10 + d_j) % M] %= 10000

        prev = next

    # 00000が混じっているがA - Bするので問題なし
    return prev

opt1 = digit_dp(B)
opt1_diff = min(int(B), 9) // M # 1 ~ 9まではダブルカウントされているので修正
opt2 = digit_dp(str(int(A) - 1))
opt2_diff = min(int(A) - 1, 9) // M

ans = 0
for j in range(2):
    for z in range(3):
        for l_d in range(10):
            ans += opt1[j][z][l_d][0] - opt2[j][z][l_d][0]

print((ans - opt1_diff + opt2_diff) % 10000)

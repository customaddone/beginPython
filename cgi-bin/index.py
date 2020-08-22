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

num = [1, 3, 5, 7, 9]
limit = 10

# 個数制限あり重複なし部分和
# 合計でlimitになる通りの数が出てくる
# numは数字のリスト、limitは部分和
def part_sum_1(num, limit):
    N = len(num)
    dp = [[0] * (limit + 1) for i in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(limit + 1):
            if num[i] <= j:
                dp[i + 1][j] = dp[i][j - num[i]] + dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j]
    return dp[N][limit]
# print(part_sum_1(num, limit))

# 個数制限なし重複あり部分和
# 合計でlimitになる通りの数が出てくる
# 1 + 3 と3 + 1 と1 + 1 + 1 + 1は違う通りになる
def part_sum_2(num, limit):
    N = len(num)

    dp = [0] * (limit + 1)
    dp[0] = 1

    for i in range(1, limit + 1):
        for j in range(N):
            if i >= num[j]:
                dp[i] += dp[i - num[j]]
    return dp[limit]
# print(part_sum_2(num, limit))

num = [i for i in range(1, 11)]
L = len(num)

# 個数を考慮
# 重複あり
def part_sum_4(limit, k):
    # dp[k][limit] k個足してlimitになった
    dp = [[0] * (limit + 1) for i in range(k + 1)]
    dp[0][0] = 1

    for i in range(k):
        for j in range(limit + 1):
            for l in range(L):
                if j - num[l] >= 0:
                    dp[i + 1][j] += dp[i][j - num[l]]
    return dp

# print(part_sum_4(5, 5))

# 重複なし
def part_sum_5(n, k, limit):
    dp = [[[0] * (limit + 1) for i in range(k + 1)] for i in range(n + 1)]
    dp[0][0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for l in range(limit + 1):
                if l - num[i - 1] >= 0:
                    dp[i][j][l] += dp[i - 1][j - 1][l - num[i - 1]]
                dp[i][j][l] += dp[i - 1][j][l]

    return dp[n][k][limit]

print(part_sum_5(L, 3, 10))

# -付き部分和
N = 4
A = [-1, 1, 0, 1]

def part_sum_minus(n, A, limit):
    dp = [[0] * (limit * 2 + 1) for i in range(N + 1)]
    dp[0][limit] = 1

    for i in range(1, N + 1):
        for j in range(limit * 2 + 1):
            # 何も足さない場合
            dp[i][j] += dp[i - 1][j]
            if 0 <= j - A[i - 1] <= limit * 2:
                dp[i][j] += dp[i - 1][j - A[i - 1]]
            # if 0 <= j + A[i - 1] <= limit * 2:
                # dp[i][j] += dp[i - 1][j + A[i - 1]]
    return dp[-1][limit]

# 何も足さない場合も含まれる
print(part_sum_minus(N, A, 10))

# 個数制限あり重複なしナップサックdp
# weightがW以内でのvalueの合計の最大値
N = 4
w = [2, 1, 3, 2]
v = [3, 2, 4, 2]
A = 5

def knapsack_1(N, limit, weight, value):
    dp = [[0] * (limit + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(limit + 1):
            if weight[i] <= j:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i])
            else:
                dp[i + 1][j] = dp[i][j]
    return dp[N][limit]
# 7
# print(knapsack_1(N, A, w, v))

# 個数制限あり重複ありナップサックdp
# N = 4個まで足せる
def knapsack_2(N, limit, weight, value):
    dp = [[0] * (limit + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(limit + 1):
            dp[i + 1][j] = dp[i][j]
            for r in range(N):
                if weight[r] <= j:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - weight[r]] + value[r])
    return dp[N][limit]

# 9
# print(knapsack_2(N, A, w, v))

# 個数制限なし重複ありナップサックdp
# 最大は当然w = 1, v = 2を5回
def knapsack_3(N, limit, weight, value):
    dp = [0] * (limit + 1)
    dp[0] = 0

    for j in range(limit + 1):
        for r in range(N):
            if weight[r] <= j:
                dp[j] = max(dp[j], dp[j - weight[r]] + value[r])
    return dp[limit]

# 10
# print(knapsack_3(N, A, w, v))

N = 10
w = [7550, 9680, 9790, 7150, 5818, 7712, 8227, 8671, 8228, 2461]
v = [540, 691, 700, 510, 415, 551, 587, 619, 588, 176]
A = 9999

# ABC153 E - Crested Ibis vs Monster
# Aをvalueで引き切るための最小weightを求める
def knapsack_4(N, limit, weight, value):
    dp = [float('inf')] * (limit + 1)
    dp[0] = 0

    for i in range(1, limit + 1):
        for j in range(N):
            if i < value[j]:
                dp[i] = min(dp[i], weight[j])
            else:
                dp[i] = min(dp[i], dp[i - value[j]] + weight[j])
    return dp[-1]

# 139815
# print(knapsack_4(N, A, w, v))

A = 999
# 重複なしver
def knapsack_5(N, limit, weight, value):
    dp = [[float('inf')] * (limit + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(1, limit + 1):
            if i == 0:
                if j < value[i]:
                    dp[i][j] = weight[i]
            elif j < value[i]:
                dp[i + 1][j] = min(dp[i][j], weight[i])
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - value[i]] + weight[i])
    return dp[N][limit]

# 14045
# print(knapsack_5(N, A, w, v))

# ABC032 D - ナップサック問題
N, A = 10, 936447862
w = [810169801, 957981784, 687140254, 932608409, 42367415, 727293784, 870916042, 685539955, 243593312, 977358410]
v = [854, 691, 294, 333, 832, 642, 139, 101, 853, 369]

# 半分全列挙 + 二分探索
def re_list(weight, value):
    fore_list = []
    # まず全通り組み合わせる
    for bit in range(1 << len(weight)):
        wei = 0
        val = 0
        for i in range(len(weight)):
            if bit & (1 << i):
                wei += weight[i]
                val += value[i]
        fore_list.append([wei, val])
    fore_list.sort()

    # リスト再作成
    alta_w = []
    alta_v = []
    now = -1
    for i in fore_list:
        if now < i[1]:
            now = i[1]
            alta_w.append(i[0])
            alta_v.append(i[1])
    return alta_w, alta_v

def half_knapsack(N, limit, weight, value):
    # 半分全列挙
    fore_w, fore_v = re_list(weight[:N // 2], value[:N // 2])
    back_w, back_v = re_list(weight[N // 2:], value[N // 2:])

    ans = 0
    for b_w, b_v in zip(back_w, back_v):
        if b_w > limit:
            continue

        opt = b_v
        index = bisect_right(fore_w, limit - b_w)
        if index > 0:
            opt += fore_v[index - 1]
        ans = max(ans, opt)

    return ans

# あるweightで獲得できる最大のvalue
def knapsack_wei(N, limit, weight, value):
    dp = [[0] * (limit + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(limit + 1):
            if weight[i] <= j:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - weight[i]] + value[i])
            else:
                dp[i + 1][j] = dp[i][j]
    return dp[N][limit]

# あるvalueを獲得するために必要な最小のweight
def knapsack_val(N, limit, weight, value):
    max_v = sum(value)
    dp = [[float('inf')] * (max_v + 1) for i in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(max_v + 1):
            if value[i] <= j:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - value[i]] + weight[i])
            else:
                dp[i + 1][j] = dp[i][j]
    for i in range(max_v - 1, -1, -1):
        if dp[N][i] <= limit:
            return i

if N <= 30:
    print(half_knapsack(N, A, w, v))
    exit()
elif max(w) <= 1000:
    print(knapsack_wei(N, A, w, v))
    exit()
else:
    print(knapsack_val(N, A, w, v))
    exit()

W = 22
N = 5
K = 3
w = [5, 8, 3, 4, 6]
v = [40, 50, 60, 70, 80]

# ナップサックdp個数
# N個の選択肢、weightの上限upper, 足し合わせlimit個以内
def knapsack_6(N, upper, limit, weight, value):
    prev = [[0] * (upper + 1) for i in range(limit + 1)]

    for i in range(N):
        next = [[0] * (upper + 1) for i in range(limit + 1)]
        for j in range(limit + 1):
            for l in range(upper + 1):
                # もし残りweightがl以上でjが１以上（後ろがある）なら
                if l >= weight[i] and j >= 1:
                    next[j][l] = max(prev[j][l], prev[j - 1][l - weight[i]] + value[i])
                else:
                    next[j][l] = prev[j][l]
        prev = next
    return prev[limit][upper]

print(knapsack_6(N, W, K, w, v))

# 最長共通部分列
s = 'pirikapirirara'
t = 'poporinapeperuto'

def dfs(s, ts):
    lens = len(s)
    lent = len(t)
    dp = [[0] * (lent + 1) for i in range(lens + 1)]
    dp[0][0] = 0

    for i in range(lens):
        for j in range(lent):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j], dp[i][j + 1])
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[lens][lent]
print(dfs(s, t))

# レーベンシュタイン距離
s = "pirikapirirara"
t = "poporinapeperuto"

def dfs(s, t):
    lens = len(s)
    lent = len(t)
    dp = [[float('inf')] * (lent + 1) for i in range(lens + 1)]
    dp[0][0] = 0

    for i in range(lens):
        for j in range(lent):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j] + 1, dp[i][j + 1] + 1)
            else:
                dp[i + 1][j + 1] = min(dp[i][j] + 1, dp[i + 1][j] + 1, dp[i][j + 1] + 1)
    return dp[lens][lent]
print(dfs(s, t))

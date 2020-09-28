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

N = 4
inf = float('inf')

d = [
[0, 2, inf, inf],
[inf, 0, 3, 9],
[1, inf, 0, 6],
[inf, inf, 4, 0]
]

dp = [[-1] * N for i in range(1 << N)]

def rec(s, v, dp):
    if dp[s][v] >= 0:
        return dp[s][v]
    if s == (1 << N) - 1 and v == 0:
        dp[s][v] = 0
        return 0
    res = float('inf')
    for u in range(N):
        if s & (1 << u) == 0:
            res = min(res,rec(s|(1 << u), u, dp) + d[v][u])
    dp[s][v] = res
    return res
# 結局のところ0からスタートしようが1からスタートしようが同じ道を通る
print(rec(0,0,dp))

# ABC054 C - One-stroke Path

N, M = getNM()
dist = [[] for i in range(N + 1)]
for i in range(M):
    a, b = getNM()
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)

cnt = 0

pos = deque([[1 << 0, 0]])

while len(pos) > 0:
    s, v = pos.popleft()
    if s == (1 << N) - 1:
        cnt += 1
    for u in dist[v]:
        if s & (1 << u):
            continue
        pos.append([s | (1 << u), u])
print(cnt)

"""
全ての場所を一度だけ通り巡回する通りの数
bit(1 << N)を小さい順から探索する
①bit & (1 << 0)
最初に0を踏んでないということだから飛ばす
②現在の場所sを探すためN個探索する
③次の場所tを探すためN個探索する
④渡すdpする
"""

N, M = getNM()
G = [[0] * N for i in range(N)]
for i in range(M):
    a, b = getNM()
    G[a - 1][b - 1] = 1 # a ~ bのエッジが存在する
    G[b - 1][a - 1] = 1

# 状態bitから次の状態へ渡すdpするというのはよくやる
# [0](001) → [0, 1](011) → [0, 1, 2](111)
#          → [0, 2](101) → [0, 1, 2](111)
def counter(sta):
    # dp[bit][i]これまでに踏んだ場所がbitであり、現在の場所がiである
    dp = [[0] * N for i in range(1 << N)]
    dp[1 << sta][sta] = 1

    for bit in range(1, 1 << N):
        if not bit & (1 << sta):
            continue
        # s:現在の場所
        for s in range(N):
            # sを踏んだことになっていなければ飛ばす
            if not bit & (1 << s):
                continue
            # t:次の場所
            for t in range(N):
                # tを過去踏んでいない and s → tへのエッジがある
                if (bit & (1 << t)) == 0 and G[s][t]:
                    dp[bit|(1 << t)][t] += dp[bit][s]

    return sum(dp[(1 << N) - 1])

print(counter(0))

# ABC104 C - All Green
# 特別ボーナスがある問題は大抵bit dp
# 目標700点
D, G = getNM()
query = []
for i in range(D):
    p, c = getNM()
    query.append([i + 1, p, c])

ans_cnt = float('inf')

for bit in range(1 << D):
    sum = 0
    cnt = 0
    for i in range(D):
        if bit & (1 << i):
            sum += query[i][0] * query[i][1] * 100 + query[i][2]
            cnt += query[i][1]

    if sum < G:
        for j in range(D - 1, -1, -1):
            if not bit & (1 << j):
                left = G - sum
                fire = query[j][0] * 100
                opt = min(query[j][1], (left + fire - 1) // fire)
                sum += opt * query[j][0] * 100
                cnt += opt
                break

    if sum >= G:
        ans_cnt = min(ans_cnt, cnt)

print(ans_cnt)

# ABC119 C - Synthetic Kadomatsu
N, A, B, C = getNM()
L = getArray(N)

def counter(array):
    if (1 in array) and (2 in array) and (3 in array):
        opt = [0, 0, 0, 0]
        # 合成に10pかかる
        cnt = 0
        for i in range(len(array)):
            if opt[array[i]] > 0:
                cnt += 1
            if array[i] >= 1:
                opt[array[i]] += L[i]

        res = cnt * 10
        res += abs(opt[1] - A)
        res += abs(opt[2] - B)
        res += abs(opt[3] - C)

        return res

    else:
        return float('inf')

ans = float('inf')
def four_pow(i, array):
    global ans
    if i == N:
        ans = min(ans, counter(array))
        return
    # 4 ** Nループ
    for j in range(4):
        new_array = array + [j]
        four_pow(i + 1, new_array)

four_pow(0, [])
print(ans)

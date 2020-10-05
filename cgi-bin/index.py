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

N, M = 4, 6
weight = [67786, 3497, 44908, 2156, 26230, 86918]
value = [[1, 3, 4], [2], [2, 3, 4], [2, 3, 4], [2], [3]]

# N個のものを全て手に入れるのに必要なコストの最小値
# コストを1にすれば最小個数がわかる
# Nの数が十分に小さいと使用可能
# Mの数が十分小さければMをbitdpする
def get_everything(n, weight, value):
    m = len(weight)
    dp = [float("inf")] * (1 << n)
    dp[0] = 0

    for i in range(m):
        bit = 0
        for item in value[i]:
            bit |= (1 << (item - 1))

        for j in range(1 << n):
            dp[j | bit] = min(dp[j | bit], dp[j] + weight[i])

    return dp[(1 << N) - 1]

ans = get_everything(N, weight, value)
if ans == float("inf"):
    print(-1)
else:
    print(ans)

# N:ブロックの個数 M;ブロックの色 Y:コンボボーナス Z:全色ボーナス
# N <= 5000, M <= 10
N, M, Y, Z = getNM()
# 色ボーナス
d = dict()
for i in range(M):
    c, p = input().split()
    d[c] = (i, int(p))
# 落ちてくるブロックの種類
B = input()

# 全通り出してみよう
# 2 ** N通り
# 単色でやってみる?
# どれを取ればいいか
# 前から順に＾
# どの色をコンボしても点数は同じ

# dp?

# dp[i][j]: 直前の色がi, 全部でjの色を使った
dp = [[-float('inf')] * (1 << M) for _ in range(M + 1)]
dp[M][0] = 0

# 交換するdpの要領
for e in B:
    # B[i]番目の色ポイント
    i, p = d[e]
    # 色iを含む状態について調べる
    # 色が少ないものから順に巻き込んでいく感じ
    for j in range((1 << M) - 1, -1, -1):
        if j & (1 << i) == 0:
            continue

        # 候補1: 直前の色が違うものだった and 以前に使った色を使った
        num1 = max(dp[k][j] for k in range(M + 1) if k != i) + p
        # 候補2: 直前の色が同じものだった
        num2 = dp[i][j] + p + Y
        # 候補3: 直前の色が違うものだった and 以前に使っってない色を使った
        num3 = max(dp[k][j ^ (1 << i)] for k in range(M + 1) if k != i) + p
        dp[i][j] = max(dp[i][j], num1, num2, num3)

# 全色ボーナス
for i in range(M):
    dp[i][(1 << M) - 1] += Z

ans = 0
for row in dp:
    ans = max(ans, max(row))
print(ans)

# JOI16 D-ぬいぐるみの整理 (Plush Toys)

# N個のぬいぐるみはM種類のうちのどれか
# 同じ種類のぬいぐるみが全て連続するように
N, M = getNM()
T = getArray(N)
T = [i - 1 for i in T]

# 20!は間に合わないが2 ** 20は間に合う
# 取り出すぬいぐるみの最小値
# ai, a2...と決めていった時
# 違う場所にあるものを全て取り出せばOK

# 20!を2 ** 20に改善する

cnt_toys = [0] * M # 種類iのぬいぐるみの数
cnt_acc = [[0] * (N + 1) for i in range(M)] # [l, r]の区間で種類iを指定した時に変えないといけないぬいぐるみの数


for i in range(M): # 種類
    for j in range(N): # 左から何番目のぬいぐるみ
        if T[j] != i:
            cnt_acc[i][j + 1] = 1
        cnt_acc[i][j + 1] += cnt_acc[i][j]
    cnt_toys[i] = N - cnt_acc[i][-1]

dp = [float('inf')] * (1 << M)
dp[0] = 0
# bit dpする
for s in range(1 << M):
    # 今まで置いてきたぬいぐるみの総計 左側に詰めて置く
    left = sum([cnt_toys[i] for i in range(M) if s & (1 << i)])
    # 種類jを新たにその右に置く
    for j in range(M):
        if s & (1 << j):
            continue
        length = cnt_toys[j]
        cnt = cnt_acc[j][left + length] - cnt_acc[j][left] # 今まで置いてきたぬいぐるみの右側に種類jのぬいぐるみを指定する
        dp[s | (1 << j)] = min(dp[s | (1 << j)], dp[s] + cnt)

print(dp[-1])

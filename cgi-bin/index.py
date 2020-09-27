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

A = [3, 4, -8]
# array内の連続する区間の総和
def imos_sum(A):
    n = len(A)
    imos = [0]
    for i in range(n):
        imos.append(imos[i] + A[i])
    for i in range(n):
        for j in range(i + 1, n + 1):
            print(imos[j] - imos[i])
imos_sum(A)

# roopする配列の長さk以下の区間和
def roop_imos(array, k):
    n = len(array)
    alta = copy.deepcopy(array)
    alta += alta
    imos = [0]
    for i in range(len(alta)):
        imos.append(imos[i] + alta[i])
    for i in range(n):
        for j in range(1, k + 1):
            print(imos[i + j] - imos[i])
# roop_imos(A, 2)

# ABC005 D - おいしいたこ焼きの焼き方
N = getN()
maze = [getList() for i in range(N)]
Q = getN()
query = getArray(Q)

# 二次元累積和
dp = [[0] * N for i in range(N)]
# 縦１行目、横１行目
for i in range(N):
    dp[i][0] = maze[i][0]
for i in range(N):
    for j in range(1, N):
        dp[i][j] = dp[i][j - 1] + maze[i][j]
# 全て
for i in range(1, N):
    for j in range(N):
        dp[i][j] += dp[i - 1][j]

# 採点マシーン
def judge(sx, sy, ex, ey):
    mother = dp[ey][ex]
    minus1 = 0
    minus2 = 0
    plus = 0
    if sx > 0:
        minus1 = dp[ey][sx - 1]
    if sy > 0:
        minus2 = dp[sy - 1][ex]
    if sx > 0 and sy > 0:
        plus = dp[sy - 1][sx - 1]
    return mother - minus1 - minus2 + plus

# 「大きさNの時の美味しさ」のリスト
anslist = [0] * (N ** 2 + 1)
for nsx in range(N):
    for nex in range(nsx, N):
        for nsy in range(N):
            for ney in range(nsy, N):
                opt = judge(nsx, nsy, nex, ney)
                #print(opt, [nsx, nsy, nex, ney])
                index = (nex - nsx + 1) * (ney - nsy + 1)
                anslist[index] = max(anslist[index], opt)

# 「大きさN以下の時の美味しさ」のリスト
ans_alta = [0] * (N ** 2 + 1)
for i in range(1, len(ans_alta)):
    ans_alta[i] = max(ans_alta[i - 1], anslist[i])

for i in query:
    print(ans_alta[i])

# ABC014 atcolor
n = int(input())
lista = []
for i in range(n):
    a, b = map(int, input().split())
    lista.append([a, b])
listb = [0] * (10 ** 6 + 2)
for i in lista:
    listb[i[0]] += 1
    listb[i[1] + 1] -= 1
listc = [0]
for i in range(10 ** 6 + 2):
    listc.append(listb[i] + listc[i])
print(max(listc))

# ABC017 C - ハイスコア

# 全ての区間を選ばないように
# 二次元累積?
# 区間累積

# queryを「lでスタートするもの」と「rでゴールするもの」という２つの捉え方をする

# N:遺跡(query) M:宝石
N, M = getNM()
query = [getList() for i in range(N)]
if M == 1:
    print(0)
    exit()

# r以前の宝石を獲得する遺跡を探索する累積和
imos_up = [0] * M
# l以降の宝石を獲得する遺跡を探索する累積和
imos_down = [0] * M

for l, r, s in query:
    imos_up[r - 1] += s
    imos_down[l - 1] += s

for i in range(1, M):
    imos_up[i] += imos_up[i - 1]
    imos_down[M - i - 1] += imos_down[M - i]

ans = 0
for i in range(M):
    # i - 1個以前の宝石を獲得する遺跡、i + 1個以降の遺跡を獲得する遺跡を探索する
    if i == 0:
        opt = imos_down[i + 1]
    elif i == M - 1:
        opt = imos_up[i - 1]
    else:
        opt = imos_up[i - 1] + imos_down[i + 1]
    ans = max(ans, opt)
print(ans)

# ABC086 D - Checker

N, K = getNM()
imos = [[0] * K for j in range(K)] # 累積和 左上のマスがどの位置にあると
white = 0
# 黒白
# 白黒　テーブルを考える
for i in range(N):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    if c == "W":
        c = 1
    else:
        c = 0
    x %= 2 * K
    y %= 2 * K

    if x > K - 1:
        x -= K
        c += 1
    if y > K - 1:
        y -= K
        c += 1
    c %= 2

    if c == 1:
        white += 1
        imos[x][y] -= 1
    else:
        imos[x][y] += 1

for i in range(K):
    for j in range(K - 1):
        imos[i][j + 1] += imos[i][j]

for j in range(K):
    for i in range(K - 1):
        imos[i + 1][j] += imos[i][j]
print(imos)

ans = 0
for i in range(K):
    for j in range(K):
        exp = imos[K - 1][K - 1] - imos[K - 1][j] - imos[i][K - 1] + 2 * imos[i][j] + white
        ans = max(ans, max(exp, N - exp))

print(ans)


H, W = 3, 4
# maze = [getList() for i in range(H)]
maze = [
[1, 2, 1, 2],
[2, 3, 2, 3],
[1, 3, 1, 3]
]

# 二次元累積和
dp_sum = [[0] * W for i in range(H)]
dp_1 = [[0] * W for i in range(H)]
dp_2 = [[0] * W for i in range(H)]
dp_3 = [[0] * W for i in range(H)]

# x = 0 ~ i, y = 0 ~ j までの数の合計
def bi_cumul_sum(dp_n):
    # 縦１行目、横１行目
    for i in range(H):
        dp_n[i][0] = maze[i][0]
    for i in range(H):
        for j in range(1, W):
            dp_n[i][j] = dp_n[i][j - 1] + maze[i][j]
    # 全て
    for i in range(1, H):
        for j in range(W):
            dp_n[i][j] += dp_n[i - 1][j]
bi_cumul_sum(dp_sum)
# print(dp_sum)

# x = 0 ~ i, y = 0 ~ j までに出るnumの回数の合計
def bi_cumul_cnt(num, dp_m):
    # 縦１行目、横１行目
    for i in range(H):
        if maze[i][0] == num:
            dp_m[i][0] = 1
    for i in range(H):
        for j in range(1, W):
            if maze[i][j] == num:
                dp_m[i][j] = dp_m[i][j - 1] + 1
            else:
                dp_m[i][j] = dp_m[i][j - 1]
    # 全て
    for i in range(1, H):
        for j in range(W):
            dp_m[i][j] += dp_m[i - 1][j]
bi_cumul_cnt(3, dp_3)
# print(dp_1)

# x = sx ~ ex y = sy ~ eyまで
def judge(sx, sy, ex, ey, dp_l):
    mother = dp_l[ey][ex]
    minus1 = 0
    minus2 = 0
    plus = 0
    if sx > 0:
        minus1 = dp_l[ey][sx - 1]
    if sy > 0:
        minus2 = dp_l[sy - 1][ex]
    if sx > 0 and sy > 0:
        plus = dp_l[sy - 1][sx - 1]
    return mother - minus1 - minus2 + plus

print(judge(1, 1, 3, 2, dp_sum))
print(judge(2, 1, 3, 2, dp_3))

N, M, Q = 10, 3, 2
query = [
[1, 5],
[2, 8],
[7, 10],
[1, 7],
[3, 10]
]

# l から rまで行く鉄道の数
lr = [[0 for i in range(N + 1)] for j in range(N + 1)]
# l から r以前のどこかまで行く鉄道の数
imos = [[0 for i in range(N + 1)] for j in range(N + 1)]
imos2 = [[0 for i in range(N + 1)] for j in range(N + 1)]

for i in query:
    l, r = i
    lr[l][r] += 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        # j - 1以前のどこかまで行くもの　+ jまで行くもの
        imos[i][j] = imos[i][j - 1] + lr[i][j]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        # i - 1以前のどこかからスタート + iスタート
        imos2[i][j] = imos2[i - 1][j] + lr[i][j]

print(imos2)

"""
# 飛ばし累積和
N = 10
num = [i for i in range(1, N + 1)]
D = 2
lista = [0] * N
for i in range(D):
    for j in range(i, N, D):
        if j == i:
            lista[j] = num[j]
        else:
            lista[j] = num[j] + lista[j - D]
# [1, 2, 4, 6, 9, 12, 16, 20, 25, 30]
print(lista)
# 9番目までの奇数の数字の合計 - 1番目までの奇数の数字の合計
# 3 + 5 + 7 + 9
print(lista[8] - lista[0])
"""

# Dかそれぞれのqueryで固定なのでこの問題は解ける
H, W, D = getNM()
maze = []
for i in range(H):
    a = getList()
    maze.append(a)
Q = getN()
# piece[0]からpiece[1]まで
# 4 → 6　→ 8
piece = []
for i in range(Q):
    l, r = getNM()
    piece.append([l, r])

place_list = [[-1, -1] for i in range(H * W)]

for y in range(H):
    for x in range(W):
        place_list[maze[y][x] - 1] = [x, y]

# 飛ばし累積和
x_plus = [0] * (H * W)
y_plus = [0] * (H * W)
for i in range(D):
    for j in range(i, H * W, D):
        if j == i:
            opt_x = 0
            opt_y = 0
        else:
            opt_x = abs(place_list[j][0] - place_list[j - D][0])
            opt_y = abs(place_list[j][1] - place_list[j - D][1])
            x_plus[j] = opt_x + x_plus[j - D]
            y_plus[j] = opt_y + y_plus[j - D]

def past_exam(piece_query):
    start = piece_query[0]
    goal = piece_query[1]

    x_point = x_plus[goal - 1] - x_plus[start - 1]
    y_point = y_plus[goal - 1] - y_plus[start - 1]
    return x_point + y_point

for i in range(Q):
    print(past_exam(piece[i]))

N, K = getNM()
imos = [[0] * K for j in range(K)] # 累積和 左上のマスがどの位置にあると
white = 0
# 黒白
# 白黒　テーブルを考える
for i in range(N):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    if c == "W":
        c = 1
    else:
        c = 0
    x %= 2 * K
    y %= 2 * K

    if x > K - 1:
        x -= K
        c += 1
    if y > K - 1:
        y -= K
        c += 1
    c %= 2

    if c == 1:
        white += 1
        imos[x][y] -= 1
    else:
        imos[x][y] += 1

for i in range(K):
    for j in range(K - 1):
        imos[i][j + 1] += imos[i][j]

for j in range(K):
    for i in range(K - 1):
        imos[i + 1][j] += imos[i][j]
print(imos)

ans = 0
for i in range(K):
    for j in range(K):
        exp = imos[K - 1][K - 1] - imos[K - 1][j] - imos[i][K - 1] + 2 * imos[i][j] + white
        ans = max(ans, max(exp, N - exp))

print(ans)

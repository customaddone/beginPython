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
MOD = 10 ** 9 + 7

#############
# Main Code #
#############

# JOI本戦 B - IOI饅頭（IOI Manju）
M, N = getNM() # M:饅頭 N:箱
sweets = getArray(M)
box = [getList() for i in range(N)] # 最大C個, E円　1個ずつ
# 菓子の価格 - 箱の価格 の最大値
# M <= 10000, N <= 500
# dp?

sweets.sort(reverse = True)
imos = [0]
for i in range(M):
    imos.append(imos[i] + sweets[i])

# 箱に詰める饅頭の価格を大きく、箱の価格を小さくする
# 合計でi個詰められる箱を用意した時の箱の価格の最小値
# 貪欲に前から?
# grid dp無理め? M <= 10000なのでそこまで求めるだけでいい
# 500 * 10000
prev = [float('inf')] * 10001
prev[0] = 0

for c, e in box:
    for j in range(10000, -1, -1): # 逆順に
        if j - c >= 0:
            prev[j] = min(prev[j], prev[j - c] + e)
        else:
            prev[j] = min(prev[j], prev[0] + e)

ans = 0
for i in range(1, M + 1):
    ans = max(ans, imos[i] - prev[i])
print(ans)

# JOI11予選 D - パスタ (Pasta)
N, K = getNM()
pasta = [[] for i in range(N)]
for i in range(K):
    a, b = getNM()
    pasta[a - 1].append(b - 1)

# 通りの数を求める: dp, 数え上げ組み合わせ
# n日前のことが関係する: n次元のdpを作れる

# modが10000
# パスタは3種類
# dp[j][k]: 本日jのパスタで、前日kのパスタの通り

prev = [[0] * 3 for i in range(3)]
# 1日目
if pasta[0]:
    prev[pasta[0][0]][(pasta[0][0] + 1) % 3] = 1
else:
    for i in range(3):
        prev[i][(i + 1) % 3] = 1

# 2日目以降
for p in pasta[1:]:
    next = [[0] * 3 for i in range(3)]
    # すでに決められているなら
    if p:
        j = p[0]
        # 本日のパスタjは確定
        # その前の日のパスタnext[]j[k]のk, prev[j][k]のjは3通り
        # そのまた前日のパスタprev[j][k]のkは3通り
        for k in range(3):
            for p_k in range(3):
                if j == k and k == p_k:
                    continue
                next[j][k] += prev[k][p_k]
                next[j][k] %= 10000
    else:
        for j in range(3):
            for k in range(3):
                for p_k in range(3):
                    if j == k and k == p_k:
                        continue
                    next[j][k] += prev[k][p_k]
                    next[j][k] %= 10000
    prev = next

ans = 0
for i in range(3):
    for j in range(3):
        ans += prev[i][j]
        ans %= 10000
print(ans)

# Code Formula 2014 本選 D - 映画の連続視聴

"""
N <= 3000 O(N ** 2)まで
Mの映画が[S ~ E]までの間上映されている
同じ映画を見ることでより多くの幸福感
違う映画を見るとリセットされる
上映時刻がダブってなければ連続して視聴可能

まず貪欲を考える
区間スケジューリング
終わりの時刻でソート
[[2, 10, 40], [1, 0, 120], [1, 15, 135], [1, 240, 330]]
どの映画を１回見ても幸福度は同じ　出来るだけ連続させた方がいい？
連続してみると幸福度は絶対上がる
全探索？
同じ映画を見た場合、違う映画を見た場合
S, Eが小さいのでDPできそうO(N ** 2)できるので
同じ種類のものは連結して考えられる
1: [1, 0, 120], [1, 15, 135], [1, 240, 330]
2:    [2, 10, 40]
[2, 10, 40]をとる　次取れるのは[1, 240, 330]
[2, 10, 40]をとらない
2 → 3と繋いで100しか上がらなくでも、3 → 4とつなぐと100000上がるかもしれない
streak1: 何個
streak2: 何個..という風に数える
合成して区間スケジューリングかも
3 + 2がバッティングしても2 + 2なら通るかもしれない
2 + 2より3 + 1の方が強い
MAX連続を想定する

### 今いくつ連続してるかを考えなくていいようにする ###
1つ連続させたもの、2つ連続させたもの...をmovieに混ぜ込む
セグ木を使う
合成したものを混ぜ込む
"""

N = getN()
H = getList()
for i in  range(N - 1):
    H[i + 1] += H[i]
movie = [getList() for i in range(N)]
movie.sort(key = lambda i: i[2])

# セグ木を使わないver
dp = [0] * (10 ** 5 + 7)
prev = 0
for i in range(N):
    m, s, e = movie[i]
    # 初期化
    for j in range(prev + 1, e + 1):
        dp[j] = max(dp[j], dp[j - 1])
    prev = e

    dp[e] = max(dp[e], dp[s] + H[0])
    cnt = 0

    # 現在のtargetから区間スケジューリング
    for j in range(i + 1, N):
        nm, ns, ne = movie[j]
        if nm != m:
            continue
        if e <= ns:
            cnt += 1
            e = ne
            dp[e] = max(dp[e], dp[s] + H[cnt])

print(max(dp))

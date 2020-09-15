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

# 部分文字列の個数
S = 'aaaaa'
N = len(S)
# i文字目以降で最初に
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alp = {}
for i in range(26):
    alp[alphabet[i]] = i

# i文字目以降で最初に文字sが登場するのは
next = [[-1] * 26 for i in range(N)]
for i in range(N - 1, -1, -1):
    for j in range(26):
        if i == N - 1:
            break
        next[i][j] = next[i + 1][j]
    next[i][alp[S[i]]] = i

dp = [0] * (N + 1) # 1-indexになる
dp[0] = 1
# 配るdpでやる
for i in range(N):
    for j in range(26):
        if next[i][j] == -1:
            continue
        # 0-indexを1-indexに直す
        dp[next[i][j] + 1] += dp[i]
print(sum(dp))

# G - 辞書順

S = input()
K = getN()
N = len(S)
# i文字目以降で最初に
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alp = {}
for i in range(26):
    alp[alphabet[i]] = i
S = [alp[S[i]] for i in range(N)] # pypyだと遅いので

def changer(i, j):
    return i * 26 + j
# i文字目以降について文字cから始まる部分文字列の個数
dp = [0] * (N + 1) * 26 # 1次元配列にしないとメモリ容量の関係で無理
dp[changer(N - 1, S[N - 1])]= 1

for i in range(N - 2, -1, -1):

    for j in range(26):
        # S[i]と一致しない場合
        if S[i] != j:
            dp[changer(i, j)] += dp[changer(i + 1, j)] # 前のを引き継ぐだけ
        # 一致する場合
        else:
            dp[changer(i, j)] += 1 # 後に何も足さないケース
            dp[changer(i, j)] += sum(dp[changer(i + 1, 0):changer(i + 2, 0)]) # S[i] + 今まで出た全てのケースを足すå

part_sum = sum(dp[:26])
if part_sum < K:
    print('Eel')
    exit()

res = ""
i = 0

while i < N:
    for j in range(26):
        if K - dp[changer(i, j)] <= 0:
            break
        K -= dp[changer(i, j)] # K >= dp[i][j]ならそのケースはK番目より前にあるので飛ばす
    res += alphabet[j] # jが次の文字
    K -= 1 # jを選んで dp[i][j]については終了
    if K <= 0: # K <= 0ならもう足さなくていい
        break
    while S[i] != j: # S[i]が足した文字jと一致するまでS[i]を進める
        i += 1
    i += 1 # 次はS[i + 1]から探索する
print(res)

# ABC171 F - Strivore 

"""
dp[i][j]を
「i文字目まででj回Sの文字を使ったか」とする

K = 5
S = 'oof'
dp = [[0] * (len(S) + 1) for i in range(K + len(S) + 1)]
dp[0][0] = 1

for i in range(1, K + len(S) + 1):
    for j in range(len(S) + 1):
        if j < len(S):
            dp[i][j] += dp[i - 1][j] * 25
        else:
            dp[i][j] += dp[i - 1][j] * 26 # j回使い切るともうSは関係なくなるので *= 26になる
        if j >= 1:
            dp[i][j] += dp[i - 1][j - 1]

l_s = len(S)
どのタイミングで「この先ずっと*= 26」になるか
後ろからi文字目にSを使い切る: pow(25, K - k, mod) * cmb(N + K - k - 1, N - 1) * pow(26, k, mod)
...
"""

lim = 2 * (10 ** 6) + 1
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
    if r == 0:
        return 1
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod

K = getN()
S = input()
N = len(S)

ans = 0
# l_s + i文字目に文字を使い切る
# 次から *= 26
for k in range(K + 1):
    # 逆からやってる
    ans += cmb(N + K - k - 1, N - 1) * pow(26, k, mod) * pow(25, K - k, mod) % mod
    ans %= mod

print(ans)

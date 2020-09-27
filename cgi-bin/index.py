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

# ABC005 C - おいしいたこ焼きの売り方
# マッチング問題だが貪欲
T = getN()
N = getN()
sell = getList()
M = getN()
buy = getList()

# 来る客1, 2に売れるか
for cus in buy:
    flag = False
    for i in range(N):
        if sell[i] <= cus <= sell[i] + T:
            flag = True
            sell[i] = mod
            break
    if not flag:
        print('no')
        exit()
print('yes')

# ABC080 D - Recording
# 使ってない録画機は他のチャンネルにスイッチできる
# 同時にいくつ放送が流れているか
N, C = getNM()
query = [getList() for i in range(N)]
dp = [[0] * (C + 1) for i in range(10 ** 5 + 2)]
for i in range(N):
    s, t, c = query[i]
    dp[s][c] += 1
    dp[t + 1][c] -= 1

for i in range(1, 10 ** 5 + 2):
    for j in range(C + 1):
        dp[i][j] += dp[i - 1][j]

ans = 0
for i in range(10 ** 5 + 2):
    cnt = 0
    for j in dp[i]:
        if j > 0:
            cnt += 1
    ans = max(ans, cnt)
print(ans)

# ABC085 D - Katana Thrower
N, H = getNM()

a = []
b = []

for i in range(N):
  x, y = map(int, input().split())
  a.append(x)
  b.append(y)

# 振った場合の最大値
max_a = max(a)

ans = 0
# 振る刀の最大攻撃力より高い攻撃力を持つ投げ刀を高い順にソートする
# 刀iで好きなだけ振って攻撃する→気が済んだら投げることで振りの攻撃力と投げの攻撃力を
# 両方利用することができる
# 実は投げてしまった刀も振ることができるというルールに変更しても
# 問題の答えは変わらない
# 実際のムーブとしては
# ①最も攻撃力が高い振り刀で攻撃する
# ②一定の体力以下になると攻撃力が高い順に投げ刀で攻撃していって撃破
# という流れになる
for x in reversed(sorted(filter(lambda x: x >= max_a, b))):
    H -= x
    ans += 1
    if H <= 0: break

ans += max(0, (H + max_a - 1) // max_a)
print(ans)

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
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

"""
y = x + (1 - p)y
全てのアイドルを集めたいです
N, M は非常に小さい
bit　dpだろ
5 2

2 300　アイドルの人数2, 500円
3 5 アイドル3が5%で手に入る
4 95 アイドル4が95%で手に入る

3 500
5 20
1 30
2 50

アイドル一種類の場合
y = 1 + 0.95y 期待回数は1 / 0.05回
アイドル複数種類、くじ1個の場合
1 5
2 95
5パーセントの確率で(1を持っている状態)に移動し
95パーセントの確率で(2を持っている確率)に移動する
dp[1][0]: 0.0475の確率で何も持ってない
dp[1][1]: 0.0025の確率で1のみ持っており、
dp[1][2]: 0.9025の確率で2のみ持っている
dp[1][3]: 0.0475の確率で2つとも持っている

dp[2][0] = 0.0475 * dp[1][0]
dp[2][1] = 0.0025 * dp[1][0] + 0.0475 * dp[1][1]
dp[2][2] = 0.9025 * dp[1][0] + 0.0475 * dp[1][2]
dp[2][3] = 0.0475 * dp[1][0] + 0.95 * dp[1][1] + 0.05 * dp[1][2] + dp[1][3]
これを回せば答えは求まる

くじが複数個ある場合
最適な行動は
どのクジを使うかは全探索
全てのアイドルがもともとなかったらcontinue
アイドル1はそのクジでしか引けない　それは絶対アイドルが出るまで回す
いくつかのクジで引ける場合　最も有利なものを
クジを融合する？
2 2
2 1000
1 30
2 70
2 800
1 80
2 20

dp[1] = 0.0025 * dp[0] + 0.0475 * dp[1] + M
何も手に入らない確率は
"""

# 何これ？
N, M = getNM()
Q = []
C = [0] * M
for i in range(M):
    ido, c = getNM()
    C[i] = c
    m1 = []
    m2 = []
    for j in range(ido):
        ind, prob = getNM()
        m1.append(ind - 1)
        m2.append(prob / 100)
    Q.append([m1, m2])

prev = [float('inf')] * (1 << N)
prev[0] = 0
# クジ
for _ in range(10):
    for i, (id, prob) in enumerate(Q):
        next = [float('inf')] * (1 << N)
        next[0] = 0
        # 配るdp
        d = {}
        for bit in range(1 << len(id)):
            tar = 0
            opt = 1
            for j in range(len(id)):
                if bit & (1 << j):
                    tar |= (1 << id[j])
                    opt *= prob[j]
                else:
                    opt *= (1 - prob[j])
            d[tar] = opt

        for bit in range(1 << N):
            opt = C[i]
            for key, value in d.items():
                if key and bit & key == key:
                    opt += prev[bit - key] * value
            next[bit] = min(next[bit], opt / (1 - d[0]))

        prev = next

    print(prev)

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
import heapq
import math
from fractions import gcd
import random
import string
import copy
from itertools import combinations, permutations, product
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

N = 4
A = [
[2, 3, 4],
[1, 3, 4],
[4, 1, 2],
[3, 1, 2]
]

# 各試合に割り振るコード番号
def code(l, r, of):
    if l > r:
        l, r = r, l
    return of[l] + r - l - 1

of = [0] * (N + 1)
# i番目の選手は試合of[i - 1] + 1からof[i]番目の試合に参加する
for i in range(N):
    of[i + 1] = of[i] + N - i - 1
g = [[] for i in range(N * (N - 1) // 2)]

# 選手iが戦う試合について
for i in range(N):
    for j in range(N - 2):
        # 試合
        fcode = code(i, A[i][j] - 1, of)
        # fcodeの次にくる試合
        tcode = code(i, A[i][j + 1] - 1, of)
        # 試合tcodeは試合fcodeより後にくる
        g[fcode].append(tcode)

# トポソする
def sort_topologically(g):
    N = len(g)
    ec = [0] * N
    for i in range(N):
        # それぞれの試合の後に来る試合について
        for e in g[i]:
            # eの前に来る試合を数える
            ec[e] += 1
    ret = [0] * N
    q = 0

    for i in range(N):
        # 後に来る試合がなければ
        if ec[i] == 0:
            # 先頭はret[0] = a1, ret[1] = a2...
            ret[q] = i
            q += 1

    p = 0
    # p == q　全て並び終えるまで続く
    while p < q:
        # 先頭に来る試合ret[0], ret[1]...のそれより後に行われる試合について
        for to in g[ret[p]]:
            # 前に来る試合を一つ減らす
            ec[to] -= 1
            # もしそれで先頭になれたなら
            if ec[to] == 0:
                # 記録する
                ret[q] = to
                q += 1
        p += 1

    # 全ての前に来る試合を消せなかったら
    for i in range(N):
        if ec[i] > 0:
            return None
    return ret

od = sort_topologically(g)

if not od:
    print(-1)
else:
    dp = [1] * (N * (N - 1) // 2)
    # 全ての試合について
    for i in range(N * (N - 1) // 2):
        for e in g[od[i]]:
            # もしod[i]（eより前にあるもの）がでかければ更新
            dp[e] = max(dp[e], dp[od[i]] + 1)
    print(max(dp))

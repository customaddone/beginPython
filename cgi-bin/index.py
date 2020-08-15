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

N, M = 3, 3
# 1 x 2のブロックを重ならないようにおく
maze = [
'...',
'.x.',
'...'
]
# 二次元dp
dp = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        if maze[i][j] == 'x':
            dp[i][j] = 1

ans = 0
def dfs(array, i):
    global ans
    # 一番下が全て埋まって現在の列が上からN + 1番目になったら
    if i == N:
        ans += 1
        return

    # 調べるのは今現在の列だけで良い
    for j in range(M):
        flag = False
        if i + 1 < N and array[i][j] == 0 and array[i + 1][j] == 0:
            alta = copy.deepcopy(array)
            alta[i][j] = 1
            alta[i + 1][j] = 1
            # 現在の列が全て埋まったら
            if alta[i][-1] == 1:
                dfs(alta, i + 1)
            else:
                dfs(alta, i)
            flag = True
        if j + 1 < M and array[i][j] == 0 and array[i][j + 1] == 0:
            alta = copy.deepcopy(array)
            alta[i][j] = 1
            alta[i][j + 1] = 1
            if alta[i][-1] == 1:
                dfs(alta, i + 1)
            else:
                dfs(alta, i)
            flag = True
        # 置いたならbreak
        if flag:
            break
dfs(dp, 0)
print(ans)

"""
計算量かかりすぎ
ans = 0
def dfs(array):
    global ans
    cnt = 0
    for i in range(N):
        cnt += sum(array[i])
    if cnt == N * M:
        ans += 1
    for i in range(N):
        for j in range(M):
            flag = False
            if i + 1 < N and array[i][j] == 0 and array[i + 1][j] == 0:
                alta = copy.deepcopy(array)
                alta[i][j] = 1
                alta[i + 1][j] = 1
                dfs(alta)
                flag = True
            if j + 1 < M and array[i][j] == 0 and array[i][j + 1] == 0:
                alta = copy.deepcopy(array)
                alta[i][j] = 1
                alta[i][j + 1] = 1
                dfs(alta)
                flag = True
            # 置いたならbreak
            if flag:
                break
        else:
            continue
        break
dfs(dp)
print(ans)
"""

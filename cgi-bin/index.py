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

# https://qiita.com/keymoon/items/2a52f1b0fb7ef67fb89e
# 頂点がN個の木構造が与えられます。各頂点について、
# その頂点から最も遠い頂点の距離(通過する辺数)を求めてください。
N = 12
dist = [
[1, 4, 6],
[0, 2, 3],
[1],
[1],
[0, 5],
[4],
[0, 7, 10, 11],
[6, 8, 9],
[7],
[7],
[6],
[6]
]

# dp[now][parent]:今nowで一つ上の親がparentの場合
dp_root = [[-1] * N for i in range(N)]
dp = [[-1] * N for i in range(N)]
num = defaultdict(list)
ans_depth = [0] * N
sta = 7

# まず一つの頂点について部分木を全て求める
# 今0で親がiのものは後で出す
def dfs(now, parent):
    res = 1
    cnt = 0

    for i in dist[now]:
        if i == parent:
            continue
        num[now].append(i)
        dp[now][cnt] = dfs(i, now)
        res = max(res, dp[now][cnt] + 1)
        cnt += 1

    if parent != -1:
        dp_root[now][parent] = res
    return res

# dfs実行
ans_depth[sta] = dfs(sta, -1)

# 累積和
dp_down = copy.deepcopy(dp)
dp_up = copy.deepcopy(dp)
for i in range(N):
    num_n = len(num[i])
    for j in range(num_n - 1):
        dp_down[i][j + 1] = max(dp_down[i][j + 1], dp_down[i][j])
        dp_up[i][num_n - j - 2] = max(dp_up[i][num_n - j - 2], dp_up[i][num_n - j - 1])

# 逆順のdp_rootを記入　遡っていく
def plus_root(now, parent):
    for i in dist[now]:
        if i == parent:
            continue
        index = num[now].index(i)
        if index != 0 and index != len(num[now]) - 1:
            dp_root[now][i] = max(dp_down[now][index - 1], dp_up[now][index + 1]) + 1
        elif index == 0:
            dp_root[now][i] = dp_up[now][index + 1] + 1
        else:
            dp_root[now][i] = dp_down[now][index - 1] + 1

        dp_root[now][i] = max(dp_root[now][i], dp_root[parent][now] + 1)


    if len(dist[now]) == 1:
        dp_root[now][now] = dp_root[parent][now] + 1

# 答えとなる距離を記入していく
pos = deque([[sta, -1]])

while len(pos) > 0:
    now, parent = pos.popleft()
    plus_root(now, parent)
    for i in dist[now]:
        if i == parent:
            continue
        pos.append([i, now])

    if now != sta:
        ans_depth[now] = max(dp_root[now])

print(*ans_depth)

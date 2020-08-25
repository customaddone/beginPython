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

# ABC037 D - 経路
H, W = getNM()
maze = []
for i in range(H):
    m = getList()
    maze.append(m)

memo = [[-1] * W for i in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# ぐるぐる回るやつはdfs
def dfs(x, y):
    if memo[y][x] != -1:
        return memo[y][x]

    res = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < W and 0 <= ny < H and maze[ny][nx] > maze[y][x]:
            res += dfs(nx, ny)
            res %= mod

    memo[y][x] = res
    return res

ans = 0
for i in range(H):
    for j in range(W):
        ans += dfs(j, i)
        ans %= mod

print(ans % mod)

# ABC129 D - Lamp
H, W = getNM()
maze = [input() for i in range(H)]

dp_row = [[-1] * W for i in range(H)]
dp_col = [[-1] * W for i in range(H)]


# 横
def dfs_row(y, x):
    if dp_row[y][x] >= 0:
        return dp_row[y][x]

    if maze[y][x] == '#':
        return 0

    res = 1
    nx = x + 1
    if 0 <= nx < W and maze[y][nx] == '.':
        res += dfs_row(y, nx)
    dp_row[y][x] = res
    return res

for i in range(H):
    for j in range(W):
        dfs_row(i, j)
    cnt = 0
    for j in range(1, W):
        if dp_row[i][j] >= 0 and dp_row[i][j - 1] >= 0:
            dp_row[i][j] = dp_row[i][j - 1]

# 縦
def dfs_col(y, x):
    if dp_col[y][x] >= 0:
        return dp_col[y][x]

    if maze[y][x] == '#':
        return 0

    res = 1
    ny = y + 1
    if 0 <= ny < H and maze[ny][x] == '.':
        res += dfs_col(ny, x)
    dp_col[y][x] = res
    return res

for i in range(H):
    for j in range(W):
        dfs_col(i, j)

for i in range(1, H):
    for j in range(W):
        if dp_col[i][j] >= 0 and dp_col[i - 1][j] >= 0:
            dp_col[i][j] = dp_col[i - 1][j]
# 集計
ans = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == '.':
            ans = max(ans, dp_row[i][j] + dp_col[i][j] - 1)
print(ans)

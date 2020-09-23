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

maze = [
    [9,9,9,9,9,9,9,9,9,9,9,9],
    [9,0,0,0,9,0,0,0,0,0,0,9],
    [9,0,9,0,0,0,9,9,0,9,9,9],
    [9,0,9,9,0,9,0,0,0,9,0,9],
    [9,0,0,0,9,0,0,9,9,0,9,9],
    [9,9,9,0,0,9,0,9,0,0,0,9],
    [9,0,0,0,9,0,9,0,0,9,1,9],
    [9,0,9,0,0,0,0,9,0,0,9,9],
    [9,0,0,9,0,9,0,0,9,0,0,9],
    [9,0,9,0,9,0,9,0,0,9,0,9],
    [9,0,0,0,0,0,0,9,0,0,0,9],
    [9,9,9,9,9,9,9,9,9,9,9,9]
]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 100000

def dfs(x, y, depth):
    global ans
    if maze[y][x] == 1:
        ans = min(ans, depth)
    maze[y][x] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[ny][nx] < 2:
            dfs(nx, ny, depth + 1)
    maze[y][x] = 0

dfs(1, 1, 0)
print(ans)

m = int(input())
n = int(input())
maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0

# 最長距離を求める
def dfs(x, y, depth):
    global ans
    maze[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and maze[ny][nx] == 1:
            dfs(nx, ny, depth + 1)
    maze[y][x] = 1
    ans = max(ans, depth)

for i in range(m):
    for j in range(n):
        if maze[j][i] == 1:
            dfs(i, j, 1)
# TLEにならないんですかこれ
print(ans)

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

H, W, T = 2, 3, 10
maze = [
['S', '#', '#'],
['.', '#', 'G']
]

start = []
goal = []
for i in range(H):
    for j in range(W):
        if maze[i][j] == "S":
            start = [j, i]
        if maze[i][j] == "G":
            goal = [j, i]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 白マス、黒マスに侵入するコストを計算する関数
def comp_dist(x, s):
    return x if s == "#" else 1

# 二次元ダイクストラの関数
def dij(start_x, start_y, goal_x, goal_y, dis):
    dist = [[float("inf") for _ in range(W)] for _ in range(H)]
    dist[start_y][start_x] = 0
    pq = [(0, start_x, start_y)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while (pq[0][1] != goal_x or pq[0][2] != goal_y):
        distance, x, y = heapq.heappop(pq)

        if distance > dist[y][x]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < W and 0 <= ny < H:
                nd = dist[y][x] + comp_dist(dis, maze[ny][nx])
                if dist[ny][nx] > nd:
                    dist[ny][nx] = nd
                    heapq.heappush(pq, [dist[ny][nx], nx, ny])
    return pq[0][0]

# にぶたん
ok = -1
ng = 10 ** 9 + 1

while ng - ok > 1:
    mid = (ok + ng) // 2

    if dij(start[0], start[1], goal[0], goal[1], mid) > T:
        ng = mid
    else:
        ok = mid

print(ok)

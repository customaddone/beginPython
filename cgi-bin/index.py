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

H, W = getNM()
Ch, Cw = getNM()
Dh, Dw = getNM()
maze = [input() for i in range(H)]
Ch -= 1
Cw -= 1
Dh -= 1
Dw -= 1

# ワープを最低で何回使うか
# 上下左右2つ向こうまでの範囲内でワープできる
# 隣接する'.'が領域

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

pos = deque([[Ch, Cw]])
dp = [[-1] * W for i in range(H)]
dp[Ch][Cw] = 0

while len(pos) > 0:
    y, x = pos.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 歩いて移動
        if 0 <= nx < W and 0 <= ny < H and maze[ny][nx] == "." and (dp[ny][nx] == -1 or dp[y][x] < dp[ny][nx]):
            # 0-1 bfs
            # 先頭に置く（優先的に処理される)
            pos.appendleft([ny, nx])
            dp[ny][nx] = dp[y][x]
    # ワープ
    for i in range(-2, 3):
        for j in range(-2, 3):
            wy = y + i
            wx = x + j
            # 歩いて移動不可能でないと使わない
            if 0 <= wx < W and 0 <= wy < H and maze[wy][wx] == "." and dp[wy][wx] == -1:
                pos.append([wy, wx])
                dp[wy][wx] = dp[y][x] + 1

print(dp[Dh][Dw])

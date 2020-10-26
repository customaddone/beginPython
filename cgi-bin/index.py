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

# ABC007 幅優先探索
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gx, gy = map(int, input().split())
sy -= 1
sx -= 1
gx -= 1
gy -= 1

maze = []
ans = float('inf')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

pos = deque([[sx, sy, 0]])
dp = [[-1] * (c + 1) for i in range(r + 1)]
dp[sx][sy] = 0

for i in range(r):
    c = input()
    maze.append(list(c))

while len(pos) > 0:
    x, y, depth = pos.popleft()
    if x == gx and y == gy:
        break
    maze[x][y] = '#'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if maze[nx][ny] == "." and dp[nx][ny] == -1:
            pos.append([nx, ny, depth + 1])
            dp[nx][ny] = dp[x][y] + 1
print(dp[gx][gy])

# ABC176 D - Wizard in Maze
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
            # 先頭に置く
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

# AGC033 A - Darker and Darker

"""
一番近い#までの距離
100万マスあるので一回の探索で済むように
黒マスの周囲４マスを探索
用が済めばポイ　同じマスについて探索する必要はない
これで計算量は4 * H * W
"""

H, W = getNM()
maze = [list(input()) for i in range(H)]
prev = []
for i in range(H):
    for j in range(W):
        if maze[i][j] == '#':
            prev.append((i, j))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

flag = True
ans = 0
while flag:
    flag = False
    next = []
    while prev:
        y, x = prev.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < H and 0 <= nx < W and maze[ny][nx] == '.':
                flag = True
                maze[ny][nx] = '#'
                next.append((ny, nx))
    prev = next
    if flag:
        ans += 1

print(ans)

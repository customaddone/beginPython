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

# ARC005
H, W = getNM()
maze = [input() for i in range(H)]

start = [0, 0]
for i in range(H):
    for j in range(W):
        if maze[i][j] == 's':
            start = [i, j]
            break

goal = [0, 0]
for i in range(H):
    for j in range(W):
        if maze[i][j] == 'g':
            goal = [i, j]
            break

def dijkstra(start, goal, size, d):
    sy, sx = start
    gy, gx = goal

    dist = [[float('inf')] * W for i in range(H)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    pos = [(0, sy, sx)]
    heapify(pos)
    dist[sy][sx] = 0

    while len(pos):
        cost, y, x = heappop(pos)

        if y == gy and x == gx:
            return cost
        if dist[y][x] < cost:
            continue
        # エッジは探索のたびに生成していく
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < H and 0 <= nx < W:
                # '.'
                if (maze[ny][nx] == '.' or maze[ny][nx] == 'g') and dist[ny][nx] > cost:
                    dist[ny][nx] = cost
                    heappush(pos, (cost, ny, nx))
                # '#'
                if maze[ny][nx] == "#" and  dist[ny][nx] > cost + d:
                    dist[ny][nx] = cost + d
                    heappush(pos, (cost + d, ny, nx))

    return dist[gy][gx]

ans = dijkstra(start, goal, H * W, 1)
if ans <= 2:
    print('YES')
else:
    print('NO')

# ABC020 C - 壁抜け
# ダイクストラ + にぶたん
H, W, T = getNM()
maze = [input() for i in range(H)]
start = [0, 0]
for i in range(H):
    for j in range(W):
        if maze[i][j] == 'S':
            start = [i, j]
            break
goal = [0, 0]
for i in range(H):
    for j in range(W):
        if maze[i][j] == 'G':
            goal = [i, j]
            break
# 二次元ダイクストラ
def dijkstra(start, goal, size, d):
    sy, sx = start
    gy, gx = goal
    dist = [[float('inf')] * W for i in range(H)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    pos = [(0, sy, sx)]
    heapify(pos)
    dist[sy][sx] = 0
    while len(pos):
        cost, y, x = heappop(pos)
        if y == gy and x == gx:
            return cost
        if dist[y][x] < cost:
            continue
        # エッジは探索のたびに生成していく
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < H and 0 <= nx < W:
                # '.'
                if (maze[ny][nx] == '.' or maze[ny][nx] == 'G') and dist[ny][nx] > cost + 1:
                    dist[ny][nx] = cost + 1
                    heappush(pos, (cost + 1, ny, nx))
                # '#'
                if maze[ny][nx] == "#" and  dist[ny][nx] > cost + d:
                    dist[ny][nx] = cost + d
                    heappush(pos, (cost + d, ny, nx))
    return dist[gy][gx]
# にぶたん
ok = -1
ng = 10 ** 9 + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if dijkstra(start, goal, H * W, mid) > T:
        ng = mid
    else:
        ok = mid
print(ok)

# ABC035 D - トレジャーハント
# 帰りがけの最短距離を求めるために全ての道を逆方向にする
N, M, T = getNM()
A = getList()
query = [getList() for i in range(M)]
dist_1 = []
dist_2 = []
for i in range(M):
    a, b, c = query[i]
    dist_1.append([a, b, c])
    # 帰りがけの最短経路については全ての道を逆順にすればいい
    dist_2.append([b, a, c])

def build_tree_dis(N, edge_list):

    G = [[] for i in range(N)]

    for i in range(len(edge_list)):
        a, b, c = edge_list[i]
        G[a - 1].append([b - 1, c])

    # 葉（末端の数）
    leaves = []
    for i in range(N):
        if len(G[i]) == 1:
            leaves.append(i)

    return G

edges_1 = build_tree_dis(N, dist_1)
edges_2 = build_tree_dis(N, dist_2)

def dij(start, edges):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        d, now = heapq.heappop(pq)
        if (d > dist[now]):
            continue
        for i in edges[now]:
            if dist[i[0]] > dist[now] + i[1]:
                dist[i[0]] = dist[now] + i[1]
                heapq.heappush(pq, (dist[i[0]], i[0]))
    return dist

dij_to = dij(0, edges_1)
dij_from = dij(0, edges_2)
ans = 0

for i in range(N):
    time = dij_to[i] + dij_from[i]
    opt = (T - time) * A[i]
    ans = max(ans, opt)
print(ans)

# ABC176
H, W = getNM()
Ch, Cw = getNM()
Dh, Dw = getNM()
maze = [input() for i in range(H)]
Ch -= 1
Cw -= 1
Dh -= 1
Dw -= 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 二次元ダイクストラ

def dijkstra(start, goal, size):
    sy, sx = start
    gy, gx = goal
    dist = [[float('inf')] * W for i in range(H)]
    pos = [(0, sy, sx)]
    heapify(pos)
    dist[sy][sx] = 0
    while len(pos):
        cost, y, x = heappop(pos)
        if y == gy and x == gx:
            return cost
        if dist[y][x] < cost:
            continue
        # エッジは探索のたびに生成していく
        # walking
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < H and 0 <= nx < W and maze[ny][nx] == '.':
                if dist[ny][nx] > cost:
                    dist[ny][nx] = cost
                    heappush(pos, (cost, ny, nx))
        # warp
        for w_y in range(-2, 3):
            for w_x in range(-2, 3):
                wy = y + w_y
                wx = x + w_x
                if 0 <= wy < H and 0 <= wx < W and maze[wy][wx] == '.':
                    if dist[wy][wx] > cost + 1:
                        dist[wy][wx] = cost + 1
                        heappush(pos, (cost + 1, wy, wx))
    return dist[gy][gx]
ans = dijkstra((Ch, Cw), (Dh, Dw), H * W)
if ans == float('inf'):
    print(-1)
else:
    print(ans)

# 0-1bfs

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

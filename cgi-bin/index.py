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

# SoundHound Inc. Programming Contest 2018 -Masters Tournament-
# D - Saving Snuuk

"""
スヌーくの最大値を求める
N個の都市 M個の電車
無向連結グラフ

a円かbスヌーくで払える
i番目の都市の両替所はi年後に閉鎖される　逆むきに考える？
sからtに行きたい　金は無限にある
多くのスヌーくを持ってる状態でゴールしたい
１年後に旅行する場合、２年後、３年後...

sからtの経路を求める　これは何通りもある
N多いな　ダイクストラは使える
貪欲になるか

各iについてO(1)で答えないといけない
スタートとゴールは一定　
ただし両替所の関係でそれぞれの経路は異なる場合がある

ある地点までは円で払う　ある地点からはスヌーくで払う
iが経過するごとに条件が厳しくなり、求める最大値が小さくなる
逆向きUnionFindか

Sから各地点までの円、スヌーくでの最短費用
各地点からTまでの円、スヌーくでの最短費用をダイクストラで求める
yen_s: [1, 0, 21, 2]
sunuke_t: [1, 11, 0, 101]
yen_s + sunuke_tの費用
"""

N, M, S, T = getNM()
Q = [getList() for i in range(M)]

S -= 1
T -= 1

yen = [[] for i in range(N)]
sunuke = [[] for i in range(N)]
for u, v, a, b in Q:
    yen[u - 1].append([v - 1, a])
    yen[v - 1].append([u - 1, a])
    sunuke[u - 1].append([v - 1, b])
    sunuke[v - 1].append([u - 1, b])

# M <= 10 ** 5なので使える
def dij(start, edges):
    dist = [float('inf') for i in range(N)]
    dist[start] = 0
    pq = [(0, start)]

    # pqの先頭がgoal行きのものなら最短距離を返す
    while len(pq) > 0:
        d, now = heappop(pq)
        if (d > dist[now]):
            continue
        for i in edges[now]:
            if dist[i[0]] > dist[now] + i[1]:
                dist[i[0]] = dist[now] + i[1]
                heappush(pq, (dist[i[0]], i[0]))
    return dist

yen_s = dij(S, yen)
sunuke_t = dij(T, sunuke)

price = [yen_s[i] + sunuke_t[i] for i in range(N)]
for i in range(N - 2, -1, -1):
    price[i] = min(price[i], price[i + 1])

for i in range(N):
    print(10 ** 15 - price[i])

# ARC003 C - 暗闇帰り道 

"""
ぐるぐる回っていい
最大値の最小値を求めよ　二分探索したくなる

だんだんと踏める部分が減っていく
全マスをt乗する そのうち下限を超えているものが一本道になっていルカ
t回かける　ルートを探索してみる
その最短経路はt回以内であるか
t回以内でゴールできる or 明るさx以内でゴールできる　を二分探索

区画の明るさがx以上でゴールできるか
"""

N, M = 500, 500
mother = [[1] * 500 for i in range(500)]
mother[0][0] = 's'
mother[499][499] = 'g'

for i in range(N):
    for j in range(M):
        if mother[i][j] == 's':
            mother[i][j] = -1
            sta = [i, j]
        elif mother[i][j] == 'g':
            mother[i][j] = float('inf')
            end = [i, j]
        elif mother[i][j] == '#':
            mother[i][j] = -1
        else:
            mother[i][j] = int(mother[i][j])

t_table = [1]
for i in range(10 ** 5 + 7):
    t_table.append(t_table[-1] * 0.99)

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def judge(target):
    dist = [[float('inf')] * M for i in range(N)]
    pos = [[0, sta[0], sta[1]]]
    heapify(pos)
    dist[sta[0]][sta[1]] = 0

    while pos:
        t, y, x = heappop(pos)
        if y == end[0] and x == end[1]:
            return True
        if dist[y][x] < t:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and dist[ny][nx] > t + 1 and mother[ny][nx] * t_table[t + 1] > target:
                dist[ny][nx] = t + 1
                heappush(pos, (t + 1, ny, nx))

    return False

ok = 0
ng = 10

for i in range(10):
    mid = (ok + ng) / 2
    if judge(mid):
        ok = mid
    else:
        ng = mid

if judge(ok):
    print(ok)
else:
    print(-1)

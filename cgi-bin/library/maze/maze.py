from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# ARC005 C - 器物損壊！高橋君
# 隣マスにコスト0で移動する場合は0-1bfsする

H, W = 4, 5
maze = [
['s', '#', '#', '#', '#'],
['.', '.', '.', '.', '#'],
['#', '#', '#', '#', '#'],
['#', '.', '.', '.', 'g'],
]

for i in range(H):
    for j in range(W):
        if maze[i][j] == 's':
            si = [i, j]
            maze[i][j] = '.'
        elif maze[i][j] == 'g':
            gi = [i, j]
            maze[i][j] = '.'

pos = deque([[si[0], si[1]]])
dist = [[-1] * W for j in range(H)]
dist[si[0]][si[1]] = 0

# 0-1bfs
while pos:
    y, x = pos.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < H and 0 <= nx < W and dist[ny][nx] == -1:
            if maze[ny][nx] == '.':
                dist[ny][nx] = dist[y][x]
                pos.appendleft([ny, nx]) # 0コストはappendleftで
            else:
                dist[ny][nx] = dist[y][x] + 1
                pos.append([ny, nx])

if dist[gi[0]][gi[1]] <= 2:
    print('YES')
else:
    print('NO')

H, W, T = 2, 3, 10
maze = [
'S##',
'.#G'
]

start = [0, 0]
goal = [0, 0]
for i in range(H):
    for j in range(W):
        if maze[i][j] == 'S':
            start = [i, j]
            break
        if maze[i][j] == 'G':
            goal = [i, j]
            break

# ABC020 C - 壁抜け
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

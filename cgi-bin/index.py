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

# AGC043 A - Range Flip Find Route

"""
白いとこだけ踏んでゴールを目指す
スタートやゴールが黒いこともある

操作をすると選択した長方形空間内の白黒が反転する
最小で何回操作するか
効率の良い操作方法を考える

黒い部分を白くすることだけを考える？
白だけ踏んでいけるとは？
二回反転させれば元どおり

白から黒に、黒から白に侵入するときだけ += 1する？
"""

H, W = getNM()
maze = [list(input()) for i in range(H)]
dp = [[float('inf')] * W for i in range(H)]
dp[0][0] = 0
if maze[0][0] == "#":
    dp[0][0] = 1

dy = [0, 1]
dx = [1, 0]

pos = deque([[0, 0]])

# 0 - 1bfs?
while pos:
    y, x = pos.popleft()
    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < H and 0 <= nx < W: # 領域内
            # 同じ色の場合
            if maze[y][x] == maze[ny][nx] and dp[ny][nx] > dp[y][x]:
                pos.appendleft([ny, nx])
                dp[ny][nx] = dp[y][x]
            # 違う色の場合
            if maze[y][x] != maze[ny][nx]:
                # 入るときだけでいい
                if maze[y][x] == "." and dp[ny][nx] > dp[y][x] + 1:
                    pos.append([ny, nx])
                    dp[ny][nx] = dp[y][x] + 1
                elif maze[y][x] == "#" and dp[ny][nx] > dp[y][x]:
                    pos.appendleft([ny, nx])
                    dp[ny][nx] = dp[y][x]

print(dp[H - 1][W - 1])

# AGC014 C - Closed Rooms

"""
H行W列
K回まで移動できる　K個の部屋を解放する
端っこの'.'を目指す　またダイクストラか

黒を移動できると考えてもいい
全探索する
端っこの部屋についての最短距離を求める
0-1bfsか

最初の１回は['.']の部分だけ移動できる
次からは['.'] + ['#']を移動できる

端っこまで黒何個消しで行けるか
単純な距離　と
黒を何個消すか　を求める

1回目白マス行けるとこまで移動する　
あとは自由に航行できる（前回のでKマス部屋を開いて今回Kマス進むため）

ほぼほぼ'#'は関係がない
posの中身を途中で書き換える問題
"""

H, W, K = getNM()
maze = [list(input()) for i in range(H)]

start = [-1, -1]
# スタート位置特定
for i in range(H):
    for j in range(W):
        if maze[i][j] == 'S':
            start = [i, j]
            break
    else:
        continue
    break

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

dis = [[-1] * W for i in range(H)]
dis[start[0]][start[1]] = 0

# 最初の１回 白マス内だけをK回まで移動する
# これらで移動したものは全てK回移動でカウントする
pos = deque([[start[0], start[1], 0]])
alta = [[start[0], start[1], K]]
while len(pos) > 0:
    y, x, d = pos.popleft()
    if d == K:
        continue
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < H and 0 <= nx < W and dis[ny][nx] == -1 and maze[ny][nx] == ".":
            dis[ny][nx] = d + 1
            alta.append([ny, nx, K])
            pos.append([ny, nx, d + 1])

ans = float('inf')
# あとはそのまま直進して壁にぶつかるだけ
for y, x, d in alta:
    up = y
    down = (H - 1) - y
    left = x
    right = (W - 1) - x
    opt = ((min(up, down, left, right) + K - 1) // K) + 1

    ans = min(ans, opt)

print(ans)

# ABC184 E - Third Avenue

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

H, W = map(int, input().split())
a = [input() for i in range(H)]

cost = [[INF] * W for i in range(H)]
tele = [list() for i in range(26)]

for i in range(H):
    for j in range(W):
        if a[i][j].islower():
            tele[ord(a[i][j]) - 97].append((i, j))
        elif a[i][j] == 'S':
            Sx, Sy = i, j
        elif a[i][j] == 'G':
            Gx, Gy = i, j

cost[Sx][Sy] = 0
q = deque([(Sx, Sy)])
while q:
    x, y = q.popleft()
    c2 = cost[x][y] + 1
    for d in range(4):
        x2 = x + dx[d]
        y2 = y + dy[d]
        if x2 < 0 or x2 >= H or y2 < 0 or y2 >= W or a[x2][y2] == '#':
            continue
        if cost[x2][y2] > c2:
            cost[x2][y2] = c2
            q.append((x2, y2))
    if a[x][y].islower():
        t = ord(a[x][y]) - 97 # 小文字は97
        for x2, y2 in tele[t]:
            if cost[x2][y2] > c2:
                cost[x2][y2] = c2
                q.append((x2, y2))
        tele[t].clear()

ans = cost[Gx][Gy]
if ans == INF:
    ans = -1
print(ans)

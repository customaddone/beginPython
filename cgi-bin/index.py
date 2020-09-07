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

# p21 三角形
N = 4
A = [4, 5, 10, 20]

# 全探索
ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for l in range(j + 1, N):
            # 一番長い辺の長さが残りの２辺の合計より短い
            if A[i] + A[j] + A[l] - 2 * max(A[i], A[j], A[l]) > 0:
                ans = max(ans,  A[i] + A[j] +  A[l])
print(ans)

# p23 ants
# アリ同士はすり抜けると考える
L = 10
N = 3
X = [2, 6, 7]
mi, ma = 0, 0
for i in range(N):
    l = X[i]
    r = L - X[i]
    mi = max(mi, min(l, r))
    ma = max(ma, max(l, r))
print(mi, ma)

def binary_search_loop(data, target):
    imin = 0
    imax = len(data) - 1
    while imin <= imax:
        imid = imin + (imax - imin) // 2
        if target == data[imid]:
            return True
        elif target < data[imid]:
            imax = imid - 1
        else:
            imin = imid + 1
    return False

# p25くじ引き
N = 3
M = 4
K = [1, 3, 5]
alta = []
for i in range(N):
    for j in range(N):
        alta.append(K[i] + K[j])
alta.sort()

ans = 'No'
for i in range(N ** 2):
    if M - alta[i] <= 0:
        continue
    if binary_search_loop(alta, M - alta[i]):
        ans = 'Yes'
        break
print(ans)

# p34 部分和問題
N = 4
A = [1, 2, 4, 7]
K = 13

def dfs(i, sum):
    if i == N:
        return sum == K
    if K - sum < A[i]:
        return dfs(i + 1, sum)
    else:
        return dfs(i + 1, sum) or dfs(i + 1, sum + A[i])

print(dfs(0, 0))

# p35 lake counting
N = 10
M = 12
# mazeの水溜りを埋めていく
maze = [
'W........WW.',
'.WWW.....WWW',
'....WW...WW.',
'.........WW.',
'.........W..',
'..W......W..',
'.W.W.....WW.',
'W.W.W.....W.',
'.W.W......W.',
'..W.......W.'
]
maze = [list(i) for i in maze]

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def dfs(y, x):
    maze[y][x] = '.'
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == 'W':
            dfs(ny, nx)

ans = 0
for i in range(N):
    for j in range(M):
        if maze[i][j] == 'W':
            dfs(i, j)
            ans += 1
print(ans)

# p37 迷路の最短路
N = 10
M = 10
maze = [
'#S######.#',
'......#..#',
'.#.##.##.#',
'.#........',
'##.##.####',
'....#....#',
'.#######.#',
'....#.....',
'.####.###.',
'....#...G#'
]
maze = [list(i) for i in maze]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

start = [-1, -1]
end = [-1, -1]
# スタート位置特定
for i in range(N):
    for j in range(M):
        if maze[i][j] == 'S':
            start = [i, j]
            break
    else:
        continue
    break

# ゴール位置特定
for i in range(N):
    for j in range(M):
        if maze[i][j] == 'G':
            goal = [i, j]
            break
    else:
        continue
    break

def bfs(start, goal, maze):
    pos = deque([start])
    dp = [[-1] * M for i in range(N)]
    dp[start[0]][start[1]] = 0

    while len(pos) > 0:
        y, x = pos.popleft()
        if y == goal[0] and x == goal[1]:
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] != "#" and dp[ny][nx] == -1:
                dp[ny][nx] = dp[y][x] + 1
                pos.append([ny, nx])

    return dp[goal[0]][goal[1]]

print(bfs(start, goal, maze))

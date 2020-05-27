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

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import fractions
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

from itertools import permutations
from math import factorial, hypot

h, w, n = map(int, input().split())

"""
10 10 9
.X...X.S.X
6..5X..X1X
...XXXX..X
X..9X...X.
8.X2X..X3X
...XX.X4..
XX....7X..
X..X..XX..
X...X.XX..
..X.......
"""

maze = []
for i in range(h):
    a = input()
    maze.append(list(a))

start = [-1, -1]
end = [-1, -1]
ans = 0
# スタート位置特定
for i in range(w):
    for j in range(h):
        if maze[j][i] == 'S':
            start = [i, j]
            break
    else:
        continue
    break
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# スタート位置破壊
maze[start[1]][start[0]] = '.'

# n → n + 1へ移動するまでにかかる時間
def bfs(sta, end):
    global start
    pos = deque([[sta[0], sta[1], 0]])
    dp = [[-1] * (w + 1) for i in range(h + 1)]
    
    while len(pos) > 0:
        x, y, time = pos.popleft()
        if maze[y][x] == str(end):
            start = [x, y]
            return dp[y][x] + 1
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] != 'X' and dp[ny][nx] == -1:
                dp[ny][nx] = dp[y][x] + 1
                pos.append([nx, ny, time + 1])

for i in range(n):
    ans += bfs([start[0], start[1]], i + 1)
print(ans)

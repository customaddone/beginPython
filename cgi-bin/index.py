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

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

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
import heapq
import math
from fractions import gcd
import random
import string
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

H, W, N = getNM()
maze = []
for i in range(H):
    a = input()
    maze.append(list(a))

start = [-1, -1]
end = [-1, -1]
ans = 0
# スタート位置特定
for i in range(W):
    for j in range(H):
        if maze[j][i] == 'S':
            start = [i, j]
            break
    else:
        continue
    break

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
mazealta = [[1] * W for i in range(H)]
mazealta[start[1]][start[0]] = 0
ans = 0

def dfs(x, y, cnt):
    global ans
    cnt_h, cnt_b = cnt
    if cnt_b * ans + cnt_h > N:
        return
    if maze[y][x] == 'G':
        opt = (N - 1 - cnt_h) // cnt_b
        ans = max(ans, opt)
    mazealta[y][x] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < W and 0 <= ny < H and mazealta[ny][nx] == 1:
            if maze[ny][nx] == ".":
                dfs(nx, ny, [cnt_h + 1, cnt_b])
            elif maze[ny][nx] == "#":
                dfs(nx, ny, [cnt_h, cnt_b + 1])
            else:
                dfs(nx, ny, [cnt_h, cnt_b])
    mazealta[y][x] = 1
dfs(start[0], start[1], [0, 0])
print(ans)

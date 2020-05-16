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
import copy
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

H, W = getNM()
maze = []
for i in range(H):
    a = getList()
    maze.append(a)

ans = []

# 部屋の掃除の要領で奇数の1を右端に運ぶ
for i in range(H):
    for j in range(W - 1):
        if maze[i][j] % 2 == 1:
            maze[i][j] -= 1
            maze[i][j + 1] += 1
            ans.append([i + 1, j + 1, i + 1, j + 2])

# 右端の1を右下に運ぶ
for i in range(H - 1):
    if maze[i][-1] % 2 == 1:
        maze[i][-1] -= 1
        maze[i + 1][-1] += 1
        ans.append([i + 1, W, i + 2, W])

print(len(ans))
for i in ans:
    print(*i)

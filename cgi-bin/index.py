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
from fractions import gcd
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

#############
# Main Code #
#############

H, W = getNM()
maze = [list(input()) for i in range(H)]
prevmaze = [['.'] * W for i in range(H)]
# 8方向のベクトル
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

# #がある点の周囲を#にする
def alter(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < W and 0 <= ny < H and prevmaze[ny][nx] == ".":
            prevmaze[ny][nx] = "#"

grass = []

# 周囲を#に囲まれた地点を検索
def rounder(x, y):
    flag = True
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < W and 0 <= ny < H:
            if maze[ny][nx] == ".":
                flag = False
    if flag:
        grass.append([x, y])
        prevmaze[y][x] = "#"

for i in range(W):
    for j in range(H):
        if maze[j][i] == "#":
            rounder(i, j)

anscopy = copy.deepcopy(prevmaze)

for i in grass:
    px, py = i[0], i[1]
    alter(px, py)
if (maze == prevmaze):
    print('possible')
    for i in anscopy:
        print(''.join(map(str, i)))
else:
    print('impossible')

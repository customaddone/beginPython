def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
# list(map(int, input().split()))
H, W = getNM()
maze = [list(input()) for i in range(H)]
prevmaze = [['.'] * W for i in range(H)]
# 8方向のベクトル
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

# 関数を小分けにしてみよう
def alter(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < W and 0 <= ny < H and prevmaze[ny][nx] == ".":
            prevmaze[ny][nx] = "#"

grass = []

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

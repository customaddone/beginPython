from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
ワープできると考える
マス目の中なら一回消費でいける
"""

H, W = getNM()
maze = [input() for i in range(H)]
pos = deque([[0, 0]])
dp = [[-1] * W for i in range(H)]
dp[0][0] = 0

while len(pos) > 0:
    # 0移動
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
            if abs(i) == abs(j):
                continue
            wy = y + i
            wx = x + j
            # 歩いて移動不可能でないと使わない
            if 0 <= wx < W and 0 <= wy < H and dp[wy][wx] == -1:
                pos.append([wy, wx])
                dp[wy][wx] = dp[y][x] + 1

print(dp[-1][-1])

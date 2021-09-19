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

"""
行列は0か1か
20 + 20だから全探索できそう

encloseするような
4 * 4のうちいくつかのブロックを囲む
dfsでできそうなんだけど
踏んだ頂点をまた踏むとその場で終了
村を全て囲めているか？
踏んだ頂点を持つ

内外判定　何回横切るか
フェンスでdfs　一筆描き
"""
A = [getList() for i in range(4)]
ignore = set()
box = set()
now = 0
ans = 0

def code(x, y):
    return x * 5 + y

def dfs(x, y, px, py, sx, sy):
    global now, ignore
    now += (1 << code(x, y))
    if now in ignore:
        return
    ignore.add(now)
    box.add((x, y, px, py))

    if x == sx and y == sy:
        box.add
        flag = True
        for i in range(4):
            for j in range(4):
                if A[i][j] == 0:
                    continue
                cnt = 0
                for k in range(4):
                    cnt += (((i + k, j + k + 1, i + k + 1, j + k + 1)) in box or ((i + k + 1, j + k + 1, i + k, j + k + 1)) in box)
                if cnt % 2 == 0:
                    flag = False

        if flag:
            ans += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= 4 and 0 <= ny <= 4 and (now & (1 << code(nx, ny)) == 0 or (sx == nx and sy == ny)):
            # 次の点
            dfs(nx, ny, x, y, sx, sy)
    now -= (1 << code(x, y))
    if (x, y, px, py) in box:
        box.remove((x, y, px, py))

for x in range(5):
    for y in range(5):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 4 and 0 <= ny <= 4:
                dfs(nx, ny, x, y, x, y)
        print(ans)

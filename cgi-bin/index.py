from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
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

# 行列掛け算 O(n3)かかる
def array_cnt(ar1, ar2):
    h = len(ar1)
    w = len(ar2[0])
    row = ar1
    col = []
    for j in range(w):
        opt = []
        for i in range(len(ar2)):
            opt.append(ar2[i][j])
        col.append(opt)

    res = [[[0, 0] for i in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            cnt = 0
            for x, y in zip(row[i], col[j]):
                cnt += x * y
            res[i][j] = cnt
    return res

"""
正N角形があります
偶数角形です
間が中心　ちょっと回転させればいい
2Π/Nだけ回転させる
"""
N = getN()
x1, y1 = getNM()
x2, y2 = getNM()

mid = [(x2 + x1) / 2, (y2 + y1) / 2]
vec = [[x1 - mid[0], y1 - mid[1]]]

# vec = [[x, y]]
# vecをang(ラジアンで)だけ回転してくれる
def rotate(vec, ang):
    rot = [[math.cos(ang), -math.sin(ang)], [math.sin(ang), math.cos(ang)]]
    # 行列累乗して返す
    return array_cnt(vec, rot)

r = rotate(vec, -math.pi * 2 / N)
print(mid[0] + r[0][0], mid[1] + r[0][1])

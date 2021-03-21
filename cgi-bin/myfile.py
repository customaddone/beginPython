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

H, W, A, B = getNM()
for bit in range(1 << H * W):
    tatami = []
    for h in range(H):
        opt = []
        for j in range(W):
            if bit & (1 << (h * W + j)):
                opt.append(-1)
            else:
                opt.append(1)
        tatami.append(opt)
    # あとは判定
    # 1を二色で塗る
    bef = tatami
    for h in range(H):
        for w in range(W):
            if tatami[h][w] == -1:
                continue
            # 右
            if w < W - 1 and tatami[h][w + 1] != -1:
                tatami[h][w + 1] = (tatami[h][w] + 1) % 2
            # 下
            if h < H - 1 and tatami[h + 1][w] != -1:
                tatami[h + 1][w] = (tatami[h][w] + 1) % 2
    one = 0
    zero = 0
    hanjo = 0
    for h in range(H):
        for w in range(W):
            if tatami[h][w] == 0:
                zero += 1
            if tatami[h][w] == 1:
                one += 1
            if tatami[h][w] == -1:
                hanjo += 1
    if one == zero and hanjo == B:
        print('bef', bef)
        print(tatami)

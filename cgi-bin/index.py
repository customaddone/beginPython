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

# うなぎ
H, W = 3, 5

distalta = [[0] * W for i in range(H)]
for i in range(H * W):
    # ジグザグに降りていく感じで縦と横のインデックスを決める
    hei = i // W
    if hei % 2 == 0:
        wid = i % W
    else:
        wid = -1 * (i % W) - 1
    distalta[hei][wid] = i
print(distalta)

# 階段
N = 5
dp = [[float('inf')] * N for i in range(N)]
cnt = 1
for i in range(N):
    for j in range(0, N - i):
        dp[j][j + i] = cnt
        cnt += 1
print(dp)

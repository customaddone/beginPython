def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)

H, W = getNM()
N = getN()
A = getList()
dist = []
for i in range(N):
    for j in range(A[i]):
        dist.append(i + 1)
distalta = [[0] * W for i in range(H)]
for i in range(H * W):
    # ジグザグに降りていく感じで縦と横のインデックスを決める
    hei = i // W
    if hei % 2 == 0:
        wid = i % W
    else:
        wid = -1 * (i % W) - 1
    distalta[hei][wid] = dist[i]
for i in distalta:
    print(*i)

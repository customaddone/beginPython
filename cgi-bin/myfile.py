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
def rotate(ar):
    h, w = len(ar), len(ar[0])
    res = [[0] * h for i in range(w)]
    for i in range(h):
        for j in range(w):
            # 上下逆 & 転置
            res[j][h - i - 1] = ar[i][j]
    return res

N = getN()
S = [list(input()) for i in range(N)]
T = [list(input()) for i in range(N)]

# 上下左右にNマスずつ写す

"""
for s in S:
    print(s)
"""

for i in range(-N, N + 1, 1):
    for j in range(-N, N + 1, 1)

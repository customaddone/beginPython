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

# items: [value, weight]
def half_knap(items, const):

    def merge(A, X): # merge A and A + X
        B = []
        i = 0
        nv, nw = X
        # aとその前の要素を比べる
        for v, w in A:
            while A[i][1] + nw < w or (A[i][1] + nw == w and A[i][0] + nv < v):
                B.append([A[i][0] + nv, A[i][1] + nw])
                i += 1
            B.append([v, w])
        # 残ったものを吐き出す
        while i < len(A):
            B.append([A[i][0] + nv, A[i][1] + nw])
            i += 1
        return B

    L = [[0, 0]]
    R = [[0, 0]]
    for item in items[:10]:
        L = merge(L, item)
    for item in items[10:]:
        R = merge(R, item)

    ans = 0
    for v, w in L:
        if w > const:
            break
        while w + R[-1][1] > const:
            R.pop()
        ans = max(ans, v + R[-1][0])

    return ans

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

N, M = getNM()
A = getList()

L = [inf] * (M + 1)
pre = [inf] * (M + 1)
L[0] = pre[0] = 0
for i in range(N):
    nxt = [inf] * (M + 1)
    for j in range(M):
        if j + A[i] <= M:
            # そのままか、切断が１つ増えるか、前のを引き継ぐか
            L[j + A[i]] = min(L[j + A[i]], L[j] + (i > 0), pre[j])
    print(L, pre, nxt)
    pre = nxt

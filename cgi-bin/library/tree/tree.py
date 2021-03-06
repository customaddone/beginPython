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

N = getN()
H = getList()
ignore = [0] * N

for i in range(10):
    res = [0] * N
    for i in range(N):
        if i > 0:
            res[i] += (H[i] - H[i - 1])
        if i < N - 1:
            res[i] += (H[i] - H[i + 1])

    cnt = 0
    for j in range(N):
        if ignore[j] == 0 and res[j] >= 0:
            cnt += 1
            H[j] = 0
            ignore[j] = 1

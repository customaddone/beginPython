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
N = getN()
E = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = getNM()
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

for i in range(N):
    E[i].sort(reverse = True)

ignore = [0] * N
ignore[0] = 1
def dfs(u):
    print(u, E)
    global ignore
    while E[u]:
        v = E[u].pop()
        # まだ
        if ignore[v] == 0:
            ignore[v] = 1
            dfs(v)

dfs(0)

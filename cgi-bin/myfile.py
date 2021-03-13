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

# cargo: 0 ~ N - 1, box: N ~ N + m - 1
# 始点: N + m, 終点: N + m + 1
mcf = MinCostFlow(N + M + 2)
for i in range(N):
    # start ~ 荷物
    mcf.add_edge(N + M, i, 1, 0)
    print(N + M, i)
    for j in range(M):
        if l <= j <= r:
            continue
        # 荷物 ~ box
        if cargo[i][0] <= box[j]:
            print(i, N + j)
            mcf.add_edge(i, N + j, 1, -cargo[i][1])
for j in range(M):
    # box ~ end
    print(N + j, N + M + 1)
    mcf.add_edge(N + j, N + M + 1, 1, 0)

ans = -mcf.flow(N + M, N + M + 1, N)
if ans == -float('inf'):
    print(0)
else:
    print(ans)

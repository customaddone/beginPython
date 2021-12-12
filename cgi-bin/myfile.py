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

N, D = getNM()
event = []
for i in range(N):
    l, r = getNM()
    event.append([l, i, 0]) # 始まり
    event.append([r, i, 1]) # 終わり
event.sort()

now = -inf
C = [0] * N # まだ残っているかのカウンター
ran = [] # 現在区間を走っているもの
for ed, ind, d in event:
    # start
    if d == 0:
        if 

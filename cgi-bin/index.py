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
S = input()
P = []
for i in range(N + 1):
    if S[i] == '0':
        P.append(i)
now = P.pop()
ans = []

while now > 0:
    # 行けない
    if P and P[-1] + M < now:
        print(-1)
        exit()
    next = float('inf')
    # いけるとこまでいく
    while next > 0 and P[-1] + M >= now:
        next = P.pop()

    ans.append(now - next)
    now = next

print(*list(reversed(ans)))

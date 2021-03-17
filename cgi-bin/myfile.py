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

E = [0] * (N + M + 1)
cnt = [0] * (N + M + 1)


# 0からマスiに到達する期待値を求める
for i in range(N + M + 1):
    if 1 < i:
        E[i] += E[i - 1]
        cnt[i] += cnt[i - 1]
    E[i] = max(0, E[i]) # マイナスにはならない
    if cnt[i]:
        E[i] = E[i] * M / cnt[i] # 足したのはM回中cnt[i]回だけなので

    if i < N and not i in A:
        E[i + 1] += (E[i] + 1) / M
        E[i + M + 1] -= (E[i] + 1) / M
        cnt[i + 1] += 1
        cnt[i - 1] -= 1

    print(i, E, cnt, P)

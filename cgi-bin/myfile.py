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
for i in range(1, N):
    next = deepcopy(prev)
    # ここ起点
    next[1 << S[i]][S[i]] += 1
    # 次はS[i] 今まで使ってないなら採用できる
    for bit in range(1 << N):
        # 今現在
        for p in range(10):
            # 今まで使ってない or 現在のものと同じ
            if (not bit & (1 << S[i])) or p == S[i]:
                next[bit | (1 << S[i])][S[i]] += prev[bit][p]
                next[bit | (1 << S[i])][S[i]] %= MOD
    prev = next
    for bit in range(1 << 10):
        if sum(prev[bit]) > 0:
            print(i, bin(bit), prev[bit])

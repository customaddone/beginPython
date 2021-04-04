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

# 1 ~ nまでに各桁のフラグが何本立つか計算する関数
def bitflag(n, flaglist):
    if n > 0:
        for i in range(1, 61):
            split = 2 ** i
            flag1 = (n // split) * (split // 2)
            flag2 = max(n % split + 1 - (split // 2), 0)
            flaglist[i] += flag1 + flag2

l = [[0, 0] for i in range(61)]
# bitの各桁が１か０かをlistaに収納
def splitbit(n):
    for i in range(61):
        if n & (1 << i):
            l[i][1] += 1
        else:
            l[i][0] += 1
for i in A:
    splitbit(i)

# ABC126 F - XOR Matching
# 0 ~ 2^N - 1までには
# 2^0, 2^1...2^N-1のフラグがそれぞれ2^N-1本ずつあり
# xorの総和は0になる
# 2 と 1 3 4 5 6 7はxorの総和がそれぞれ2

M, K = getNM()

if M == 1:
    if K == 0:
        print(0, 1, 1, 0)
    else:
        print(-1)
    exit()

if K >= 2 ** M:
    print(-1)
    exit()

res = [i for i in range(1 << M) if i != K]
res = [K] + res + [K] + res[::-1]
print(*res)

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
E = []
for _ in range(N):
    l, r = getNM()
    E.append([l, r, 1])
    E.append([r + 1, l, -1])
E.sort(reverse = True)

cnt, now = 0, 0
left = 0 # またがってない区間の数
ans = 0
while E:
    nxt = E[-1][0]
    # またがる区間がある　and またがる区間のどれかが中央値になる
    if cnt and left + 1 <= N // 2 + 1 <= left + cnt:
        print(now, nxt, M, left + 1, left + cnt)
    while E and E[-1][0] <= nxt:
        ind, pair, v = E.pop()
        cnt += v
        # 使い終わる　lの値を配分する
        if v == -1:
            left += 1
            M -= pair
    now = nxt

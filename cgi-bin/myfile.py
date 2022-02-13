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

N, L = getNM()
O = [input() + 'o' for i in range(N)]
S = input() + 's'

ran = []
for i in range(N):
    st = -1
    for j in range(L + 1):
        # 一致する区間
        if O[i][j] != S[j]:
            if j - st > 2:
                # 開区間
                ran.append([st + 1, j, i])
            st = j

ran.sort()
ans = [[-1, 0, -1]]
for l, r, i in ran:
    # もし区間を付け加えられるなら
    while l <= ans[-1][0] and ans[-1][1] <= r:
        # 前の奴が区間内に入るなら取り除く
        ans.pop()
    # 前のをできる限り長さ2にする
    if ans[-1][0] <= l and l <= ans[-1][1] <= r and r - ans[-1][0] >= 4:
        l_new = max(ans[-1][0] + 2, l)
        ans[-1][1] = l_new
        ans.append([l_new, r, i])
    print(ans)

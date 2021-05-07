from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
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

mod = 10 ** 9 + 7
MOD = 998244353

INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

N, K = getNM()
A = getList()
d = {}

l = 0
for r in range(N):
    # rの要素を足す
    if A[r] in d:
        d[A[r]] += 1
    else:
        d[A[r]] = 1

    while len(d.items()) > K:
        # 末尾をどんどん除いていく
        d[A[l]] -= 1
        if not d[A[l]]:
            del d[A[l]]
        l += 1
        
    print(l, r)

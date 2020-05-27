def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import fractions
import copy
from itertools import permutations
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

from itertools import permutations
from math import factorial, hypot

N, K = getNM()
S = [getN() for i in range(N)]

# 左を伸ばしていく
# その部分列に含まれる全ての要素の値の積はK以下である。
# lはrをオーバーすることもある

if 0 in S:
    print(N)
    exit()
else:
    l, ans, total = 0, 0, 1
    for r in range(N):
        total *= S[r]
        while total > K and l <= r:
            total //= S[l]
            l += 1
        ans = max(ans, r - l + 1)
print(ans)

# (条件) 連続部分列に含まれる全ての要素の値の和は、K以上である。
N, K = getNM()
A = getList()

left = 0
total = 0
ans = 0

for right in range(0, N):
    total += A[right]
    while total >= K:
        ans += N - right
        total -= A[left]
        left += 1
print(ans)

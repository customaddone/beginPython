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

N = 3

dist = [
[1, 2],
[0, 2],
[0, 1]
]

ans = 0
def rec(s, v):
    global ans
    if s == (1 << N) - 1 and v == 0:
        ans += 1
        return
    for u in dist[v]:
        if s & (1 << u):
            continue
        rec(s | (1 << u), u)

rec(0,0)
print(ans)

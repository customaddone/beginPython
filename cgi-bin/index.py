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
import copy
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

h,w = [int(i) for i in input().split()]
b = [input() for i in range(h)]

ans = [[0]*w for i in range(h)]

for i in range(h):
    res = 0
    for j in range(w):
        if b[i][j] == ".":
            ans[i][j] += res
        if b[i][j] == ".":
            res += 1
        else:
            res = 0

for i in range(h):
    res = 0
    for j in range(w-1,-1,-1):
        if b[i][j] == ".":
            ans[i][j] += res
        if b[i][j] == ".":
            res += 1
        else:
            res = 0

for j in range(w):
    res = 0
    for i in range(h):
        if b[i][j] == ".":
            ans[i][j] += res
        if b[i][j] == ".":
            res += 1
        else:
            res = 0

for j in range(w):
    res = 0
    for i in range(h-1,-1,-1):
        if b[i][j] == ".":
            ans[i][j] += res
        if b[i][j] == ".":
            res += 1
        else:
            res = 0

print(max(max(row) for row in ans) + 1)

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

# 1 + 3 と3 + 1 と1 + 1 + 1 + 1は違う通りになる
# dfs使った方がいい
def dfs(now, sum):
    if sum <= 0:
        return sum == 0
    res = 0
    for i in range(now, W):
        res += dfs(i, sum - a[i])
    return res

a = [1, 3, 5, 7, 9]
W = len(a)
A = 9
print(dfs(0, A))

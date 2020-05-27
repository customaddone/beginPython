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

N = int(input())
P = [list(map(int, input().split())) for i in range(N)]

ans = 0

for ps in permutations(P):
    # 最初の一つ目
    x1, y1 = ps[0]
    # 条件についてループ
    for i in range(n):
        x2, y2 = ps[i]
        ans += hypot(x1-x2, y1-y2)
        x1, y1 = x2, y2
ans /= factorial(n)
print(ans) += 1
print(sumans)

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

S = "14282668646"

prev1 = 0

pw = 1
prev2 = 0

# 1, 14, 142...の余り
for b in S:
    mi = (prev1 * 10 + int(b)) % 2019
    print(mi)
    prev1 = mi

# 6, 46, 646...の余り
for c in S[::-1]:
    m = ((int(c) * pw + int(prev2)) % 2019)
    print(m)
    pw = pw * 10 % 2019
    prev2 = m

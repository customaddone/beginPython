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

def f(x):
    return x + p / pow(2, 2 * x / 3)

p = float(input())
left, right = 0, 100

while right > left + 10 ** -10:
    # mid二つ
    mid1 = (right * 2 + left) / 3
    mid2 = (right + left * 2) / 3
    if f(mid1) >= f(mid2):
        right = mid1
    else:
        left = mid2
print(f(right))

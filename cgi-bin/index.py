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

def dfs(i, sum):
    if i == N:
        return sum == K
    if dfs(i + 1, sum):
        return True
    if dfs(i + 1, sum + A[i]):
        return True
    return False

N, K = map(int, input().split())
A = list(map(int, input().split()))

if dfs(0, 0):
    print("Yes")
else:
    print("No")

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

ans = 0
numlist = [3, 5, 7]

def dfs(s):
    global ans
    if s:
        # 上限
        if int(s) > N:
            return
        elif "3" in s and "5" in s and "7" in s:
            ans += 1
    # dfs
    for i in numlist:
        dfs(s + str(i))
dfs("")
print(ans)

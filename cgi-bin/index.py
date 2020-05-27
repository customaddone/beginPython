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

s = input()
l = ['A', 'T', 'G', 'C']
n = len(s)

num = 0
ans = 0

for i in range(n):
    # 条件を書く
    if s[i] in l:
        num += 1
    else:
        ans = max(num, ans)
        num = 0
ans = max(num, ans)
print(ans)

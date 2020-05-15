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

N = getN()
A = getList()
A.sort()

max = max(A)
index = bisect_left(A, max / 2)
# nCrのrはnの真ん中に行くほど強い
if abs((max / 2) - A[index]) < abs((max / 2) - A[index - 1]):
    ans = [max, A[index]]
else:
    ans = [max, A[index - 1]]
print(*ans)

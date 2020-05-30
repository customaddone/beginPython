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
from fractions import gcd
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

#############
# Main Code #
#############

N = getN()

ans = []
sq = math.floor(math.sqrt(N))
for i in range(sq, 0, -1):
    if N % i == 0:
        ans = [i, N // i]
        break
print(max(len(str(ans[0])), len(str(ans[1]))))

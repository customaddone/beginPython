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

N = getN()
D = getList()
if D[0] != 0:
    print(0)
    exit()
D = Counter(D)
D = sorted(D.items(), key = lambda x: x[0])
if D[0][1] != 1:
    print(0)
    exit()

x1 = 0
y1 = 1
ans = 1
for i in D[1:]:
    if x1 + 1 != i[0]:
        ans = 0
        break
    ans *= y1 ** i[1]
    x1 = i[0]
    y1 = i[1]
print(ans % 998244353)

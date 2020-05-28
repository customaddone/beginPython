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
A = getList()

course = []
x1 = A[0]
for i in A:
    x2 = i
    opt = gcd(x1, x2)
    course.append(opt)
    x1 = opt

reverse = []
y1 = A[-1]
for i in A[::-1]:
    y2 = i
    opt = gcd(y1, y2)
    reverse.append(opt)
    y1 = opt
reverse.sort()

ans = 0
for i in range(N):
    res = 0
    if i == 0:
        res = reverse[1]
    elif i == N - 1:
        res = course[-2]
    else:
        res = gcd(course[i - 1], reverse[i + 1])
    ans = max(ans, res)
print(ans)

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

n, q = map(int, input().split())
dist = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    dist[a - 1].append(b - 1)
    dist[b - 1].append(a - 1)
value = [0 for i in range(n)]

for i in range(q):
    p, x = map(int, input().split())
    value[p - 1] += x
#  重複を防ぐ
ignore = [0] * n
ignore[0] = 1

pos = deque([0])

while len(pos) > 0:
    u = pos.popleft()
    for i in dist[u]:
        if ignore[i] == 0:
            ignore[i] = 1
            value[i] += value[u]
            pos.append(i)

print(*value)

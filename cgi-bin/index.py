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

s = input()
K = getN()

# K <= 5なのでS[i] ~ s[i:i + k]までを取り出すだけでOK
sub = set()
for k in range(1, 6):
    for i in range(len(s)):
        sub.add(s[i:i + k])

sub = sorted(list(sub))
print(sub[K - 1])

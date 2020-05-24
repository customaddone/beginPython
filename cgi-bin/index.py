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

N = getN()
works = []
for i in range(N):
    a, b = getNM()
    works.append([a, b])
works.sort(key = lambda i: i[1])

done = 0
flag = True
for w in works:
    done += w[0]
    if done > w[1]:
        flag = False
print('Yes' if flag else 'No')

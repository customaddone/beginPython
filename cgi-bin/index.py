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
from decimal import *
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
A = getList()

cnt4 = 0
cnt2 = 0
# 実際に数字を並べて確かめてみる
for i in A:
    if i % 4 == 0:
        cnt4 += 1
    elif i % 2 == 0:
        cnt2 += 1

if cnt4 * 2 + 1 >= N:
    print('Yes')
else:
    left = N - cnt4 * 2
    if cnt2 >= left:
        print('Yes')
    else:
        print('No')

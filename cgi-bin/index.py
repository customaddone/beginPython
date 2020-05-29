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

def spliter(n, split):
    splited = n
    cnt = 0

    while splited % split == 0:
        if splited == 0:
            break
        splited //= split
        cnt += 1
    # print(cnt)
    return splited

ans = set()
for i in range(N):
    ans.add(spliter(A[i], 2))
print(len(ans))

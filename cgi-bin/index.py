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

n = int(input())
A = list(map(int, input().split()))
m = 10 ** 9 + 7

from operator import mul
from functools import reduce

# mod使わない時はこっち
def cmb(n, r):
    r = min(n - r, r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

mono = 1
sum = 0
for i in range(1, n):
    if A[i] > A[i - 1]:
        mono += 1
    else:
        # 重複組み合わせ
        sum += cmb(mono + 1, 2)
        mono = 1
sum += cmb(mono + 1, 2)
print(sum)

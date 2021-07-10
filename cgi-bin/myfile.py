from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
from bisect import bisect_left, bisect_right

def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7
INF = float('inf')
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

"""
[0, a)までの転倒数　求められる
[1, a)の転倒数は？
0番目の数字について、a)までの数字の中で自分より小さい数字の個数を引く
bit = BIT(N + 1)
cnt = 0
for i in range(1, N + 1):
    cnt += i - 1 - bit.get(A[i] + 1)
    bit.add(A[i], 1)
    print(cnt)
"""

N, K = getNM()
A = getList()

bit = Comp_BIT(N + 1, A)
print(bit.alter, bit.rev)

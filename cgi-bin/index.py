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

# 0 ~ n - 1までのうち重複を許して個取ってくれる

def rep_comb_pow(n, r):
    def child_pow(i, array):
        global cnt
        if i == r:
            print(array)
            return

        last = -1
        if len(array) > 0:
            last = array[-1]

        for j in range(last, n):
            new_array = array + [j]
            child_pow(i + 1, new_array)

    child_pow(0, [])

rep_comb_pow(4, 2)

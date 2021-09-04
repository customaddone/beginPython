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
2N個のボール　1~Nまで二色ずつ
M本の筒にそれぞれボールが入っている
一番上が一番左のやつ　あんま自由度なさそう　言い換えの問題
ペアは一つしかない dequeで管理　貪欲に？
colorが2つ以上あるものを消す　なくなったら-1 全てが-1になったら終了
"""

N = getN()
A = getList()
B = getList()

P = [[A[i], B[i]] for i in range(N)]
P.sort(reverse = True)

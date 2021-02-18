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

# ABC030 D - へんてこ辞書
# ループを飛ばす

N, A = getNM()
K = getN()
B = getList()
A -= 1
B = [i - 1 for i in B] # 次の行き先

# スタートからtステップでどこまで行けるか
def roop(s, t):
    visited = [-1] * N
    visited[s] = 1

    cnt = 1
    to = B[s]

    while cnt < t:
        cnt += 1
        if visited[to] >= 0:
            cnt += ((K - cnt) // (cnt - visited[to])) * (cnt - visited[to])
            visited = [-1] * N
        visited[to] = cnt
        to = B[to]

    return to

print(roop(A, K) + 1)

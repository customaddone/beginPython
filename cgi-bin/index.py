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

N, M = getNM()
V = getList()
R = getList()
A, B = getNM()
# 個数制限あり重複なし部分和
# 合計でlimitになる通りの数が出てくる
# numは数字のリスト、limitは部分和
def part_sum_dict(array):
    N = len(array)
    prev = defaultdict(int)
    prev[0] = 1

    for i in range(N):
        next = deepcopy(prev)
        for key, value in prev.items():
            next[key + array[i]] += 1
        prev = next

    return prev

su_v = sorted([[key, value] for key, value in part_sum_dict(V).items()])
su_r = sorted([[key, value] for key, value in part_sum_dict(R).items()])

l = 0
r = 0
print(su_v)
print(su_r)
for opt in su_r[1:]:
    while l < len(su_v) and A * opt >= su_v[l][0]:
        l += 1
    while r < len(su_v) and B * opt >= su_v[r][0]:
        r += 1
    print(opt, l, r)

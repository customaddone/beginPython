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

N = 3
A = [6, 10, 15]
# 全てのAiの要素について互いに素か判定
def co_prime(array):
    limit = max(array)
    table = [0] * (limit + 1) # Aに何の要素が何個あるか
    prime = [0] * (limit + 1) # 素数だけを取り出すためのテーブル
    for a in array:
        table[a] += 1
    # iで割り切れるAの要素は何個あるか
    for i in range(2, limit + 1):
        cnt = 0
        # 素数のみを探索する
        if prime[i] == 1:
            continue
        for j in range(i, limit + 1, i):
            cnt += table[j] # iの倍数であるAの要素は何個あるか調べる
            prime[j] = 1

        if cnt > 1:
            return False

    return True

print(co_prime(A))

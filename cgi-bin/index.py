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

# 調和級数
# ABC170 D - Not Divisible
# A内の全てが素数ならエラストテネスにO(N ** 2)かかる

# Amaxが小さいなぁ...
# Amaxが小さいので、長さAmax + 1のテーブルを用意し、Aを小さい順に
# A1の倍数を消す、A2の倍数を消す...を繰り返す
# 実はそんなに計算量は増えない（調和級数) AmaxlogAmax程度
# AのソートにNlogNかかるので合計AmaxlogAmax + NlogN

N = 10
A = [33,18, 45, 28, 8, 19, 89, 86, 2, 4]

def co_prime(array):
    limit = max(array)
    table = [0] * (limit + 1) # Aiの倍数を書き込むテーブル
    double = [0] * (limit + 1) # Aiに何が何回出たかを書き込むテーブル
    array.sort()
    for a in array:
        double[a] += 1
        # すでにaの約数が出ている場合は飛ばす
        if table[a] > 0:
            continue
        # aの倍数2a, 3a, 4a...を書き込む
        for j in range(a * 2, limit + 1, a):
            table[j] = 1

    # 集計
    res = []
    for i in range(1, limit + 1):
        if table[i] == 0 and double[i] == 1:
            res.append(i)

    return res

print(co_prime(A))

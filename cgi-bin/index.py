from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product, combinations_with_replacement
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getListGraph():
    return list(map(lambda x:int(x) - 1, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
(a + b)のa, bの組みとしてありうるものの種類数
12の場合は(1, 11), (2, 10), (10, 2), (11, 1)
Nは大きい　全探索したいけど...

二桁ずつ考えるか
足してiになる数字はそれぞれ10通り
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10] [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
どうせ1つ上の桁には関係がないので...

2021 → 22と01になる
"""

T = getN()
for _ in range(T):
    opt = input()
    a = '0'
    b = '0'
    for i in range(len(opt)):
        if i % 2 == 0:
            a += opt[i]
        else:
            b += opt[i]

    print((int(a) + 1) * (int(b) + 1) - 2)

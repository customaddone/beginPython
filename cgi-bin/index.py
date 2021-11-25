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
sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# 条件が2つのマッチング
# B <= C かつ D <= A
N, M = getNM()
male = [getList() for i in range(N)]
female = [getList() for i in range(M)]

# 年収の低い順にソートする
male.sort()
# 女性の理想の高い順にソートする 理想が同じ場合はきつい女性(低い順から)探索
female.sort(key = lambda i:i[0])
female.sort(key = lambda i:i[1], reverse = True)

q = []
for c, d in female:
    # d <= aを満たす間
    while male and d <= male[-1][0]:
        # bをqにpush
        heappush(q, male.pop()[1])
    # b <= cを満たすように
    print(c, q)

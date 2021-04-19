from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product
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
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

# nCr (mod p)を求めてくれる
# 前処理 p^2
# cmb logn
class Lucas():
    def __init__(self, p):
        self.p = p
        # 前計算
        self.tab = [[0] * p for i in range(p)]
        self.tab[0][0] = 1
        for i in range(1, p):
            self.tab[i][0] = 1
            for j in range(i, 0, -1):
                self.tab[i][j] = (self.tab[i - 1][j - 1] + self.tab[i - 1][j]) % self.p

    def cmb(self, n, r):
        res = 1
        while n:
            ni, ri = n % self.p, r % self.p
            res = (res * self.tab[ni][ri]) % self.p
            n //= self.p
            r //= self.p
        return res

N = getN()
C = list(input())
for i in range(N):
    if C[i] == 'B':
        C[i] = 0
    elif C[i] == 'W':
        C[i] = 1
    else:
        C[i] = 2

lu = Lucas(3)
ans = 0
for i in range(N):
    rev = (N - 1) % 2
    ans += C[i] * ((-1) ** rev) * lu.cmb(N - 1, i)
    ans %= 3

if ans == 0:
    print('B')
elif ans == 1:
    print('W')
else:
    print('R')

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
# sys.setrecursionlimit(1000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

N = input()
L = len(N)

# dp[i][j][k]: i番目まで進む　Nに張り付いてて現在先頭がk
dp = [[[0] * 2 for _ in range(2)] for i in range(L + 1)]
dp[0][0][0] = 1

for i in range(L):
    d = int(N[i])
    for j in range(2):
        # 次の値　Nに張り付いているならd + 1が、そうでなければ10が配られる
        for d_j in range(10 if j else d + 1):
            print(i, j, d_j)
            # 0が継続する
            if d_j == 0:
                dp[i + 1][j | (d_j < d)][0] += dp[i][j][0]
            # 先頭が1になる
            if d_j == 1:
                dp[i + 1][j | (d_j < d)][1] += dp[i][j][0]
            dp[i + 1][j | (d_j < d)][1] += dp[i][j][1]

print(dp)

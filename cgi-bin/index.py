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
# sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-10)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

# codeforces round735
# B-Cobb

# orなので...
# Kが小さいので
# f(i, j) = i * J - K * (Ai | Aj)についてそれぞれの項での最大最小を考える
# i * jの最大値はN(N - 1)
# k * (Ai | Aj)の最大値は2KNなので...
# i * jに比べK * (Ai | Aj)は随分小さい→i * j基準で考える

T = getN()
for _ in range(T):
    N, K = getNM()
    A = [0] + getList()
    ans = -float('inf')
    for i in range(N, 1, -1):
        # k * (Ai | Aj)の最大は2kn
        # 上位だけ調べればいい
        for j in range(i - 1, 0, -1):
            # K * (Ai | Aj)の最大値は K * 2 * N
            if N * (N - 1) - i * j > 2 * K * N:
                break
            ans = max(ans, j * i - K * (A[i] | A[j]))
    print(ans)

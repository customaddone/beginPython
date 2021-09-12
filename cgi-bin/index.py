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

# 完全二分木
# 0:小さいナンバーのチームが勝つ
# 1:大きいナンバーのチームが勝つ
# 操作はそんなに多くなさそう logKぐらい
# dfs(u)
# 2^k - c → >>1, >>1 ...
# 0: child1, 1: child2, ?: child1 + child2
# 正直逆の方がいい

K = getN()
S = list(input())
bi = 2 ** K - 1
dp = [0] * (bi + 1)

def rec(mat, result):
    ind = bi - mat# reverse
    S[bi - ind] = result # rewrite
    while ind >= 1:
        # first game
        if ind > bi // 2:
            if S[bi - ind] == '0' or S[bi - ind] == '1':
                dp[ind] = 1
            else:
                dp[ind] = 2
        # second, third...
        else:
            if S[bi - ind] == '0':
                dp[ind] = dp[ind * 2 + 1]
            elif S[bi - ind] == '1':
                dp[ind] = dp[ind * 2]
            else:
                dp[ind] = dp[ind * 2 + 1] + dp[ind * 2]

        ind //= 2

for i in range(bi):
    rec(i, S[i])

Q = getN()
for _ in range(Q):
    m, r = input().split()
    rec(int(m) - 1, r)
    print(dp[1])

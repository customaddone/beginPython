from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import sys
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
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

"""
3 3
0 1 5
1 0 1
5 1 0
の場合
部門の数 * K + 同じ部門の中の信頼度 - sum(V)
"""

N, K = getNM()
V = [getList() for i in range(N)]
diff = sum([sum(v) for v in V]) // 2

dp = [K] * (1 << N) # 固有値k
dp[0] = 0
for bit in range(1 << N):
    o = [i for i in range(N) if bit & (1 << i)]
    n = len(o)
    for i in range(n):
        for j in range(i + 1, n):
            dp[bit] += V[o[i]][o[j]]

for bit in range(1 << N):
    j = bit # 例: 1010(10)
    while j:
        # 1010と0
        dp[bit] = max(dp[bit], dp[j] + dp[bit ^ j])
        j -= 1 # 1010 → 1001 1だけ減らして数字を変える
        j &= bit # 1010 → 1000 実質引き算 同じ要素があるところまで数字を減らす

print(dp[-1] - diff)

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

# codeforces round650 F1 - Flying Sort (Easy Version)

# distinct
# 前か後ろに置ける
# 操作回数の最小値　前にやった？ BITする
# まず前側の操作だけなら
# 0 2 1 → 1 0 2 → 0 1 2
# 0 1 3 2 → 2 0 1 3 → 1 2 0 3 → 0 1 2 3
# 0 2 3 1 → 1 0 2 3 → 0 1 2 3
# 前からいくつ、後ろからいくつを担当するか
# 2 3 5 1 4 → 2 3   1, 5   4
# 末尾のindexを見る　現在の先頭より後ろにありますか？　あれば操作を行う

# 一番前に置く操作の場合　数字の大きい方から見て行って
# その数字の場所がこれまでの数字の先頭より前にあるかを見る
# 後ろにあれば当該数字を先頭に置く

T = getN()
for _ in range(T):
    N = getN()
    A = getList()
    A = [[A[i], i] for i in range(N)]
    A.sort()

    fore, back = [0] * N, [0] * N
    for i in range(N):
        # fore
        cnt, fir = 0, N
        for j in range(i, -1, -1):
            # do operation
            if A[j][1] > fir:
                fir = -1
                cnt += 1
            fir = min(fir, A[j][1])
        fore[i] = cnt

        # back
        cnt, last = 0, -1
        for j in range(N - i - 1, N):
            if A[j][1] < last:
                last = N
                cnt += 1
            last = max(last, A[j][1])
        back[-i - 1] = cnt

    print(min([fore[i] + back[i] for i in range(N)]))

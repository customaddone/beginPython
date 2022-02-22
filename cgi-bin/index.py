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
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
# sys.setrecursionlimit(10000000)
inf = float('inf')
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

def gene(s1, s2):
    na, nc = len(s1), len(s2)
    La = [[-1, -1] for i in range(na)]
    Lc = [[-1, -1] for i in range(nc)]
    for i in range(na):
        # Cの右端
        #      aaa
        #  aaaaa
        for j in range(i + 1):
            if s1[i - j] == s2[-j - 1] or s1[i - j] == '?' or s2[-j - 1] == '?':
                La[i][1] = i - j
            else:
                break

        # Cの左端
        # aaa
        #   aaaaa
        for j in range(i + 1):
            if s1[-i + j - 1] == s2[j] or s1[-i + j - 1] == '?' or s2[j] == '?':
                La[-i - 1][0] = na - i + j - 1
            else:
                break

    for i in range(nc):
        # Aの右端
        #    aaaaa
        #  aaa
        for j in range(min(na, i + 1)):
            if s1[-j - 1] == s2[i - j] or s1[-j - 1] == '?' or s2[i - j] == '?':
                Lc[i][1] = i - j
            else:
                break
        # Aの左端
        # aaaaa
        #     aaa
        for j in range(min(na, i + 1)):
            if s1[j] == s2[-i + j - 1] or s1[j] == '?' or s2[-i + j - 1] == '?':
                Lc[-i - 1][0] = nc - i + j - 1
            else:
                break

    return La, Lc

"""
A[i]とCの右端を揃えた時に左に何個目まで一致するか
その逆

La[i][0]の場合はN-1まで行けば、La[i][1]の場合は0まで行ったら一致
aba
abcとは1まで一致

aba
  abc 2まで一致
[[1, -1], [-1, -1], [2, -1]]
abc
[[1, 0], [-1, -1], [-1, -1]]
"""

S = [input() for i in range(3)]
S = [[len(s), s] for s in S]
S.sort()
na, A = S[0][0], S[0][1]
nb, B = S[1][0], S[1][1]
nc, C = S[2][0], S[2][1]

print(A, C)
print(gene(A, C))

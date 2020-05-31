def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()

from collections import defaultdict, deque, Counter
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

"""
1
1 1 0 1 0 0 0 1 0 1
3 4 5 6 7 8 9 -2 -3 4 -2
"""
N = getN()
F = []
for i in range(N):
    # これ使う
    f = list(map(str, input().split()))
    bi = ''.join(f)
    F.append(int(bi, 2))
P = []
for i in range(N):
    p = getList()
    P.append(p)
print(F)

# modに!!
ans = -mod
for bit in range(1, 1 << 10):
    cnt = 0
    for j in range(N):
        open = bit & F[j]
        index = str(bin(open)).count('1')
        # print(P[i][index])
        cnt += P[j][index]
    ans = max(ans, cnt)
print(ans)

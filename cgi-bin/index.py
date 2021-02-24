from collections import defaultdict, deque, Counter
import sys
from decimal import *
from heapq import heapify, heappop, heappush
import math
import random
import string
from copy import deepcopy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce, lru_cache
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

# ABC189 C - Mandarin Orange

N = getN()
A = getList()
A = [[A[i], i] for i in range(N)]
A.sort()

ans = 0
check = [0] * N
U = UnionFind(N)

while A:
    now = A[-1][0]
    index = []
    # 同じ数を引き終わるまで引き続ける
    while A and A[-1][0] == now:
        val, ind = A.pop()
        index.append(ind)
        check[ind] = 1

    # uniteする
    for ind in index:
        # 左側と
        if ind > 0 and check[ind - 1] == 1:
            U.union(ind - 1, ind)
        # 右側と
        if ind < N - 1 and check[ind + 1] == 1:
            U.union(ind, ind + 1)

    # 計算
    for ind in index:
        ans = max(ans, now * U.size(ind))

print(ans)

# 技術室奥プログラミングコンテスト#4 Day2
# E - 引きこもり

N, M, Q = getNM()
E = [getList() for i in range(M)]
E.sort(reverse = True, key = lambda i:i[2])
query = getArray(Q)

U = UnionFind(N)
d = [float('inf')] * (10 ** 5 + 7)
d[1] = 0
que = []
for i in range(N):
    heappush(que, [1, i])

# 混ぜこぜでqueにぶち込んで取り出すときにそれが正しいか判定する
while E:
    now = E[-1][2]
    al = []
    # 抜き取る
    while E and E[-1][2] == now:
        a, b, c = E.pop()
        U.union(a - 1, b - 1)
        al.append([a - 1, b - 1])
    # 判定
    for a, b in al:
        heappush(que, [U.size(a), a])
        heappush(que, [U.size(b), b])

    # 正規のやつを引くまで
    while que[0][0] != U.size(U.find(que[0][1])):
        heappop(que)
    d[que[0][0]] = min(d[que[0][0]], now)

for i in range(len(d) - 2, -1, -1):
    d[i] = min(d[i], d[i + 1])

for q in query:
    if d[q] == float('inf'):
        print('trumpet')
    else:
        print(d[q])

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

# edufo 114
# D - The Strongest Build
# We love abc の亜種

# resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
# print(resource.getrlimit(resource.RLIMIT_STACK))

N = getN()
I = [getList()[1:] for i in range(N)]
M = getN()
ban = set()
for i in range(M):
    b = tuple(getListGraph())
    ban.add(b)

count = [len(I[i]) - 1 for i in range(N)]
ans = [0] * N
val = sum([I[i][-1] for i in range(N)])
ignore = set()
ma = 0

# 現在の値だけ持つ　差分を足し引きしていく
def dfs():
    global count, ma, val
    # 値が足りないの or もう探索した　でストップ
    if val <= ma or tuple(count) in ignore:
        return
    ignore.add(tuple(count))

    # 無いのでここで探索ストップ
    if not tuple(count) in ban:
        ma = max(ma, val)
        for i in range(N):
            ans[i] = count[i] + 1
        return

    # ある場合　まだ探索する
    for i in range(N):
        if count[i] > 0:
            val += (-I[i][count[i]] + I[i][count[i] - 1])
            count[i] -= 1
            dfs()
            # countを減らしているので添え字が変わる
            val -= (-I[i][count[i] + 1] + I[i][count[i]])
            count[i] += 1

dfs()
print(*ans)

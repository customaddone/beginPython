def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left

import sys
# sys.setrecursionlimit(1000000)
# list(map(int, input().split()))
mod = 10 ** 9 + 7
# https://atcoder.jp/contests/abc141/tasks/abc141_d

# Nは人、Mは関係の数
N, M, K = getNM()
friend = [[] for i in range(N)]
for i in range(M):
    a, b = getNM()
    friend[a - 1].append(b - 1)
    friend[b - 1].append(a - 1)
blocked = [[] for i in range(N)]
for i in range(K):
    a, b = getNM()
    blocked[a - 1].append(b - 1)
    blocked[b - 1].append(a - 1)
def matcher(n):
    ignore = [0] * (N + 1)
    ignore[n] = 1
    pos = deque([n])
    setfriend = set(friend[n])
    setblocked = set(blocked[n])
    res = set()
    while len(pos) > 0:
        u = pos.popleft()
        for i in friend[u]:
            if ignore[i] > 0:
                continue
            ignore[i] = 1
            if not i in (setfriend | setblocked):
                res.add(i)
            pos.append(i)
    return len(res)
ans = []
for i in range(N):
    ans.append(matcher(i))
print(*ans)

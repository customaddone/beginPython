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
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

N, M = getNM()
dist = [[] for i in range(N + 1)]
for i in range(M):
    a, b = getNM()
    dist[a].append(b)
    dist[b].append(a)

pos = deque([[1, 0]])
ignore = [-1] * (N + 1)
ans = [-1] * (N + 1)
ignore[1] = 0

# 最短経路の求め方
while len(pos) > 0:
    u, time = pos.popleft()
    for i in dist[u]:
        if ignore[i] != -1:
            continue
        ignore[i] = time + 1
        # 経路復元
        ans[i] = u
        pos.append([i, time + 1])
ans.pop(0)
ans.pop(0)

flag = True
for i in ans:
    if i < 0:
        flag = False
if flag:
    print('Yes')
    for i in ans:
        print(i)
else:
    print('No')

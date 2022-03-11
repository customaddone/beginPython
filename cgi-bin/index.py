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
inf = float('inf')
eps = 10 ** (-15)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

#############
# Main Code #
#############

"""
N個の点には入ってないA[i]にもっとも近い点を探す
距離1、距離2...とやっていきたいが点が固まっているとやばい
bfsすればいい
"""

N = getN()
d = {}
ans = [tuple(getList()) for i in range(N)]
P = set(ans)

q = deque([])
# 距離1
for x, y in P:
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (nx, ny) in P:
            d[(x, y)] = (nx, ny)
            # 起点
            q.append((x, y, nx, ny))
            break

while q:
    x, y, sx, sy = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx, ny) in P and not (nx, ny) in d:
            d[(nx, ny)] = (sx, sy)
            q.append((nx, ny, sx, sy))

for x, y in ans:
    print(*d[(x, y)])

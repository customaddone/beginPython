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

from collections import deque

def bfs(s):
    q = deque()
    q.append((s, 1, 1))
    visit = [0] * n0
    visit[s] = 1
    while q:
        i, now1, now2 = q.popleft()
        for j, m in G[i]:
            if not visit[j]:
                if m > 0:
                    dist1[s][j] = now1 * m
                    dist2[s][j] = now2
                else:
                    dist1[s][j] = now1
                    dist2[s][j] = now2 * -m
                if dist1[s][j] % dist2[s][j] == 0:
                    dist1[s][j], dist2[s][j] = dist1[s][j] // dist2[s][j], 1
                q.append((j, dist1[s][j], dist2[s][j]))
                visit[j] = 1
    return

n = int(input())
d = dict()
w = []
n0 = 0
G = [[] for _ in range(405)]
for _ in range(n):
    s, m, l = input().split()
    if not s in d:
        d[s] = n0
        w.append(s)
        n0 += 1
    if not l in d:
        d[l] = n0
        w.append(l)
        n0 += 1
    G[d[l]].append([d[s], int(m)])
    G[d[s]].append([d[l], -int(m)])
dist1 = [[1] * n0 for _ in range(n0)]
dist2 = [[1] * n0 for _ in range(n0)]
for i in range(n0):
    bfs(i)
maxdist = 0
x, y = 0, 0
for i in range(n0):
    for j in range(n0):
        if not dist1[i][j] % dist2[i][j] == 0:
            continue
        nowdist = dist1[i][j] // dist2[i][j]
        if maxdist < nowdist:
            maxdist = nowdist
            x, y = i, j
ans = "".join(map(str, [1, w[y], "=", maxdist, w[x]]))
print(ans)
